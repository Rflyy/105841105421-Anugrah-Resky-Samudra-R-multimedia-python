import simpleaudio as sa
from pydub import AudioSegment

# Memuat file audio dari format MP3
audio = AudioSegment.from_file('lagu.mp3')

# Memutar audio
wave_obj = sa.WaveObject.from_wave_file('result.wav')
play_obj = wave_obj.play()

# Menunggu sampai audio selesai diputar
play_obj.wait_done()

# Menyimpan file audio dalam format yang sama
audio.export('result.mp3', format='mp3')

clipped_audio = audio[:10000]  # 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')
audio.export('result.wav', format='wav')
louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')