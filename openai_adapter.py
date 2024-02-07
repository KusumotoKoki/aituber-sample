import openai
import dotenv
import os

# APIキーの設定
dotenv.load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

class OpenAIAdapter:
    """
    OpenAIのAPIを使用してチャットを生成するクラス
    """

    SAVE_PREVIOUS_CHAT_NUM = 5
    OPENAI_MODEL = "gpt-3.5-turbo"
    
    def __init__(self):
        # system_promptはsystem_prompt.txtから読み込む
        with open("system_prompt.txt","r",encoding="utf-8") as f:
            self.system_prompt = f.read()
        self.chat_log = []
        pass

    def create_chat(self, question):
        system_message = self._create_message("system", self.system_prompt)
        past_messages = self._get_past_messages()
        user_message = self._create_message("user", question)
        messages = [system_message] + past_messages + [user_message]

        response = openai.ChatCompletion.create(
            model=self.OPENAI_MODEL,
            messages=messages,
        )
        answer = response["choices"][0]["message"]["content"]
        self._update_chat_log(question, answer)

        return answer
    
    def _create_message(self, role, content):
        return {
            "role":role,
            "content":content
        }
    
    def _get_past_messages(self):
        messages = []
        for chat in self.chat_log:
            messages.append(self._create_message("user", chat["question"]))
            messages.append(self._create_message("assistant", chat["answer"]))
        return messages
    
    def _update_chat_log(self, question, answer):
        # チャットログを保存する
        self.chat_log.append({
            "question":question,
            "answer":answer
        })
        # チャットログがSAVE_PREVIOUS_CHAT_NUMを超えたら古いログを削除する
        if len(self.chat_log)>self.SAVE_PREVIOUS_CHAT_NUM:
            self.chat_log.pop(0)
        return True

    

if __name__ == "__main__":
    adapter = OpenAIAdapter()
    while True:
        question = input("質問を入力してください:")
        response_text = adapter.create_chat(question)
        print(response_text)
        print(adapter.chat_log)