# 🎨 Ejemplos de Personalización

Este archivo contiene ejemplos de código para personalizar y extender el Hand Gesture Controller.

## 📋 Tabla de Contenidos

1. [Agregar Nuevos Gestos](#agregar-nuevos-gestos)
2. [Modificar Acciones Existentes](#modificar-acciones-existentes)
3. [Ajustar Parámetros](#ajustar-parámetros)
4. [Agregar Atajos de Teclado](#agregar-atajos-de-teclado)
5. [Crear Macros](#crear-macros)

---

## 1. Agregar Nuevos Gestos

### Ejemplo: Click Derecho (Pulgar + Meñique)

**Paso 1**: Agregar el estado al enum (línea ~10 en hand_controller.py)

```python
class GestureState(Enum):
    IDLE = 0
    MOVING = 1
    CLICKING = 2
    SCROLLING = 3
    DRAGGING = 4
    RIGHT_CLICKING = 5  # Nuevo estado
```

**Paso 2**: Detectar el gesto (en el método `detect_gesture`, línea ~70)

```python
def detect_gesture(self, fingers):
    thumb, index, middle, ring, pinky = fingers
    
    # ... gestos existentes ...
    
    # Nuevo: Pulgar + Meñique = Click derecho
    elif thumb and not index and not middle and not ring and pinky:
        return GestureState.RIGHT_CLICKING
    
    return GestureState.IDLE
```

**Paso 3**: Implementar la acción (en el método `run`, línea ~200)

```python
elif gesture_state == GestureState.RIGHT_CLICKING:
    cursor_pos = self.move_cursor(hand_landmarks)
    if self.perform_right_click():
        cv2.circle(frame, (frame.shape[1]//2, frame.shape[0]//2), 
                 50, (0, 0, 255), 3)  # Feedback visual rojo
```

**Paso 4**: Agregar el método de click derecho

```python
def perform_right_click(self):
    """Perform a right mouse click with cooldown"""
    current_time = time.time()
    if current_time - self.last_click_time > self.click_delay:
        pyautogui.rightClick()
        self.last_click_time = current_time
        return True
    return False
```

---

## 2. Modificar Acciones Existentes

### Ejemplo: Doble Click en lugar de Click Simple

Modificar el método `perform_click`:

```python
def perform_click(self):
    """Perform a double click with cooldown"""
    current_time = time.time()
    if current_time - self.last_click_time > self.click_delay:
        pyautogui.doubleClick()  # Cambio aquí
        self.last_click_time = current_time
        return True
    return False
```

### Ejemplo: Scroll Horizontal en lugar de Vertical

Modificar el método `perform_scroll`:

```python
def perform_scroll(self, hand_landmarks):
    """Perform horizontal scrolling based on hand position"""
    index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
    current_x = index_tip.x  # Cambio: usar X en lugar de Y
    
    if self.prev_scroll_x != 0:
        delta_x = (current_x - self.prev_scroll_x) * 1000
        if abs(delta_x) > 5:
            scroll_amount = int(delta_x / 10)
            pyautogui.hscroll(scroll_amount)  # Scroll horizontal
    
    self.prev_scroll_x = current_x
```

---

## 3. Ajustar Parámetros

### Sensibilidad del Cursor

```python
# En __init__ (línea ~30)
self.smoothing = 3  # Más rápido (menos suavizado)
# o
self.smoothing = 8  # Más suave (más lag)
```

### Velocidad de Click

```python
# En __init__ (línea ~35)
self.click_delay = 0.3  # Clicks más rápidos
# o
self.click_delay = 1.0  # Clicks más lentos (más seguros)
```

### Confianza de Detección

```python
# En __init__ (línea ~15)
self.hands = self.mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,  # Más sensible (detecta más fácil)
    min_tracking_confidence=0.5    # Menos preciso pero más rápido
)
```

### Resolución de Cámara

```python
# En __init__ (línea ~25)
# Para mejor rendimiento:
self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Para mejor calidad:
self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
```

---

## 4. Agregar Atajos de Teclado

### Ejemplo: Copiar/Pegar con Gestos

**Gesto para Copiar** (Pulgar + Índice + Medio):

```python
# En detect_gesture
elif thumb and index and middle and not ring and not pinky:
    return GestureState.COPY

# En run
elif gesture_state == GestureState.COPY:
    pyautogui.hotkey('ctrl', 'c')
    print("Copiado!")
```

**Gesto para Pegar** (Todos menos pulgar):

```python
# En detect_gesture
elif not thumb and index and middle and ring and pinky:
    return GestureState.PASTE

# En run
elif gesture_state == GestureState.PASTE:
    pyautogui.hotkey('ctrl', 'v')
    print("Pegado!")
```

### Ejemplo: Cambiar de Ventana (Alt+Tab)

```python
# En detect_gesture
elif thumb and middle and not index and not ring and not pinky:
    return GestureState.SWITCH_WINDOW

# En run
elif gesture_state == GestureState.SWITCH_WINDOW:
    if self.perform_window_switch():
        print("Cambiando ventana...")

# Nuevo método
def perform_window_switch(self):
    current_time = time.time()
    if current_time - self.last_action_time > 1.0:  # Cooldown de 1 segundo
        pyautogui.hotkey('alt', 'tab')
        self.last_action_time = current_time
        return True
    return False
```

---

## 5. Crear Macros

### Ejemplo: Macro de Captura de Pantalla

```python
# En detect_gesture
elif thumb and ring and not index and not middle and not pinky:
    return GestureState.SCREENSHOT

# En run
elif gesture_state == GestureState.SCREENSHOT:
    self.take_screenshot()

# Nuevo método
def take_screenshot(self):
    current_time = time.time()
    if current_time - self.last_action_time > 2.0:
        # Captura de pantalla
        pyautogui.hotkey('win', 'shift', 's')
        print("Captura de pantalla!")
        self.last_action_time = current_time
```

### Ejemplo: Macro de Presentación

```python
# Avanzar slide (3 dedos arriba)
elif not thumb and index and middle and ring and not pinky:
    return GestureState.NEXT_SLIDE

# Retroceder slide (3 dedos abajo)
elif not thumb and not index and middle and ring and pinky:
    return GestureState.PREV_SLIDE

# En run
elif gesture_state == GestureState.NEXT_SLIDE:
    pyautogui.press('right')  # o 'space'
    
elif gesture_state == GestureState.PREV_SLIDE:
    pyautogui.press('left')
```

---

## 6. Gestos Avanzados con Movimiento

### Ejemplo: Detectar Movimiento de Barrido

```python
def __init__(self):
    # ... código existente ...
    self.gesture_history = []
    self.swipe_threshold = 0.3

def detect_swipe(self, hand_landmarks):
    """Detectar barrido horizontal"""
    index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
    
    # Guardar posición
    self.gesture_history.append(index_tip.x)
    
    # Mantener solo últimos 10 frames
    if len(self.gesture_history) > 10:
        self.gesture_history.pop(0)
    
    # Detectar barrido
    if len(self.gesture_history) >= 10:
        delta = self.gesture_history[-1] - self.gesture_history[0]
        
        if delta > self.swipe_threshold:
            return "SWIPE_RIGHT"
        elif delta < -self.swipe_threshold:
            return "SWIPE_LEFT"
    
    return None

# Usar en run
swipe = self.detect_swipe(hand_landmarks)
if swipe == "SWIPE_RIGHT":
    pyautogui.hotkey('alt', 'right')  # Adelante en navegador
elif swipe == "SWIPE_LEFT":
    pyautogui.hotkey('alt', 'left')   # Atrás en navegador
```

---

## 7. Agregar Feedback Visual Personalizado

### Ejemplo: Círculo de Color según Gesto

```python
def draw_gesture_indicator(self, frame, gesture_state):
    """Dibuja un indicador visual del gesto actual"""
    center_x = frame.shape[1] // 2
    center_y = 50
    
    colors = {
        GestureState.MOVING: (0, 255, 255),      # Amarillo
        GestureState.CLICKING: (0, 255, 0),      # Verde
        GestureState.SCROLLING: (255, 128, 0),   # Naranja
        GestureState.DRAGGING: (255, 0, 255),    # Magenta
        GestureState.IDLE: (100, 100, 100)       # Gris
    }
    
    color = colors.get(gesture_state, (100, 100, 100))
    cv2.circle(frame, (center_x, center_y), 30, color, -1)
    cv2.putText(frame, gesture_state.name, (center_x - 50, center_y + 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

# Llamar en el loop principal
self.draw_gesture_indicator(frame, gesture_state)
```

---

## 8. Modo de Depuración

### Ejemplo: Logging Detallado

```python
import logging

# En __init__
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='hand_controller.log'
)
self.logger = logging.getLogger(__name__)

# Usar en el código
self.logger.debug(f"Fingers: {fingers}")
self.logger.info(f"Gesture detected: {gesture_state}")
self.logger.warning(f"Low FPS: {self.fps}")
```

---

## 9. Perfiles de Usuario

### Ejemplo: Guardar y Cargar Configuración

```python
import json

def save_settings(self):
    """Guardar configuración actual"""
    settings = {
        'smoothing': self.smoothing,
        'click_delay': self.click_delay,
        'detection_confidence': 0.7,
        'tracking_confidence': 0.7
    }
    
    with open('user_settings.json', 'w') as f:
        json.dump(settings, f, indent=4)
    
    print("Configuración guardada!")

def load_settings(self):
    """Cargar configuración guardada"""
    try:
        with open('user_settings.json', 'r') as f:
            settings = json.load(f)
        
        self.smoothing = settings.get('smoothing', 5)
        self.click_delay = settings.get('click_delay', 0.5)
        
        print("Configuración cargada!")
    except FileNotFoundError:
        print("No se encontró archivo de configuración, usando valores por defecto")
```

---

## 💡 Consejos para Personalización

1. **Prueba en modo demo primero**: Usa `demo_practice.py` para probar nuevos gestos sin afectar el mouse

2. **Comenta el código original**: Antes de modificar, comenta el código original para poder volver atrás

3. **Usa cooldowns**: Agrega delays entre acciones para evitar activaciones accidentales

4. **Feedback visual**: Siempre agrega feedback visual para saber qué gesto se detectó

5. **Logging**: Usa logging para depurar problemas

6. **Gestos únicos**: Asegúrate de que cada gesto sea claramente diferente de los demás

7. **Prueba gradualmente**: Agrega un gesto a la vez y pruébalo bien antes de agregar más

---

## 🔗 Referencias Útiles

- **PyAutoGUI Docs**: https://pyautogui.readthedocs.io/
- **MediaPipe Hands**: https://google.github.io/mediapipe/solutions/hands.html
- **OpenCV Docs**: https://docs.opencv.org/

---

¡Experimenta y crea tus propios gestos personalizados! 🚀
