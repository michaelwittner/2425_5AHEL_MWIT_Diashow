from pydub import AudioSegment
import ffmpeg

class AudioEngine:
    def __init__(self):
        pass

    def cut_audio(self, file_name, result_length, cut_direction):
        # Öffnen der MP3-Datei
        song = AudioSegment.from_mp3(file_name)

        # Umrechnung der gewünschten Länge in Millisekunden
        result_length_ms = result_length * 1000

        # Prüfen der Cut-Richtung
        if cut_direction == "CUT-LEFT":
            # Vom Anfang wegschneiden: Die letzten 'result_length' Sekunden behalten
            result_audio = song[-result_length_ms:]
        elif cut_direction == "CUT-RIGHT":
            # Vom Ende wegschneiden: Die ersten 'result_length' Sekunden behalten
            result_audio = song[:result_length_ms]
        else:
            raise ValueError("Bitte 'CUT-LEFT' oder 'CUT-RIGHT' angeben.")

        # Speichern der neuen Datei
        result_audio.export(f"cut_{cut_direction}_{result_length}_seconds.mp3", format="mp3")
        print(f"Neue Datei '{f'cut_{cut_direction}_{result_length}_seconds.mp3'}' wurde erstellt und gespeichert.")

    def crossfade(self, file1, file2, duration):
        song1 = AudioSegment.from_mp3(file1)
        song2 = AudioSegment.from_mp3(file2)
        return song1.append(song2, crossfade=duration)

    def fade_in(self, file_name, duration):
        song = AudioSegment.from_mp3(file_name)
        return song.fade_in(duration)

    def fade_out(self, file_name, duration):
        song = AudioSegment.from_mp3(file_name)
        return song.fade_out(duration)


    def add_audio_to_video(self, video_name, audio_name, output_name):
        video_input = video_name
        audio_input = audio_name
        output_video = output_name

        video = ffmpeg.input(video_input).video
        audio = ffmpeg.input(audio_input).audio
        ffmpeg.output(audio, video, output_video, vcodec='copy', acodec='copy').run()
