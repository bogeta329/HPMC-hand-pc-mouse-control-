"""
Test script to verify camera and MediaPipe installation
"""

import cv2
import mediapipe as mp
import sys

def test_camera():
    """Test if camera is accessible"""
    print("Testing camera access...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[X] ERROR: Cannot access camera")
        return False
    
    ret, frame = cap.read()
    if not ret:
        print("[X] ERROR: Cannot read from camera")
        cap.release()
        return False
    
    print(f"[OK] Camera OK - Resolution: {frame.shape[1]}x{frame.shape[0]}")
    cap.release()
    return True

def test_mediapipe():
    """Test MediaPipe hand detection"""
    print("\nTesting MediaPipe...")
    try:
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5
        )
        print("[OK] MediaPipe initialized successfully")
        hands.close()
        return True
    except Exception as e:
        print(f"[X] ERROR: MediaPipe failed - {e}")
        return False

def test_pyautogui():
    """Test PyAutoGUI"""
    print("\nTesting PyAutoGUI...")
    try:
        import pyautogui
        screen_size = pyautogui.size()
        print(f"[OK] PyAutoGUI OK - Screen size: {screen_size.width}x{screen_size.height}")
        return True
    except Exception as e:
        print(f"[X] ERROR: PyAutoGUI failed - {e}")
        return False

def main():
    print("=" * 50)
    print("Hand Gesture Controller - System Test")
    print("=" * 50)
    print()
    
    tests = [
        ("Camera", test_camera),
        ("MediaPipe", test_mediapipe),
        ("PyAutoGUI", test_pyautogui)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"[X] {name} test crashed: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 50)
    print("Test Summary")
    print("=" * 50)
    
    all_passed = True
    for name, result in results:
        status = "[OK] PASS" if result else "[X] FAIL"
        print(f"{name:20} {status}")
        if not result:
            all_passed = False
    
    print("=" * 50)
    
    if all_passed:
        print("\n[SUCCESS] All tests passed! You're ready to use the Hand Gesture Controller.")
        print("Run: start_controller.bat")
        return 0
    else:
        print("\n[WARNING] Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
