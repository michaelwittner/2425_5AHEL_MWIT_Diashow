from pydub import AudioSegment
from pydub.playback import play

# Open the files
song1 = AudioSegment.from_file(file="music.wav", format="wav")
song2 = AudioSegment.from_file(file="music2.wav", format="wav")

# crossfade duration
crossfade_duration = 5000

#adding fade in and fade out
song1 = song1.fade_in(3000).fade_out(3000)
song2 = song2.fade_in(3000).fade_out(3000)

# Perform crossfade: the second song fades in while the first song fades out
crossfaded = song1.append(song2, crossfade=crossfade_duration)

# Export the crossfaded audio as a new file
crossfaded.export("crossfade_output.wav", format="wav")
