from dotenv import load_dotenv
from openai import OpenAI, Stream
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam


class ChatGPT:
    """
    ChatGPT API
    """

    def __init__(self, *, api_key: str | None = None) -> None:
        """
        OpenAI API 設定
        """
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            load_dotenv()
            self.client = OpenAI()

    def chat(
        self,
        messages: list[ChatCompletionMessageParam],
        *,
        model: str = "gpt-3.5-turbo",
        stream: bool = True,
    ) -> Stream[ChatCompletionChunk] | ChatCompletion:
        """
        開始聊天 (串流傳輸)
        """
        return self.client.chat.completions.create(
            messages=messages,
            model=model,
            stream=stream,
        )
