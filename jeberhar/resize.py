from moviepy.editor as mp
from moviepy.video.fx import Resize

def convert_video(input_file: str, width: int = None, height: int = None, aspect_ratio: str = "16:9"):

    try:
        clip = VideoFileClip(input_file)

        # Seitenverhältnis in numerische Werte umwandeln
        aspect_w, aspect_h = map(int, aspect_ratio.split(":"))

        # Fehlende Dimension berechnen
        if width and not height:
            height = int(width * aspect_h / aspect_w)
        elif height and not width:
            width = int(height * aspect_w / aspect_h)
        elif not width or not height:
            raise ValueError("Entweder Breite oder Höhe muss angegeben werden.")

        # Video skalieren
        resized_clip = clip.fx(resize.resize, newsize=(width, height))

        # Ausgabe-Dateinamen erstellen
        output_file = f"converted_{input_file.split('.')[0]}.mp4"

        # Video speichern
        resized_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

        print(f"Video erfolgreich konvertiert: {output_file}")
    except Exception as e:
        print(f"Fehler bei der Konvertierung: {e}")

# Beispielaufruf:
# convert_video("input.mp4", width=1280, aspect_ratio="16:9")
convert_video("drift.mp4", height=720, aspect_ratio="4:3")
