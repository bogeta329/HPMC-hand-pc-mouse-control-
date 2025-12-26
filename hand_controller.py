"""
Hand Gesture Controller for Windows ("SCI-FI HUD" Edition)
Uses OpenCV and MediaPipe to track hand gestures and control the mouse.
Features:
- Zero-Latency Gaming Mode ('G' Key)
- Adaptive Smart Smoothing
- Futuristic "Iron Man" Visuals
"""

import cv2
import mediapipe as mp
import pyautogui
import numpy as np
from enum import Enum
import time
import math
import sys

# Disable PyAutoGUI fail-safe and pauses
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

class GestureState(Enum):
    """Enum for different gesture states"""
    IDLE = 0            # Fist (Pause)
    MOVING = 1          # Open Palm
    LEFT_CLICK = 2      # Pinch (Click/Drag)
    RIGHT_CLICK = 3     # Pinky / Rock
    SCROLLING = 4       # Two fingers

class HandController:
    def __init__(self):
        # 1. Initialize MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=1, 
            min_detection_confidence=0.8,
            min_tracking_confidence=0.7
        )
        
        # 2. Get Screen Size
        self.screen_width, self.screen_height = pyautogui.size()
        
        # 3. Initialize Camera
        try:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        except Exception as e:
            print(f"Camera Init Error: {e}")
            sys.exit(1)
        
        # 4. Tracking Variables
        self.prev_hand_x = None
        self.prev_hand_y = None
        
        self.sensitivity = 1.3
        self.curr_dx = 0
        self.curr_dy = 0
        
        self.is_dragging = False 
        self.pinch_start_time = 0
        self.prev_scroll_y = 0
        
        self.last_right_click = 0
        self.last_fist_time = 0
        
        # MODES
        self.gaming_mode = False 
        
        # VISUALS
        self.click_anim_time = 0 # For flash effect
        
    def get_finger_states(self, hand_landmarks):
        fingers = []
        thumb_tip = hand_landmarks.landmark[4]
        thumb_ip = hand_landmarks.landmark[3]
        fingers.append(thumb_tip.x < thumb_ip.x) 
        
        tips = [8, 12, 16, 20] 
        pips = [6, 10, 14, 18]
        
        for tip, pip in zip(tips, pips):
            fingers.append(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y)
        return fingers

    def get_distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    def detect_gesture(self, fingers, hand_landmarks):
        thumb, index, middle, ring, pinky = fingers
        
        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]
        
        pinch_dist = self.get_distance(thumb_tip, index_tip)
        is_pinching = pinch_dist < 0.05
        
        # 1. FIST / PAUSE
        if not index and not middle and not ring and not pinky:
            self.last_fist_time = time.time()
            return GestureState.IDLE
            
        # 2. TRANSITION SAFETY
        if (time.time() - self.last_fist_time) < 0.5:
            return GestureState.MOVING
            
        # 3. RIGHT CLICK
        if pinky and not index and not middle and not ring:
             return GestureState.RIGHT_CLICK
        if pinky and index and not middle and not ring: 
             return GestureState.RIGHT_CLICK
            
        # 4. SCROLL
        if index and middle and not ring:
            return GestureState.SCROLLING
            
        # 5. CLICK / DRAG
        if is_pinching:
            return GestureState.LEFT_CLICK
            
        return GestureState.MOVING
    
    def move_cursor_relative(self, hand_landmarks, freeze=False):
        try:
            tracking_point = hand_landmarks.landmark[5]
            curr_x = tracking_point.x
            curr_y = tracking_point.y
            
            if freeze:
                self.prev_hand_x = curr_x
                self.prev_hand_y = curr_y
                return

            if self.prev_hand_x is None:
                self.prev_hand_x = curr_x
                self.prev_hand_y = curr_y
                return
            
            raw_dx = (curr_x - self.prev_hand_x) * self.screen_width
            raw_dy = (curr_y - self.prev_hand_y) * self.screen_height
            
            speed = (raw_dx**2 + raw_dy**2)**0.5
            calc_speed = min(speed, 60.0)
            
            # Smart Smoothing
            t = calc_speed / 60.0 
            smoothing = max(0.1, 0.95 - (0.85 * (t**0.6)))
            
            accel = 1.0
            if speed > 3.0:
                 accel = 1.0 + (speed * 0.08) 
                
            dx = raw_dx * self.sensitivity * accel
            dy = raw_dy * self.sensitivity * accel
            
            self.curr_dx = (dx * (1 - smoothing)) + (self.curr_dx * smoothing)
            self.curr_dy = (dy * (1 - smoothing)) + (self.curr_dy * smoothing)
            
            if abs(self.curr_dx) < 1.0 and abs(self.curr_dy) < 1.0:
                self.curr_dx = 0
                self.curr_dy = 0
                
            mouse_x, mouse_y = pyautogui.position()
            new_x = int(mouse_x + self.curr_dx)
            new_y = int(mouse_y + self.curr_dy)
            new_x = max(0, min(self.screen_width - 1, new_x))
            new_y = max(0, min(self.screen_height - 1, new_y))
            
            self.prev_hand_x = curr_x
            self.prev_hand_y = curr_y
            
            pyautogui.moveTo(new_x, new_y, _pause=False)
            
        except Exception:
            pass
    
    def handle_click_status(self, is_clicking):
        if self.gaming_mode:
            if is_clicking:
                if not self.is_dragging:
                    pyautogui.mouseDown()
                    self.is_dragging = True
                    self.click_anim_time = time.time() # Flash
            else:
                if self.is_dragging:
                    pyautogui.mouseUp()
                    self.is_dragging = False
            return

        current_time = time.time()
        if is_clicking:
            if self.pinch_start_time == 0:
                self.pinch_start_time = current_time
            
            if (current_time - self.pinch_start_time) > 0.2:
                if not self.is_dragging:
                    print(">>> DRAGGING STARTED")
                    pyautogui.mouseDown()
                    self.is_dragging = True
        else:
            if self.is_dragging:
                print(">>> DRAG ENDED")
                pyautogui.mouseUp()
                self.is_dragging = False
            elif self.pinch_start_time != 0:
                print(">>> CLICK EXECUTED!")
                pyautogui.click()
                self.click_anim_time = time.time() # Flash
            
            self.pinch_start_time = 0

    def perform_right_click(self):
        current_time = time.time()
        if current_time - self.last_right_click > 1.0:
            pyautogui.rightClick()
            self.last_right_click = current_time

    def perform_scroll(self, hand_landmarks):
        tracking_point = hand_landmarks.landmark[5]
        current_y = tracking_point.y
        if self.prev_scroll_y != 0:
            delta_y = (current_y - self.prev_scroll_y) * 1000
            if abs(delta_y) > 5:
                scroll_amount = int(delta_y * -2.0)
                pyautogui.scroll(scroll_amount)
        self.prev_scroll_y = current_y

    def draw_sci_fi_hud(self, frame, marks, gesture_state):
        h, w, c = frame.shape
        
        # COLORS (BGR)
        CYAN = (255, 255, 0)
        MAGENTA = (255, 0, 255)
        NEON_GREEN = (50, 255, 50)
        RED = (0, 0, 255)
        WHITE = (255, 255, 255)
        
        # 1. DRAW EXOSKELETON (Custom Lines)
        # Joints to connect
        connections = self.mp_hands.HAND_CONNECTIONS
        for connection in connections:
            start_idx = connection[0]
            end_idx = connection[1]
            
            start_point = marks.landmark[start_idx]
            end_point = marks.landmark[end_idx]
            
            p1 = (int(start_point.x * w), int(start_point.y * h))
            p2 = (int(end_point.x * w), int(end_point.y * h))
            
            # Sci-Fi Line style: Thin, anti-aliased
            cv2.line(frame, p1, p2, CYAN, 1, cv2.LINE_AA)
            
        # 2. DRAW JOINTS (Tech Nodes)
        for id, lm in enumerate(marks.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            # Draw a small filled circle with a ring
            cv2.circle(frame, (cx, cy), 3, (0,0,0), -1) # Black hole
            cv2.circle(frame, (cx, cy), 3, CYAN, 1)     # Cyan rim
        
        # 3. CURSOR TARGET (Index Finger Top)
        idx_tip = marks.landmark[8]
        ix, iy = int(idx_tip.x * w), int(idx_tip.y * h)
        
        # Target Reticle
        color_reticle = NEON_GREEN if not self.gaming_mode else RED
        cv2.circle(frame, (ix, iy), 8, color_reticle, 1, cv2.LINE_AA)
        cv2.line(frame, (ix-12, iy), (ix-4, iy), color_reticle, 1)
        cv2.line(frame, (ix+4, iy), (ix+12, iy), color_reticle, 1)
        cv2.line(frame, (ix, iy-12), (ix, iy-4), color_reticle, 1)
        cv2.line(frame, (ix, iy+4), (ix, iy+12), color_reticle, 1)
        
        # 4. CLICK FLASH (Pulse)
        if (time.time() - self.click_anim_time) < 0.15:
            # Draw expanding white ring
            radius = int((time.time() - self.click_anim_time) * 300) + 10
            cv2.circle(frame, (ix, iy), radius, WHITE, 2)
            
        # 5. DRAG LOADING BAR (If waiting for drag in Desktop Mode)
        if not self.gaming_mode and gesture_state == GestureState.LEFT_CLICK and not self.is_dragging:
            elapsed = time.time() - self.pinch_start_time
            if elapsed > 0:
                # Progress 0.0 to 0.2s
                pct = min(1.0, elapsed / 0.2)
                # Draw arc around center of hand
                wrist = marks.landmark[0]
                wx, wy = int(wrist.x * w), int(wrist.y * h)
                center = ( (ix+wx)//2, (iy+wy)//2 )
                
                # Elliptical arc
                axes = (30, 30)
                angle = 0
                startAngle = 0
                endAngle = int(360 * pct)
                cv2.ellipse(frame, center, axes, angle, startAngle, endAngle, MAGENTA, 2)

    def draw_info_overlay(self, frame, gesture_state):
        h, w, c = frame.shape
        
        # HUD BORDERS in Gaming Mode
        if self.gaming_mode:
            # Red/Purple Border
            color = (0, 0, 255)
            thick = 3
            len_line = 50
            # Corners
            cv2.line(frame, (0,0), (len_line,0), color, thick)
            cv2.line(frame, (0,0), (0,len_line), color, thick)
            
            cv2.line(frame, (w,0), (w-len_line,0), color, thick)
            cv2.line(frame, (w,0), (w,len_line), color, thick)
            
            cv2.line(frame, (0,h), (len_line,h), color, thick)
            cv2.line(frame, (0,h), (0,h-len_line), color, thick)
            
            cv2.line(frame, (w,h), (w-len_line,h), color, thick)
            cv2.line(frame, (w,h), (w,h-len_line), color, thick)
            
            cv2.putText(frame, "COMBAT MODE ACTIVE", (w//2 - 150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        # STATE BOX
        box_x, box_y = 20, 50
        cv2.putText(frame, gesture_state.name, (box_x, box_y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        
        # Instructions
        y_off = h - 20
        cv2.putText(frame, "'G': Game Mode | FIST: Pause | PINCH: Click", (20, y_off), cv2.FONT_HERSHEY_PLAIN, 1.2, (200, 200, 200), 1)

    def run(self):
        print(" HAND CONTROLLER - SCI-FI EDITION")
        print(" Press 'G' for Gaming Mode")
        
        while True:
            try:
                success, frame = self.cap.read()
                if not success: break
                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(rgb_frame)
                gesture_state = GestureState.IDLE
                
                if results.multi_hand_landmarks:
                    for marks in results.multi_hand_landmarks:
                        # NEW: Draw Custom Sci-Fi HUD
                        self.draw_sci_fi_hud(frame, marks, gesture_state)
                        
                        fingers = self.get_finger_states(marks)
                        gesture_state = self.detect_gesture(fingers, marks)
                        
                        if gesture_state == GestureState.IDLE: 
                            self.move_cursor_relative(marks, freeze=True)
                            self.handle_click_status(False)
                        elif gesture_state == GestureState.MOVING:
                            self.move_cursor_relative(marks, freeze=False)
                            self.handle_click_status(False)
                        elif gesture_state == GestureState.LEFT_CLICK:
                            if self.gaming_mode:
                                self.move_cursor_relative(marks, freeze=False)
                            else:
                                should_freeze = not self.is_dragging
                                self.move_cursor_relative(marks, freeze=should_freeze)
                            self.handle_click_status(True)
                        elif gesture_state == GestureState.RIGHT_CLICK:
                            self.move_cursor_relative(marks, freeze=True)
                            self.handle_click_status(False)
                            self.perform_right_click()
                        elif gesture_state == GestureState.SCROLLING:
                            self.handle_click_status(False)
                            self.perform_scroll(marks)
                            self.prev_hand_x = None
                else:
                    self.handle_click_status(False)
                    self.prev_hand_x = None
                    
                self.draw_info_overlay(frame, gesture_state)
                cv2.imshow("Hand Controller", frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'): break
                if key == ord('g'): 
                    self.gaming_mode = not self.gaming_mode
                    print(f"GAMING MODE: {'ON' if self.gaming_mode else 'OFF'}")
                
            except Exception: pass
        
        try:
            if self.is_dragging: pyautogui.mouseUp()
        except: pass
        if hasattr(self, 'cap'): self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try: HandController().run()
    except Exception: input()
