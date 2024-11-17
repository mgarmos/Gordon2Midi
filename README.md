
# Generador de Ritmos MIDI

Este proyecto es una herramienta en Python para generar archivos MIDI basados en frases rítmicas (según el mémodo MLT de Gordon) que incluyen silencios y ritmos binarios o ternarios. Cada frase se compone de sílabas, donde cada sílaba representa un patrón rítmico único con duraciones definidas.

## Funcionalidades
- Generación de frases musicales con ritmos binarios (DUPLE) y ternarios (TRIPLE).
- Soporte para silencios representados con duraciones negativas.
- Creación de archivos MIDI que reflejan los patrones rítmicos generados.
- Configuración dinámica del compás (4/4 o 3/4).
- Modo de ejecución desde la línea de comandos con parámetros personalizados.

## Archivos principales
- **phrase.py**: Define la clase `Phrase` para representar frases musicales y controlar su generación.
- **syllables.py**: Contiene las definiciones de las sílabas y sus patrones rítmicos, incluyendo silencios.
- **word.py**: Genera palabras que son combinaciones de sílabas.
- **song.py**: Genera los archivos MIDI basados en las frases musicales.

## Requisitos
- Python 3.6 o superior.
- Bibliotecas necesarias:
  - `midiutil`: Para la generación de archivos MIDI.

### Instalación de dependencias
```bash
pip install midiutil
```

## Ejecución
### Desde la línea de comandos
El script `song.py` acepta los siguientes parámetros:
- `meter`: Define el tipo de ritmo, puede ser `DUPLE` o `TRIPLE`.
- `--length`: (Opcional) Número de palabras en la frase. Por defecto es 4.

#### Ejemplo
```bash
python3 song.py TRIPLE --length 6
```

### Generar ejecutable
Para crear un ejecutable que no requiera dependencias adicionales:
1. Instalar PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Crear el ejecutable:
   ```bash
   pyinstaller --onefile song.py
   ```

## Ejemplo
En un ritmo triple, una frase podría incluir patrones como:
- **Sílaba B1**: Representada como `DU` con un ritmo `[3]`, llenando un compás completo.
- **Sílaba B7**: `DU DA - SILENCE` con un ritmo `[1, 1, -1]`.

El archivo MIDI generado reflejará estos patrones con precisión.

