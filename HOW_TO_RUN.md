# Execution Guide - Hand Gesture PC Controller

## Important: How to Run the Scripts

There are **TWO ways** to run the scripts, depending on your environment:

---

## Option 1: File Explorer (RECOMMENDED)

### Easiest and Most Reliable

Simply **double-click** the `.bat` files:

- `setup.bat` - Initial installation
- `practice.bat` - Practice mode
- `start_controller.bat` - Start controller
- `test.bat` - specific system test

**This method works consistently without compatibility issues.**

---

## Option 2: Terminal / Command Line

### CMD (Command Prompt)

```cmd
practice.bat
```

### PowerShell

You have 2 options:

**A) Run the .bat via CMD:**
```powershell
cmd /c practice.bat
```

**B) Use the PowerShell scripts (.ps1):**
```powershell
.\practice.ps1
```

---

## All Available Commands

### From CMD
```cmd
setup.bat              # Install
test.bat               # Verify
practice.bat           # Practice Mode
start_controller.bat   # Start Controller
```

### From PowerShell
```powershell
# Option 1: Run .bat via cmd
cmd /c setup.bat

# Option 2: Use .ps1 scripts
.\test.ps1
.\practice.ps1
.\start_controller.ps1
```

### From File Explorer
```
Double-click any .bat file
```

---

## Why Two Types of Scripts?

Batch files (`.bat`) are designed for **CMD**, not PowerShell. Running them directly in PowerShell can sometimes cause path or environment issues.

**Solutions:**
1. **Double-click** the file (Recommended).
2. Execute with `cmd /c script.bat` in PowerShell.
3. Use the provided `.ps1` files in PowerShell.

---

## Quick Start Summary

### First Time:

1. **Double-click:** `setup.bat` (Wait for completion)
2. **Double-click:** `test.bat` (Verify system)
3. **Double-click:** `practice.bat` (Practice gestures)
4. **Double-click:** `start_controller.bat` (Start control)

### Regular Use:

**Double-click:** `start_controller.bat`

---

## File Summary

### Batch Scripts (CMD / Double-click):
- `setup.bat`
- `test.bat`
- `practice.bat`
- `start_controller.bat`

### PowerShell Scripts:
- `test.ps1`
- `practice.ps1`
- `start_controller.ps1`

### Python Code:
- `hand_controller.py`
- `demo_practice.py`
- `test_system.py`

---

## Quick Verification

To verify installation is correct:

**From Explorer:**
- Double-click `test.bat`

**From PowerShell:**
```powershell
cmd /c test.bat
# or
.\test.ps1
```

You should see:
```
[OK] Camera PASS
[OK] MediaPipe PASS
[OK] PyAutoGUI PASS
```

---

**Enjoy controlling your PC with hand gestures!**
