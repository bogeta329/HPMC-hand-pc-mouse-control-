# 🖐️ Hand PC Control - Proyecto Completo

## 📦 Resumen del Proyecto

Este proyecto te permite **controlar tu PC Windows usando gestos de mano** capturados a través de tu webcam. Utiliza tecnologías de visión por computadora de última generación para detectar y reconocer gestos en tiempo real.

---

## 🎯 Características Principales

✅ **Control Total del Mouse**
- Movimiento fluido del cursor
- Click izquierdo
- Scroll vertical
- Arrastrar y soltar

✅ **Detección en Tiempo Real**
- 25-30 FPS en hardware moderno
- Latencia mínima (~30-50ms)
- Suavizado inteligente de movimientos

✅ **Interfaz Visual**
- Overlay con información en tiempo real
- Visualización de landmarks de la mano
- Indicadores de estado de gestos
- Contador de FPS

✅ **Modo de Práctica**
- Aprende gestos sin controlar el mouse
- Visualización de dedos extendidos
- Feedback visual instantáneo

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.11.0 | Lenguaje principal |
| **OpenCV** | 4.8.1 | Captura y procesamiento de video |
| **MediaPipe** | 0.10.9 | Detección de landmarks de manos |
| **PyAutoGUI** | 0.9.54 | Control del mouse y teclado |
| **NumPy** | 1.24.3 | Operaciones numéricas |
| **pynput** | 1.7.6 | Control adicional de entrada |

---

## 📁 Estructura del Proyecto

```
HAND PC CONTROL/
│
├── 📄 hand_controller.py      # Controlador principal
├── 📄 demo_practice.py        # Modo de práctica (sin control del mouse)
├── 📄 test_system.py          # Script de verificación del sistema
├── 📄 requirements.txt        # Dependencias del proyecto
│
├── 🚀 setup.bat               # Instalación automática
├── 🚀 start_controller.bat    # Iniciar controlador
├── 🚀 practice.bat            # Modo de práctica
├── 🚀 test.bat                # Verificar sistema
│
├── 📖 README.md               # Documentación principal
├── 📖 QUICK_START.md          # Guía de inicio rápido
├── 📖 TECHNICAL_GUIDE.md      # Guía técnica avanzada
├── 📖 PROJECT_OVERVIEW.md     # Este archivo
│
├── 🔧 .gitignore              # Archivos ignorados por Git
└── 📁 venv/                   # Entorno virtual (generado)
```

---

## 🎮 Gestos Implementados

### 1. Mover Cursor 👆
- **Dedos**: Solo índice extendido
- **Acción**: El cursor sigue tu dedo índice
- **Uso**: Navegación general

### 2. Click Izquierdo ✌️
- **Dedos**: Índice + Medio extendidos
- **Acción**: Click izquierdo del mouse
- **Cooldown**: 0.5 segundos entre clicks

### 3. Scroll 🖐️
- **Dedos**: Todos los dedos extendidos
- **Acción**: Scroll vertical (arriba/abajo)
- **Uso**: Navegar por páginas largas

### 4. Arrastrar y Soltar 🤏
- **Dedos**: Pulgar + Índice (pellizcar)
- **Acción**: Mantener para arrastrar, soltar para dejar
- **Uso**: Mover archivos, seleccionar texto

---

## 🚀 Guía de Uso Rápida

### Primera Vez

1. **Instalar**
   ```bash
   setup.bat
   ```

2. **Verificar**
   ```bash
   test.bat
   ```

3. **Practicar** (recomendado)
   ```bash
   practice.bat
   ```

4. **Usar**
   ```bash
   start_controller.bat
   ```

### Uso Regular

```bash
start_controller.bat
```

Presiona `q` en la ventana del controlador para salir.

---

## 📊 Rendimiento

### Requisitos Mínimos
- **CPU**: Intel i3 o equivalente
- **RAM**: 4 GB
- **Webcam**: 480p @ 15fps
- **OS**: Windows 10/11

### Rendimiento Esperado
- **FPS**: 15-30 (dependiendo del hardware)
- **CPU**: 15-25% de uso
- **RAM**: ~200-300 MB
- **Latencia**: 30-80ms

---

## 🎓 Casos de Uso

### 🎤 Presentaciones
- Control de slides sin tocar el teclado
- Interacción natural con la audiencia
- Apuntar y hacer click en elementos

### 🌐 Navegación Web
- Scroll por páginas
- Click en enlaces
- Navegación hands-free

### 📝 Productividad
- Selección de texto
- Arrastrar archivos
- Navegación en documentos

### 🎮 Entretenimiento
- Juegos casuales
- Control de media players
- Navegación en aplicaciones

### ♿ Accesibilidad
- Control alternativo del mouse
- Ideal para personas con movilidad limitada
- Interacción sin contacto

---

## 🔧 Personalización

El proyecto está diseñado para ser fácilmente personalizable:

### Ajustar Sensibilidad
```python
# En hand_controller.py
self.smoothing = 5  # Cambiar entre 1-10
```

### Agregar Nuevos Gestos
```python
# Definir nuevo patrón de dedos
if thumb and middle and not index:
    return GestureState.CUSTOM_ACTION
```

### Modificar Acciones
```python
# Agregar click derecho, atajos de teclado, etc.
pyautogui.rightClick()
pyautogui.hotkey('ctrl', 'c')
```

Consulta `TECHNICAL_GUIDE.md` para más detalles.

---

## 🐛 Solución de Problemas

### Cámara no detectada
- Cierra otras aplicaciones que usen la cámara
- Verifica permisos de la cámara en Windows

### Gestos no reconocidos
- Mejora la iluminación
- Usa un fondo uniforme
- Mantén la mano a 30-60cm de la cámara

### Rendimiento bajo
- Cierra aplicaciones innecesarias
- Reduce la resolución de la cámara
- Ajusta `model_complexity` en MediaPipe

---

## 📚 Documentación Adicional

- **README.md**: Documentación completa con instalación y uso
- **QUICK_START.md**: Guía rápida en español
- **TECHNICAL_GUIDE.md**: Arquitectura, algoritmos y personalización
- **Código fuente**: Comentarios detallados en cada archivo

---

## 🔒 Seguridad y Privacidad

✅ **100% Local**: Todo el procesamiento se hace en tu PC  
✅ **Sin Internet**: No requiere conexión a internet  
✅ **Sin Datos Enviados**: Ningún dato sale de tu computadora  
✅ **Open Source**: Código completamente visible y auditable  

---

## 🎯 Próximas Mejoras Sugeridas

- [ ] Soporte para dos manos simultáneas
- [ ] Gestos dinámicos (movimientos en el tiempo)
- [ ] Click derecho con gesto personalizado
- [ ] Perfiles de gestos guardables
- [ ] Integración con comandos de voz
- [ ] Soporte para múltiples monitores
- [ ] Calibración automática por usuario
- [ ] Grabación y reproducción de macros

---

## 📞 Soporte

Si encuentras problemas:

1. Revisa `QUICK_START.md` para soluciones comunes
2. Ejecuta `test.bat` para diagnosticar el sistema
3. Consulta `TECHNICAL_GUIDE.md` para configuración avanzada
4. Revisa los comentarios en el código fuente

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

---

## 🙏 Agradecimientos

Este proyecto utiliza las siguientes tecnologías de código abierto:

- **Google MediaPipe**: Framework de ML para detección de manos
- **OpenCV**: Biblioteca de visión por computadora
- **PyAutoGUI**: Automatización de GUI en Python

---

## ✨ Conclusión

Este proyecto demuestra el poder de la visión por computadora moderna para crear interfaces naturales e intuitivas. Con solo una webcam y Python, puedes controlar tu PC usando gestos de mano en tiempo real.

**¡Disfruta controlando tu PC con las manos!** 🎉

---

*Creado con ❤️ usando Python, OpenCV y MediaPipe*
