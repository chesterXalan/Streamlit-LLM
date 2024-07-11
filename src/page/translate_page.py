import streamlit as st

from src.utils.streamlit_session import (
    SessionState,
    init_session_state,
    render_ai_chat,
    render_history,
    render_human_chat,
    render_system_chat,
)

from ..service.chain_bot import TranslateChain
from ..utils.streamlit_msg import Avatar, Role


def page(title: str, bot: TranslateChain) -> None:
    """
    翻譯頁面
    """
    init_session_state([SessionState("translate_messages", [])])

    st.title(title)
    # 語言選單
    lang = st.selectbox("想翻譯成什麼語言?", ["中文", "英文", "日文", "韓文"])
    render_history(attr="translate_messages")

    # 輸入文字
    if prompt := st.chat_input("請輸入想翻譯的文字"):
        render_chat(bot, lang, prompt)


def render_chat(bot: TranslateChain, lang: str, prompt: str) -> None:
    """
    顯示即時對話內容
    """
    render_human_chat(Role.human, Avatar.human, prompt, attr="translate_messages")

    try:
        stream = bot.chat(lang, prompt)
        render_ai_chat(lang, None, stream, attr="translate_messages")

    except Exception as e:
        render_system_chat(e)
