# Project Overview - Hand PC Control

## Summary

This project enables **Windows PC control using hand gestures** captured via webcam. It leverages state-of-the-art computer vision to detect and interpret gestures in real-time.

---

## Key Features

### Mouse Control
- Fluid cursor movement
- Left click
- Vertical scroll
- Drag and drop

### Real-time Detection
- 25-30 FPS on modern hardware
- Low latency (~30-50ms)
- Intelligent movement smoothing

### Visual Interface
- Real-time HUD overlay
- Hand landmark visualization
- Gesture state indicators
- FPS counter

### Practice Mode
- Learn gestures without affecting the mouse
- Visual feedback on extended fingers

---

## Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11.0 | Core language |
| **OpenCV** | 4.8.1 | Video capture and processing |
| **MediaPipe** | 0.10.9 | Hand landmark detection |
| **PyAutoGUI** | 0.9.54 | Mouse and keyboard control |
| **NumPy** | 1.24.3 | Numerical operations |

---

## Implemented Gestures

### 1. Move Cursor
- **Fingers**: Index finger only.
- **Action**: Cursor follows index finger tip.

### 2. Left Click
- **Fingers**: Index + Middle fingers.
- **Action**: Performs a left click.
- **Cooldown**: 0.5s between clicks.

### 3. Scroll
- **Fingers**: All fingers extended.
- **Action**: Vertical scrolling (up/down).

### 4. Drag & Drop
- **Fingers**: Thumb + Index (pinch).
- **Action**: Pinch to resize/drag, release to drop.

---

## Usage Guide

### First Run
1. **Install**: `setup.bat`
2. **Verify**: `test.bat`
3. **Practice**: `practice.bat`
4. **Run**: `start_controller.bat`

### Regular Usage
Run `start_controller.bat`. Press `q` to quit.

---

## Performance

### Minimum Requirements
- **CPU**: Intel i3 or equivalent
- **RAM**: 4 GB
- **Webcam**: 480p @ 15fps
- **OS**: Windows 10/11

### Expected Performance
- **FPS**: 15-30 (hardware dependent)
- **CPU Usage**: 15-25%
- **Latency**: 30-80ms

---

## Use Cases

### Presentations
- Slide control without physical devices.
- Pointing and clicking on screen elements.

### Web Navigation
- Scrolling through pages.
- Clicking links.

### Productivity
- Text selection.
- File management.

### Accessibility
- Alternative mouse control method.
- Touch-free interaction.

---

## Customization

The project is designed for easy customization:

- **Sensitivity**: Adjust `self.smoothing` in `hand_controller.py`.
- **New Gestures**: Add conditions in `detect_gesture()`.
- **Custom Actions**: Map gestures to keyboard shortcuts using `pyautogui`.

See `TECHNICAL_GUIDE.md` for details.

---

## Troubleshooting

- **Camera Issues**: Check permissions and ensure no other app is using the webcam.
- **Recognition Issues**: Check lighting and background contrast.
- **Performance**: Lower camera resolution or MediaPipe complexity if lagging.

---

## Security & Privacy

- **Local Processing**: All computation is done on your machine.
- **Offline**: No internet connection required.
- **Open Source**: Full code transparency.

---

## Future Improvements

- [ ] Dual hand support
- [ ] Dynamic gestures (motion-based)
- [ ] Custom gesture profiles
- [ ] Voice command integration
- [ ] Macro recording

---

## License

This project is open source and available for personal and educational use.

---

*Built with Python, OpenCV, and MediaPipe.*
