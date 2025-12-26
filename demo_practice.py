"""
Hand Detection Demo - Practice gestures without controlling the mouse
This is a safe way to practice and understand the gesture recognition
"""

import cv2
import mediapipe as mp
import time

class HandDetectionDemo:
    def __init__(self):
        """Initialize the demo"""
        # MediaPipe setup
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        
        # Camera setup
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Performance tracking
        self.fps_time = time.time()
        self.fps = 0
        
    def get_finger_states(self, hand_landmarks):
        """Determine which fingers are extended"""
        fingers = []
        
        # Thumb
        thumb_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        thumb_ip = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP]
        fingers.append(thumb_tip.x < thumb_ip.x)
        
        # Other fingers
        finger_tips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP
        ]
        
        finger_pips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_PIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
            self.mp_hands.HandLandmark.RING_FINGER_PIP,
            self.mp_hands.HandLandmark.PINKY_PIP
        ]
        
        for tip, pip in zip(finger_tips, finger_pips):
            fingers.append(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y)
        
        return fingers
    
    def detect_gesture(self, fingers):
        """Detect gesture based on finger states"""
        thumb, index, middle, ring, pinky = fingers
        
        if index and not middle and not ring and not pinky:
            return "MOVE CURSOR", (0, 255, 255)
        elif index and middle and not ring and not pinky:
            return "CLICK", (0, 255, 0)
        elif index and middle and ring and pinky:
            return "SCROLL", (255, 128, 0)
        elif thumb and index and not middle and not ring and not pinky:
            return "DRAG & DROP", (255, 0, 255)
        
        return "IDLE", (100, 100, 100)
    
    def draw_info(self, frame, gesture_name, gesture_color, fingers):
        """Draw information overlay"""
        # Calculate FPS
        current_time = time.time()
        self.fps = 1 / (current_time - self.fps_time)
        self.fps_time = current_time
        
        # Draw semi-transparent overlay
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (400, 250), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
        
        # Title
        cv2.putText(frame, "HAND GESTURE DEMO", (20, 40), 
                    cv2.FONT_HERSHEY_BOLD, 0.7, (255, 255, 255), 2)
        
        # FPS
        cv2.putText(frame, f"FPS: {int(self.fps)}", (20, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Detected Gesture
        cv2.putText(frame, f"Gesture: {gesture_name}", (20, 105), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, gesture_color, 2)
        
        # Finger states
        finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        y_offset = 140
        cv2.putText(frame, "Fingers Extended:", (20, y_offset), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
        for i, (name, state) in enumerate(zip(finger_names, fingers)):
            y_offset += 20
            status = "[X]" if state else "[ ]"
            color = (0, 255, 0) if state else (100, 100, 100)
            cv2.putText(frame, f"{status} {name}", (30, y_offset), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        
        # Instructions
        cv2.putText(frame, "Press 'q' to quit", (20, frame.shape[0] - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
        # Gesture guide (right side)
        guide_x = frame.shape[1] - 250
        guide_y = 30
        cv2.putText(frame, "GESTURE GUIDE:", (guide_x, guide_y), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        gestures = [
            ("1 finger - Move", (0, 255, 255)),
            ("2 fingers - Click", (0, 255, 0)),
            ("All fingers - Scroll", (255, 128, 0)),
            ("Thumb+Index - Drag", (255, 0, 255))
        ]
        
        for i, (text, color) in enumerate(gestures):
            cv2.putText(frame, text, (guide_x, guide_y + 25 + i*25), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
    
    def run(self):
        """Main demo loop"""
        print("=" * 60)
        print("Hand Gesture Detection Demo")
        print("=" * 60)
        print("\nThis demo shows gesture detection WITHOUT controlling the mouse.")
        print("Use this to practice and understand the gestures.\n")
        print("Gestures:")
        print("  - Index finger only -> MOVE CURSOR")
        print("  - Index + Middle -> CLICK")
        print("  - All fingers -> SCROLL")
        print("  - Thumb + Index -> DRAG & DROP")
        print("\nPress 'q' to quit\n")
        print("=" * 60)
        
        while True:
            success, frame = self.cap.read()
            if not success:
                print("Failed to capture frame")
                break
            
            # Flip frame horizontally
            frame = cv2.flip(frame, 1)
            
            # Convert to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Process frame
            results = self.hands.process(rgb_frame)
            
            gesture_name = "NO HAND DETECTED"
            gesture_color = (100, 100, 100)
            fingers = [False, False, False, False, False]
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw hand landmarks
                    self.mp_drawing.draw_landmarks(
                        frame, 
                        hand_landmarks, 
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                        self.mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=2)
                    )
                    
                    # Get finger states
                    fingers = self.get_finger_states(hand_landmarks)
                    
                    # Detect gesture
                    gesture_name, gesture_color = self.detect_gesture(fingers)
                    
                    # Draw gesture indicator
                    if gesture_name != "IDLE":
                        cv2.circle(frame, (frame.shape[1]//2, 50), 30, gesture_color, -1)
                        cv2.putText(frame, "DETECTED!", (frame.shape[1]//2 - 50, 60), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
            # Draw information overlay
            self.draw_info(frame, gesture_name, gesture_color, fingers)
            
            # Display frame
            cv2.imshow('Hand Gesture Demo - Practice Mode', frame)
            
            # Check for quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        print("\nCleaning up...")
        self.cap.release()
        cv2.destroyAllWindows()
        print("Demo stopped.")

def main():
    demo = HandDetectionDemo()
    try:
        demo.run()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        demo.cleanup()
    except Exception as e:
        print(f"\nError: {e}")
        demo.cleanup()

if __name__ == "__main__":
    main()
