# 🚀 Guía de Ejecución - Hand Gesture PC Controller

## ⚠️ IMPORTANTE: Cómo Ejecutar los Scripts

Hay **DOS formas** de ejecutar los scripts, dependiendo de dónde estés:

---

## 📍 Opción 1: Desde el Explorador de Archivos (RECOMENDADO)

### ✅ Más Fácil y Confiable

Simplemente haz **doble click** en los archivos `.bat`:

- 🔧 `setup.bat` - Instalación inicial
- 🎮 `practice.bat` - Modo de práctica
- 🚀 `start_controller.bat` - Iniciar controlador
- 🧪 `test.bat` - Verificar sistema

**Esto funciona siempre sin problemas.**

---

## 📍 Opción 2: Desde la Terminal

### Si estás en CMD (Command Prompt):

```cmd
practice.bat
```

### Si estás en PowerShell:

Tienes 2 opciones:

**A) Ejecutar el .bat desde CMD:**
```powershell
cmd /c practice.bat
```

**B) Usar los scripts PowerShell (archivos .ps1):**
```powershell
.\practice.ps1
```

---

## 🎯 Todos los Comandos Disponibles

### Desde CMD:
```cmd
setup.bat              # Instalación
test.bat               # Verificar sistema
practice.bat           # Modo de práctica
start_controller.bat   # Iniciar controlador
```

### Desde PowerShell:
```powershell
# Opción 1: Ejecutar .bat desde CMD
cmd /c setup.bat
cmd /c test.bat
cmd /c practice.bat
cmd /c start_controller.bat

# Opción 2: Usar scripts PowerShell
.\test.ps1
.\practice.ps1
.\start_controller.ps1
```

### Desde Explorador de Archivos:
```
Doble click en cualquier archivo .bat
```

---

## ❓ ¿Por Qué Este Problema?

Los archivos `.bat` están diseñados para **CMD (Command Prompt)**, no para PowerShell. Cuando ejecutas un `.bat` directamente en PowerShell, a veces hay problemas de compatibilidad.

**Soluciones:**
1. ✅ **Doble click** en el archivo (siempre funciona)
2. ✅ Ejecutar con `cmd /c nombre.bat` desde PowerShell
3. ✅ Usar los archivos `.ps1` desde PowerShell

---

## 🎮 Inicio Rápido

### Primera Vez:

1. **Doble click en:** `setup.bat`
   - Espera a que termine (1-2 minutos)

2. **Doble click en:** `test.bat`
   - Verifica que todo funcione

3. **Doble click en:** `practice.bat`
   - Practica los gestos sin controlar el mouse

4. **Doble click en:** `start_controller.bat`
   - ¡Empieza a controlar tu PC!

### Uso Regular:

**Doble click en:** `start_controller.bat`

---

## 🔧 Solución al Error que Tuviste

El error que viste:
```
ERROR: Virtual environment not found!
Please run setup.bat first.
```

**Causa:** Ejecutaste `practice.bat` desde PowerShell directamente.

**Solución:**
1. ✅ Haz doble click en `practice.bat` desde el explorador
2. ✅ O ejecuta: `cmd /c practice.bat` en PowerShell
3. ✅ O ejecuta: `.\practice.ps1` en PowerShell

Ahora los scripts están actualizados y deberían funcionar mejor, pero la forma más confiable sigue siendo hacer **doble click** en los archivos `.bat`.

---

## 📝 Resumen de Archivos

### Scripts Batch (para CMD o doble click):
- `setup.bat`
- `test.bat`
- `practice.bat`
- `start_controller.bat`

### Scripts PowerShell (para PowerShell):
- `test.ps1`
- `practice.ps1`
- `start_controller.ps1`

### Código Python:
- `hand_controller.py`
- `demo_practice.py`
- `test_system.py`

---

## ✅ Verificación Rápida

Para verificar que todo está bien instalado:

**Desde Explorador:**
- Doble click en `test.bat`

**Desde PowerShell:**
```powershell
cmd /c test.bat
# o
.\test.ps1
```

Deberías ver:
```
[OK] Camera PASS
[OK] MediaPipe PASS
[OK] PyAutoGUI PASS
```

---

## 🎯 Próximos Pasos

1. ✅ Verifica que el sistema funcione: `test.bat`
2. ✅ Practica los gestos: `practice.bat`
3. ✅ Usa el controlador: `start_controller.bat`

**¡Disfruta controlando tu PC con gestos!** 🎉
