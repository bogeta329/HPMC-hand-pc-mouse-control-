# 🚀 Inicio Rápido - Hand Gesture PC Controller

## Instalación en 3 Pasos

### 1️⃣ Ejecutar Setup
```bash
setup.bat
```
Esto creará el entorno virtual e instalará todas las dependencias automáticamente.

### 2️⃣ Probar el Sistema (Opcional pero Recomendado)
```bash
test.bat
```
Verifica que la cámara, MediaPipe y PyAutoGUI funcionen correctamente.

### 3️⃣ Iniciar el Controlador
```bash
start_controller.bat
```
¡Listo! Ahora puedes controlar tu PC con gestos de mano.

---

## 🎮 Controles de Gestos

### Mover el Cursor (NUEVO: Modo Touchpad)
**Gesto**: ☝️ Solo dedo índice extendido  
**Acción**: Funciona como un touchpad invisible. 
Mueve el dedo para empujar el cursor. Si llegas al borde de tu "zona cómoda", simplemente **baja el dedo (o cierra la mano)**, reposiciona tu mano al centro, levanta el dedo índice de nuevo y sigue moviendo. ¡Como levantar el dedo en un touchpad!

**Tip**: No necesitas mover el brazo entero, solo la muñeca o pequeños movimientos funcionan mejor gracias a la alta sensibilidad.

```
     ☝️
    /|      (Mueve como si tocaras
   / |       un touchpad en el aire)
  /  |
```

### Click Izquierdo
**Gesto**: ✌️ Índice + Medio extendidos  
**Acción**: Realiza un click izquierdo

```
    ✌️
    /|\
   / | \
  /  |  \
```

### Scroll (Desplazamiento)
**Gesto**: 🖐️ Todos los dedos extendidos  
**Acción**: Mueve la mano arriba/abajo para hacer scroll

```
    🖐️
   /||||\
  / |||| \
 /  ||||  \
```

### Arrastrar y Soltar
**Gesto**: 🤏 Pulgar + Índice (como pellizcar)  
**Acción**: Mantén el gesto para arrastrar, suelta para soltar

```
    🤏
    /\
   /  \
  /    \
```

---

## ⚙️ Configuración Recomendada

### Posición Óptima
- **Distancia**: 30-60 cm de la cámara
- **Iluminación**: Buena luz frontal (evita contraluz)
- **Fondo**: Preferiblemente uniforme y sin movimiento
- **Altura**: Cámara a la altura de tu pecho/cara

### Consejos para Mejor Rendimiento
1. **Mantén la mano dentro del cuadro** de la cámara
2. **Gestos claros**: Extiende bien los dedos para cada gesto
3. **Movimientos suaves**: Evita movimientos bruscos
4. **Practica primero**: Familiarízate con los gestos antes de usar aplicaciones importantes

---

## 🔧 Solución de Problemas Comunes

### La cámara no se detecta
```bash
# Verifica que la cámara funcione
test.bat
```
- Asegúrate de que ninguna otra aplicación esté usando la cámara
- Prueba cerrar Zoom, Teams, Skype, etc.

### Los gestos no se reconocen
- Mejora la iluminación
- Acércate o aléjate de la cámara
- Asegúrate de que tu mano sea claramente visible
- Evita fondos con colores similares a tu piel

### El cursor se mueve de forma errática
- Mejora la iluminación
- Reduce movimientos de fondo
- Ajusta el parámetro `smoothing` en `hand_controller.py` (línea ~30)

### Clicks accidentales
- Aumenta `click_delay` en `hand_controller.py` (línea ~35)
- Practica hacer gestos más deliberados

---

## 📝 Comandos Útiles

| Comando | Descripción |
|---------|-------------|
| `setup.bat` | Instala dependencias (solo primera vez) |
| `test.bat` | Verifica que todo funcione |
| `start_controller.bat` | Inicia el controlador de gestos |
| `q` (en ventana) | Cierra el controlador |

---

## 🎯 Casos de Uso

### Presentaciones
- Navega por slides sin tocar el teclado
- Apunta y haz click en elementos importantes

### Navegación Web
- Scroll por páginas web
- Click en enlaces y botones

### Edición de Documentos
- Selecciona texto (arrastra)
- Navega por documentos largos (scroll)

### Gaming Casual
- Juegos de apuntar y hacer click
- Navegación en menús

---

## ⚠️ Notas Importantes

1. **Fail-safe desactivado**: El fail-safe de PyAutoGUI está desactivado para permitir movimientos suaves. Ten cuidado al usar el controlador.

2. **Rendimiento**: El sistema usa ~15-25% de CPU en hardware moderno. Si experimentas lag, cierra otras aplicaciones.

3. **Privacidad**: Todo el procesamiento se hace localmente. No se envía ningún dato a internet.

4. **Práctica**: Tómate 5-10 minutos para practicar los gestos antes de usar en tareas importantes.

---

## 📚 Más Información

- **README.md**: Documentación completa del proyecto
- **TECHNICAL_GUIDE.md**: Guía técnica y personalización avanzada
- **hand_controller.py**: Código fuente principal

---

## 🎉 ¡Disfruta controlando tu PC con gestos!

Si tienes problemas, revisa la sección de solución de problemas o consulta la documentación técnica.
