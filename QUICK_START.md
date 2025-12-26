# Quick Start - Hand Gesture PC Controller

## Installation in 3 Steps

### 1. Run Setup
```bash
setup.bat
```
This will create the virtual environment and install all dependencies automatically.

### 2. Test the System (Optional but Recommended)
```bash
test.bat
```
Verifies that the camera, MediaPipe, and PyAutoGUI are working correctly.

### 3. Start the Controller
```bash
start_controller.bat
```
Ready! You can now control your PC with hand gestures.

---

## Gesture Controls

### Move Cursor (Touchpad Mode)
**Gesture**: Index finger extended.
**Action**: Works like an invisible touchpad. Move your finger to push the cursor. If you reach the edge of your "comfortable zone", simply lower your finger (or close your hand), reposition your hand to the center, lift your index finger again, and continue moving. Just like lifting your finger on a physical touchpad!

**Tip**: You don't need to move your entire arm; wrist movements work best thanks to the high sensitivity.

```
     ^
    /|      (Move as if touching
   / |       a touchpad in the air)
  /  |
```

### Left Click
**Gesture**: Index + Middle fingers extended.
**Action**: Performs a left click.

```
    ^ ^
    | |
   /| |\
  / | | \
```

### Scroll
**Gesture**: All fingers extended.
**Action**: Move hand up/down to scroll.

```
   ^ ^ ^ ^ ^
   | | | | |
  /| | | | |\
```

### Drag and Drop
**Gesture**: Thumb + Index (pinch).
**Action**: Hold to drag, release to drop.

```
    / \
   /   \
  /     \
```

---

## Recommended Configuration

### Optimal Position
- **Distance**: 30-60 cm from the camera.
- **Lighting**: Good frontal lighting (avoid backlight).
- **Background**: Preferably uniform/static.
- **Height**: Camera at chest/face level.

### Tips for Best Performance
1. **Keep hand in frame**: Ensure your hand is visible to the camera.
2. **Clear gestures**: Extend fingers clearly.
3. **Smooth movements**: Avoid rapid, jerky motions.
4. **Practice**: Familiarize yourself with gestures in a safe environment first.

---

## Common Troubleshooting

### Camera not detected
```bash
# Verify camera function
test.bat
```
- Ensure no other application is using the camera (Zoom, Teams, etc.).

### Gestures not recognized
- Improve lighting.
- Adjust distance from camera.
- Ensure hand contrast with background.

### Erratic cursor movement
- Improve lighting.
- Adjust `smoothing` in `hand_controller.py`.

### Accidental clicks
- Increase `click_delay` in `hand_controller.py`.

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `setup.bat` | Installs dependencies (first time only) |
| `test.bat` | System verification |
| `start_controller.bat` | Starts the gesture controller |
| `q` (in window) | Quits the controller |

---

## Use Cases

- **Presentations**: Navigate slides without a clicker.
- **Web Navigation**: Scroll and click hands-free.
- **Media Control**: Play/Pause or adjust volume (customizable).
- **Casual Gaming**: Point-and-click games.

---

## Important Notes

1. **Fail-safe**: PyAutoGUI fail-safe is disabled for smoother operation. Use with caution.
2. **Performance**: Uses 15-25% CPU on modern hardware.
3. **Privacy**: All processing is local. No data is sent to the internet.
