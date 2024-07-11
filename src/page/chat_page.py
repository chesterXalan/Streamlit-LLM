import streamlit as st

from ..service.chat_bot import ChatGPT
from ..utils.streamlit_msg import Avatar
from ..utils.streamlit_session import (
    SessionState,
    init_session_state,
    render_ai_chat,
    render_history,
    render_human_chat,
    render_system_chat,
)


def page(title: str, bot: ChatGPT) -> None:
    """
    聊天頁面
    """
    init_session_state([SessionState("chat_messages", [])])

    st.title(title)
    render_history(attr="chat_messages")

    # 使用者輸入
    if prompt := st.chat_input("請輸入文字"):
        render_chat(bot, prompt)


def render_chat(bot: ChatGPT, prompt: str) -> None:
    """
    顯示即時對話內容
    """
    render_human_chat("user", Avatar.human, prompt, attr="chat_messages")

    try:
        # 將聊天紀錄傳給 ChatGPT
        stream = bot.chat(st.session_state.chat_messages)
        render_ai_chat("assistant", Avatar.ai, stream, attr="chat_messages")

    except Exception as e:
        render_system_chat(e)
