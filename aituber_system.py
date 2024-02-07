import random
from obs_adapter import OBSAdapter
from voicevox_adapter import VoicevoxAdapter
from openai_adapter import OpenAIAdapter
from youtube_comment_adapter import YoutubeCommentAdapter
from play_sound import PlaySound
from dotenv import load_dotenv
load_dotenv()
import os

class AITuberSystem:
    def __init__(self) -> None:
        video_id = os.getenv("YOUTUBE_VIDEO_ID")
        self.youtube_comment_adapter = YoutubeCommentAdapter(video_id)
        self.openai_adapter = OpenAIAdapter()
        self.voicevox_adapter = VoicevoxAdapter()
        self.obs_adapter = OBSAdapter()
        self.play_sound = PlaySound(output_device_name="CABLE Input")
        pass

    def talk_with_comment(self) -> bool:
        print("コメントを読み込みます…")
        comment = self.youtube_comment_adapter.get_latest_chat_message()
        if comment is None:
            print("コメントがありませんでした。")
            return False
        
        response_text = self.openai_adapter.create_chat(comment)
        data, rate = self.voicevox_adapter.generate_voice_data_and_sample_rate_from_text(response_text)
        self.obs_adapter.set_question(comment)
        self.obs_adapter.set_answer(response_text)
        self.play_sound.play_sound(data, rate)
        return True