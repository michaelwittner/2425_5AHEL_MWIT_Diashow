# AudioEngine Klasse

Die `AudioEngine`-Klasse bietet verschiedene Funktionen zur Bearbeitung von Audiodateien, einschließlich Schneiden, Überblenden sowie Ein- und Ausblenden.

## Installation der benötigten Bibliothek

Bevor die Klasse verwendet wird, muss die Bibliothek `pydub` installiert sein:

```bash
pip install pydub
```

Zusätzlich wird `ffmpeg` benötigt, um MP3-Dateien zu verarbeiten. Installiere es entsprechend für dein Betriebssystem.
Tutorial: https://www.youtube.com/watch?v=JR36oH35Fgg

## Klasseninitialisierung

Die `AudioEngine`-Klasse kann einfach durch Instanziierung eines Objekts verwendet werden:

```python
from pydub import AudioSegment

# Instanziierung der AudioEngine
engine = AudioEngine()
```

## Funktionen

### `cut_audio(file_name, result_length, cut_direction)`
Schneidet eine MP3-Datei von links oder rechts auf eine bestimmte Länge zu.

- **Parameter:**
  - `file_name` (str): Der Name der MP3-Datei.
  - `result_length` (int): Die gewünschte Länge des Ergebnisses in Sekunden.
  - `cut_direction` (str): "CUT-LEFT" oder "CUT-RIGHT", um den Schnittbereich zu bestimmen.

- **Funktion:**
  Schneidet das Audio entsprechend der angegebenen Richtung und speichert es als neue Datei.

### `crossfade(file1, file2, duration)`
Überblendet zwei MP3-Dateien für einen nahtlosen Übergang.

- **Parameter:**
  - `file1` (str): Die erste MP3-Datei.
  - `file2` (str): Die zweite MP3-Datei.
  - `duration` (int): Dauer der Überblendung in Millisekunden.

- **Funktion:**
  Erstellt eine neue Datei mit einem sanften Übergang zwischen den beiden Audiodateien.

### `fade_in(file_name, duration)`
Fügt einen Einblendeffekt zur MP3-Datei hinzu.

- **Parameter:**
  - `file_name` (str): Die MP3-Datei, die eingeblendet werden soll.
  - `duration` (int): Dauer des Einblendens in Millisekunden.

- **Funktion:**
  Die Lautstärke wird allmählich von 0 auf die volle Lautstärke erhöht.

### `fade_out(file_name, duration)`
Fügt einen Ausblendeffekt zur MP3-Datei hinzu.

- **Parameter:**
  - `file_name` (str): Die MP3-Datei, die ausgeblendet werden soll.
  - `duration` (int): Dauer des Ausblendens in Millisekunden.

- **Funktion:**
  Die Lautstärke wird allmählich von der aktuellen Lautstärke auf 0 reduziert.

