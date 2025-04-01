from moviepy.editor import VideoFileClip,concatenate_videoclips


def merge_videos(video_paths, output_path="output.mp4"):
    try:
        clips = [VideoFileClip(video) for video in video_paths]
        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile(output_path, codec="libx264", fps=30)
        print(f"Video erfolgreich gespeichert als: {output_path}")
    except Exception as e:
        print(f"Fehler beim Zusammenfügen der Videos: {e}")

def extract_audio(video_path, output_audio_path="output_audio.mp3"):
    try:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(output_audio_path)
        print(f"Audiospur gespeichert als: {output_audio_path}")
    except Exception as e:
        print(f"Fehler beim Extrahieren  der Audiospur: {e}")

def convert_video(input_file: str, width: int = None, height: int = None, aspect_ratio: str = "16:9"):

    try:
        clip = VideoFileClip(input_file)

        # Umwandlung des Seitenverhältnisses in numerische Werte
        aspect_w, aspect_h = map(int, aspect_ratio.split(":"))

        # Berechnung der fehlenden Dimension
        if width and not height:
            height = int(width * aspect_h / aspect_w)
        elif height and not width:
            width = int(height * aspect_w / aspect_h)
        elif not width or not height:
            raise ValueError("Entweder Breite oder Höhe muss angegeben werden.")

        resized_clip = clip.resize(newsize=(width, height))

        output_file = f"converted_{input_file.split('.')[0]}.mp4"

        resized_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

        print(f"Video erfolgreich konvertiert: {output_file}")
    except Exception as e:
        print(f"Fehler bei der Konvertierung: {e}")



#convert_video("drift.mp4", height=720, aspect_ratio="4:3")
video_list = ["video1.mp4", "video2.mp4", "video3.mp4"]
#merge_videos(video_list, "final_video.mp4")
extract_audio("drift2.mp4","driftaudio.mp3")