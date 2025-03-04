from pydub import AudioSegment

print("test")

# Öffnen einer MP3-Datei mit pydub.
song = AudioSegment.from_mp3("WhoYouFoolin.mp3")

# pydub arbeitet in millisekunden
ten_seconds = 10 * 1000

# Startet bei 0 kann man aber auch selber definieren start_wert:end_wert
first_10_seconds = song[:ten_seconds]

# save file
first_10_seconds.export("first_10_seconds.mp3", format="mp3")
print("New Audio file is created and saved")
