from voicevox_adapter import VoicevoxAdapter 
from play_sound import PlaySound

voicevox_adapter = VoicevoxAdapter()
play_sound = PlaySound(output_device_name="CABLE Input")

text = "こんにちは"
data, rate = voicevox_adapter.generate_voice_data_and_sample_rate_from_text(text)
play_sound.play_sound(data, rate)
