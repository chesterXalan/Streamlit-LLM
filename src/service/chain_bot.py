from collections.abc import Iterator
from typing import cast

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class TranslateChain:
    """
    使用 LangChain 製作翻譯機器人
    """

    def __init__(
        self, *, api_key: str | None = None, model: str = "gpt-3.5-turbo"
    ) -> None:
        """
        OpenAI API 設定
        """
        if api_key:
            self.model = ChatOpenAI(api_key=api_key, model=model)
        else:
            load_dotenv()
            self.model = ChatOpenAI(model=model)

        self.parser = StrOutputParser()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "你是一個翻譯專家, 請將以下的內容翻譯成{lang}"),
                ("human", "{text}"),
            ]
        )

    def chat(self, lang: str, text: str, *, stream: bool = True) -> Iterator[str] | str:
        self.model.streaming = stream
        chain = self.prompt | self.model | self.parser

        if stream:
            return cast(Iterator[str], chain.stream({"lang": lang, "text": text}))
        return cast(str, chain.invoke({"lang": lang, "text": text}))
