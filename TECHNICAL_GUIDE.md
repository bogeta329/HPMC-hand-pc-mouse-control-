# 🎯 Guía Técnica - Hand Gesture PC Controller

## 📐 Arquitectura del Sistema

### Componentes Principales

```
┌─────────────────────────────────────────────────────────┐
│                    Hand Controller                       │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   OpenCV     │  │  MediaPipe   │  │  PyAutoGUI   │  │
│  │ (Captura de  │→ │ (Detección   │→ │  (Control    │  │
│  │   Video)     │  │  de Manos)   │  │  del Mouse)  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Flujo de Datos

1. **Captura**: OpenCV captura frames de la webcam (640x480 @ 30fps)
2. **Detección**: MediaPipe procesa el frame y detecta 21 landmarks por mano
3. **Análisis**: Algoritmo personalizado analiza la posición de los dedos
4. **Reconocimiento**: Se identifica el gesto basado en el estado de los dedos
5. **Acción**: PyAutoGUI ejecuta la acción correspondiente en el sistema

## 🧠 Algoritmo de Detección de Gestos

### Landmarks de MediaPipe

MediaPipe detecta 21 puntos clave en cada mano:

```
        8   12  16  20
        |   |   |   |
    4   |   |   |   |
    |   7   11  15  19
    |   |   |   |   |
    3   6   10  14  18
    |   |   |   |   |
    2   5   9   13  17
    |   └───┴───┴───┘
    1       PALM
    |
    0 (WRIST)
```

### Detección de Dedos Extendidos

```python
# Pulgar: Comparación horizontal (eje X)
thumb_extended = thumb_tip.x < thumb_ip.x

# Otros dedos: Comparación vertical (eje Y)
finger_extended = finger_tip.y < finger_pip.y
```

### Gestos Reconocidos

| Gesto | Dedos Extendidos | Estado | Acción |
|-------|------------------|--------|--------|
| ☝️ | `[?, T, F, F, F]` | MOVING | Mover cursor |
| ✌️ | `[?, T, T, F, F]` | CLICKING | Click izquierdo |
| 🖐️ | `[?, T, T, T, T]` | SCROLLING | Scroll vertical |
| 🤏 | `[T, T, F, F, F]` | DRAGGING | Arrastrar y soltar |

*T = True (extendido), F = False (doblado), ? = cualquiera*

## ⚙️ Parámetros de Configuración

### MediaPipe Hands

```python
self.hands = self.mp_hands.Hands(
    static_image_mode=False,        # Modo video (no imagen estática)
    max_num_hands=1,                # Detectar solo 1 mano
    min_detection_confidence=0.7,   # Confianza mínima para detección
    min_tracking_confidence=0.7     # Confianza mínima para seguimiento
)
```

**Ajustes recomendados:**
- **Buena iluminación**: `min_detection_confidence=0.7`
- **Poca iluminación**: `min_detection_confidence=0.5`
- **Movimientos rápidos**: `min_tracking_confidence=0.5`
- **Precisión máxima**: ambos valores a `0.8` o más

### Suavizado del Cursor

```python
self.smoothing = 5  # Factor de suavizado (1-10)
smooth_x = prev_x + (x - prev_x) / smoothing
```

**Efectos del factor de suavizado:**
- `smoothing = 1`: Sin suavizado (movimiento directo pero nervioso)
- `smoothing = 5`: Balance entre precisión y suavidad (recomendado)
- `smoothing = 10`: Muy suave pero con lag notable

### Cooldown de Clicks

```python
self.click_delay = 0.5  # segundos entre clicks
```

**Ajustes:**
- **Clicks rápidos**: `0.3` segundos
- **Normal**: `0.5` segundos (recomendado)
- **Prevenir clicks accidentales**: `0.8` segundos

## 🎨 Personalización Avanzada

### Agregar Nuevo Gesto

1. **Definir el patrón de dedos** en `detect_gesture()`:

```python
def detect_gesture(self, fingers):
    thumb, index, middle, ring, pinky = fingers
    
    # Nuevo gesto: Solo pulgar y meñique (rock sign 🤘)
    if thumb and not index and not middle and not ring and pinky:
        return GestureState.CUSTOM_ACTION
```

2. **Agregar el estado** al enum:

```python
class GestureState(Enum):
    IDLE = 0
    MOVING = 1
    CLICKING = 2
    SCROLLING = 3
    DRAGGING = 4
    CUSTOM_ACTION = 5  # Nuevo estado
```

3. **Implementar la acción** en el loop principal:

```python
elif gesture_state == GestureState.CUSTOM_ACTION:
    # Tu acción personalizada
    pyautogui.hotkey('win', 'd')  # Mostrar escritorio
```

### Ejemplos de Acciones Personalizadas

```python
# Click derecho
pyautogui.rightClick()

# Doble click
pyautogui.doubleClick()

# Atajos de teclado
pyautogui.hotkey('ctrl', 'c')  # Copiar
pyautogui.hotkey('ctrl', 'v')  # Pegar
pyautogui.hotkey('alt', 'tab')  # Cambiar ventana

# Escribir texto
pyautogui.write('Hola Mundo', interval=0.1)

# Presionar teclas
pyautogui.press('enter')
pyautogui.press('space')
```

## 🔧 Optimización de Rendimiento

### Reducir Latencia

```python
# Reducir resolución de cámara
self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Reducir complejidad de MediaPipe
self.hands = self.mp_hands.Hands(
    model_complexity=0,  # 0=ligero, 1=completo (default)
    max_num_hands=1
)
```

### Mejorar FPS

```python
# Procesar cada N frames
frame_count = 0
if frame_count % 2 == 0:  # Procesar 1 de cada 2 frames
    results = self.hands.process(rgb_frame)
frame_count += 1
```

## 🐛 Debugging

### Visualizar Coordenadas

```python
# Mostrar coordenadas de landmarks
for idx, landmark in enumerate(hand_landmarks.landmark):
    print(f"Landmark {idx}: x={landmark.x:.3f}, y={landmark.y:.3f}")
```

### Logging de Gestos

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# En detect_gesture()
logger.debug(f"Fingers: {fingers}, Gesture: {gesture_state}")
```

### Modo de Prueba (Sin Control del Mouse)

```python
# En __init__()
self.test_mode = True  # Activar modo prueba

# En move_cursor()
if not self.test_mode:
    pyautogui.moveTo(smooth_x, smooth_y)
else:
    print(f"TEST: Would move to ({smooth_x}, {smooth_y})")
```

## 📊 Métricas de Rendimiento

### Benchmarks Típicos

| Hardware | FPS | Latencia | CPU |
|----------|-----|----------|-----|
| i5 8th Gen + Webcam 720p | 25-30 | ~50ms | 15-20% |
| i7 10th Gen + Webcam 1080p | 30+ | ~30ms | 10-15% |
| Laptop básico + Webcam 480p | 15-20 | ~80ms | 25-35% |

### Monitoreo en Tiempo Real

El overlay muestra:
- **FPS**: Frames por segundo procesados
- **State**: Estado actual del gesto
- **Cursor**: Posición del cursor en pantalla

## 🔒 Seguridad y Limitaciones

### Fail-Safe Desactivado

```python
pyautogui.FAILSAFE = False
```

⚠️ **IMPORTANTE**: El fail-safe de PyAutoGUI está desactivado para permitir movimientos suaves. Normalmente, mover el mouse a la esquina superior izquierda detiene PyAutoGUI.

**Para reactivarlo** (recomendado durante desarrollo):
```python
pyautogui.FAILSAFE = True
```

### Limitaciones Conocidas

1. **Iluminación**: Requiere buena iluminación para detección confiable
2. **Fondo**: Fondos complejos pueden afectar la detección
3. **Distancia**: Funciona mejor a 30-60cm de la cámara
4. **Velocidad**: Movimientos muy rápidos pueden perder tracking
5. **Una mano**: Solo detecta una mano a la vez

## 🚀 Mejoras Futuras

### Ideas para Implementar

- [ ] Soporte para dos manos
- [ ] Gestos dinámicos (movimientos en el tiempo)
- [ ] Calibración automática por usuario
- [ ] Perfiles de gestos personalizables
- [ ] Integración con reconocimiento de voz
- [ ] Modo de entrenamiento para nuevos gestos
- [ ] Soporte para múltiples monitores
- [ ] Grabación y reproducción de macros gestuales

## 📚 Referencias

- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- [OpenCV Documentation](https://docs.opencv.org/)
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)

---

**¿Preguntas o problemas?** Consulta el README.md principal o abre un issue.
