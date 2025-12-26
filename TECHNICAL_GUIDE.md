# Technical Guide - Hand Gesture PC Controller

## System Architecture

### Main Components

- **OpenCV**: Handles video capture from the webcam.
- **MediaPipe**: Performs hand landmark detection (21 points per hand).
- **PyAutoGUI**: Executes mouse and keyboard actions based on interpreted gestures.

### Data Flow

1. **Capture**: OpenCV grabs frames (default 640x480 or 1280x720).
2. **Detection**: MediaPipe processes the frame to find hand landmarks.
3. **Analysis**: Custom algorithm calculates finger states (extended vs folded).
4. **Recognition**: Pattern matching identifies the specific gesture.
5. **Action**: PyAutoGUI simulates the corresponding mouse/keyboard event.

## Gesture Detection Algorithm

### MediaPipe Landmarks

The system tracks 21 key points on the hand:
- 0: Wrist
- 4: Thumb Tip
- 8: Index Tip
- 12: Middle Tip
- 16: Ring Tip
- 20: Pinky Tip

(And intermediate joints for each finger)

### Finger Extension Logic

- **Thumb**: Comparisons are made on the X-axis (horizontal).
  - Extended if tip is further out than the knuckle.
- **Fingers**: Comparisons are made on the Y-axis (vertical).
  - Extended if tip is higher (lower Y value) than the PIP joint.

### Recognition Logic

| Gesture | Finger State (T,I,M,R,P) | State Enum | Action |
|---------|--------------------------|------------|--------|
| Pointer | `[?, T, F, F, F]` | MOVING | Move Cursor |
| Click | `[?, T, T, F, F]` | CLICKING | Left Click |
| Scroll | `[?, T, T, T, T]` | SCROLLING | Scroll |
| Drag | `[T, T, F, F, F]` | DRAGGING | Drag & Drop |

*T=True (Extended), F=False (Folded), ?=Any*

## Configuration Parameters

### MediaPipe Settings

Located in `__init__`:
```python
self.hands = self.mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
```
- **confidence**: Higher (0.8+) = stricter, more precise. Lower (0.5) = faster, forgiving lighting.

### Cursor Smoothing

To prevent jitter, a smoothing algorithm is applied to coordinates:
```python
self.smoothing = 5
new_pos = prev_pos + (target_pos - prev_pos) / smoothing
```
- **Value 1**: No smoothing (fast, raw).
- **Value 10**: Heavy smoothing (slow, fluid).

### Click Cooldown

Prevents double-clicking by accident:
```python
self.click_delay = 0.5 # Seconds
```

## Advanced Customization

### Adding a New Gesture

1. **Define Pattern**: In `detect_gesture`, add a condition for the finger state.
2. **Add Enum**: Add a news state to `GestureState`.
3. **Map Action**: In the main loop, check for the new state and execute code.

### Custom Actions

You can use any PyAutoGUI function:
- `pyautogui.rightClick()`
- `pyautogui.doubleClick()`
- `pyautogui.hotkey('ctrl', 'c')`
- `pyautogui.write('text')`

## Performance Optimization

### Latency Reduction

- Reduce camera resolution:
  ```python
  self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
  ```
- Decrease MediaPipe Model Complexity:
  ```python
  model_complexity=0
  ```

### FPS Improvement

- Process every Nth frame (skip frames) if CPU is limited.
- Ensure good lighting to help MediaPipe track faster.

## Debugging

### Logging

Enable debug prints to see detected finger states:
```python
print(f"Fingers: {fingers} | State: {gesture_state}")
```

### Visual Debugging

The overlay draws the skeleton and current state. Use this to verify if the camera sees your hand correctly.

## Safety & Limitations

### Fail-Safe

PyAutoGUI's fail-safe is **disabled** (`FAILSAFE = False`) to allow full screen movement.
To re-enable: `pyautogui.FAILSAFE = True`. (Moving mouse to corner throws exception).

### Limitations

- **Lighting**: Crucial for tracking.
- **Occlusion**: Hiding fingers prevents detection.
- **Single Hand**: Current logic is optimizing for single-hand control.

## References

- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- [OpenCV Docs](https://docs.opencv.org/)
- [PyAutoGUI Docs](https://pyautogui.readthedocs.io/)
