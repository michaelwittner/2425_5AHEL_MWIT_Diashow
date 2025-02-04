from pydub import AudioSegment
from pydub.playback import play

#opens the file
song = AudioSegment.from_mp3("music.mp3")

#adding 3 seconds fade in and 3 seconds fade out
awesome = song.fade_in(3000).fade_out(3000)

#playing the audio file directly in pycharm
play(awesome)

#exporting the audio file with the changes as mp3.
awesome.export("mashup.mp3", format="mp3")

