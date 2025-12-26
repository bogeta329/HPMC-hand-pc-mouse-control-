# Customization Examples

This guide provides code snippets to customize and extend the Hand Gesture Controller.

## 1. Adding New Gestures

### Example: Right Click (Thumb + Pinky)

**Step 1**: Add state to Enum (in `hand_controller.py`)

```python
class GestureState(Enum):
    # ... existing ...
    RIGHT_CLICKING = 5
```

**Step 2**: Detect gesture (in `detect_gesture`)

```python
def detect_gesture(self, fingers):
    thumb, index, middle, ring, pinky = fingers
    
    # New: Thumb + Pinky = Right Click
    if thumb and pinky and not index and not middle and not ring:
        return GestureState.RIGHT_CLICKING
        
    # ... existing ...
```

**Step 3**: Implement Action (in `run` loop)

```python
elif gesture_state == GestureState.RIGHT_CLICKING:
    self.move_cursor_relative(marks, freeze=True)
    self.perform_right_click()
```

**Step 4**: Helper Method

```python
def perform_right_click(self):
    current = time.time()
    if current - self.last_click > 1.0:
        pyautogui.rightClick()
        self.last_click = current
```

---

## 2. Modifying Existing Actions

### Example: Double Click instead of Single Click

Modify `handle_click_status` or create a new handler:

```python
# Instead of pyautogui.click()
pyautogui.doubleClick()
```

### Example: Horizontal Scroll

Modify `perform_scroll`:

```python
def perform_scroll(self, hand_landmarks):
    # use X coordinate instead of Y
    current_x = hand_landmarks.landmark[8].x
    # ... logic to scroll ...
    pyautogui.hscroll(amount)
```

---

## 3. Adjusting Parameters

### Cursor Sensitivity

In `__init__`:
```python
self.sensitivity = 1.5 # Increase for faster cursor
```

### Smoothing

In `__init__`:
```python
self.smoothing = 2 # Lower value = faster response, more jitter
self.smoothing = 8 # Higher value = smoother, more lag
```

### Camera Resolution

Higher resolution = more precision but more CPU usage.
```python
self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```

---

## 4. Keyboard Shortcuts

### Copy / Paste Gestures

**Copy** (Three fingers: Index, Middle, Ring):
```python
# Detect
if index and middle and ring and not pinky: return GestureState.COPY
# Execute
pyautogui.hotkey('ctrl', 'c')
```

**Paste** (Four fingers):
```python
# Detect
if index and middle and ring and pinky: return GestureState.PASTE
# Execute
pyautogui.hotkey('ctrl', 'v')
```

---

## 5. Creating Macros

### Screenshot Macro

**Gesture**: Thumb + Ring finger.
```python
# Execute
pyautogui.hotkey('win', 'shift', 's')
```

### Presentation Control

**Next Slide**: Hand Swipe Right (requires gesture history logic).
**Prev Slide**: Hand Swipe Left.
```python
pyautogui.press('right')
pyautogui.press('left')
```

---

## 6. Advanced Customization

### Gesture History (Swipe Detection)

To detect motion (swipes), you need to track position over time.

```python
self.history = []

def detect_swipe(self, current_x):
    self.history.append(current_x)
    if len(self.history) > 10: self.history.pop(0)
    
    # Check difference between start and end of history
    delta = self.history[-1] - self.history[0]
    if delta > 0.3: return "RIGHT"
    if delta < -0.3: return "LEFT"
```

---

## 7. Visual Feedback

Draw custom shapes on the frame based on state.

```python
if gesture_state == GestureState.CLICKING:
    cv2.circle(frame, CenterPoint, 20, (0, 255, 0), -1) # Green Circle
```

---

## 8. User Profiles

You can save settings to a JSON file and load them at startup.

```python
import json
settings = {"sensitivity": 1.5, "smoothing": 5}
with open('settings.json', 'w') as f: json.dump(settings, f)
```

---

## Tips

1. **Test in Demo Mode**: Use `demo_practice.py` to test detection without mouse interference.
2. **Use Cooldowns**: Always add a time delay between actions like clicks or key presses to prevent spamming.
3. **Logging**: Use `print()` liberally when identifying new gestures to see what the camera is detecting.
