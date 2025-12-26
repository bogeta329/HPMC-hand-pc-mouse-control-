# 🖐️ Hand Gesture PC Controller ("Sci-Fi HUD" Edition)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

Control your Windows PC using hand gestures captured through your webcam! This project uses **OpenCV** for video capture, **MediaPipe** for hand tracking, and **PyAutoGUI** for mouse control, all wrapped in a futuristic "Sci-Fi HUD" interface.

## ✨ Features

- **🖱️ Touch-Free Control**: Move your cursor by pointing with your index finger.
- **🎮 Gaming Mode**: Zero-latency mode (toggle with 'G') for faster response times.
- **🤖 Sci-Fi Visuals**: "Iron Man" style HUD with joint tracking and dynamic overlays.
- **⚡ Smart Smoothing**: Adaptive algorithms for natural, jitter-free cursor movement.
- **👆 Gesture Actions**:
    - **Click**: Pinch thumb & index finger.
    - **Scroll**: Use two fingers.
    - **Drag & Drop**: Pinch and hold.
    - **Right Click**: Extend pinky.

## 📂 Documentation

Detailed documentation is available in the following files:

- [**QUICK START**](QUICK_START.md) - Get up and running in minutes.
- [**HOW TO RUN**](HOW_TO_RUN.md) - Detailed usage instructions.
- [**TECHNICAL GUIDE**](TECHNICAL_GUIDE.md) - Deep dive into the code and algorithms.
- [**PROJECT OVERVIEW**](PROJECT_OVERVIEW.md) - High-level architectural view.
- [**CUSTOMIZATION**](CUSTOMIZATION_EXAMPLES.md) - How to tweak and modify the system.

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hand-pc-control.git
   cd hand-pc-control
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. Run the application:
   ```bash
   python hand_controller.py
   ```
2. **Position your hand** 30-60cm from the camera.
3. **Controls**:
   - **'G' Key**: Toggle Gaming Mode (Red HUD = Active).
   - **'Q' Key**: Quit application.

## 🛠️ Configuration

You can adjust parameters directly in `hand_controller.py`:
- `self.sensitivity`: Cursor speed multiplier.
- `self.smoothing`: Movement smoothing factor (lower = faster, higher = smoother).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool controls your mouse cursor automatically. Use responsibly and be aware of your surroundings when testing gestures!
