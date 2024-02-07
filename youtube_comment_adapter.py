import pytchat
import json

class YoutubeCommentAdapter:
    def __init__(self, video_id) -> None:
        try:
            self.chat = pytchat.create(video_id=video_id, interruptable=False)
        except Exception as e:
            print("YoutubeCommentAdapterのインスタンス作成でエラーが発生しました: ", e)
            self.chat = None
        pass

    def get_latest_chat_message(self):
        # チャットを一括で取得
        chat_data = self.__get_chat_data()
        if (chat_data == None):
            return None
        latest_chat_data = chat_data[-1] # 最新のチャットのデータ
        # チャット情報の中からチャットのみを取得
        latest_chat_message = latest_chat_data.get("message")
        return latest_chat_message
    
    def __get_chat_data(self):
        if (self.chat.is_alive() == False):
            print("配信が開始していません")
            return None
        
        chat_data = json.loads(self.chat.get().json())
        if (chat_data == []):
            print("チャットデータが取得できませんでした")
            return None
        
        return chat_data
    
if __name__ == "__main__":
    import time
    video_id = "<youtubeのvideo_id>"
    chat = YoutubeCommentAdapter(video_id)
    time.sleep(2) # コメント取得のために少し待つ
    print(chat.get_latest_chat_message())