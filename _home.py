from enum import StrEnum

import streamlit as st
from streamlit_option_menu import option_menu

from src.page import chat_page, translate_page
from src.service.chain_bot import TranslateChain
from src.service.chat_bot import ChatGPT

st.set_page_config(layout="wide")


class Options(StrEnum):
    chat = "聊天"
    translate_ = "翻譯"


def main() -> None:
    with st.sidebar:
        menu = option_menu(
            "選單",
            list(Options),
            icons=["chat-dots", "translate"],
        )
        openai_api_key = st.text_input(
            "OpenAI API Key", placeholder="請輸入您的API Key", type="password"
        )

    # 建立介面與AI
    if menu == Options.chat:
        chat_page.page(menu, ChatGPT(api_key=openai_api_key))

    elif menu == Options.translate_:
        translate_page.page(menu, TranslateChain(api_key=openai_api_key))


if __name__ == "__main__":
    main()
