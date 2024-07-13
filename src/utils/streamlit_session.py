from typing import Any, NamedTuple, cast

import streamlit as st

from ..utils.streamlit_msg import Avatar, MessageModel, Role


class SessionState(NamedTuple):
    attr: str
    value: Any


def init_session_state(state: list[SessionState]) -> None:
    """
    初始化工作階段變數
    """
    for s in state:
        if s.attr not in st.session_state:
            setattr(st.session_state, s.attr, s.value)


def render_history(*, attr: str, ignore_role: str | None = None) -> None:
    """
    顯示對話紀錄
    """
    for message in getattr(st.session_state, attr):
        message = cast(MessageModel, message)
        if message.role == ignore_role:
            continue
        with st.chat_message(message.role, avatar=message.avatar):
            st.write(message.content)


def render_human_chat(content: str, *, attr: str) -> None:
    """
    顯示使用者對話
    """
    with st.chat_message(Role.human, avatar=Avatar.human):
        st.write(content)
    save_message(Role.human, Avatar.human, content, attr=attr)


def render_human_chat_custom(
    role: str, avatar: str | None, content: str, *, attr: str
) -> None:
    """
    顯示使用者對話 (自定義名稱與頭貼)
    """
    with st.chat_message(role, avatar=avatar):
        st.write(content)
    save_message(role, avatar, content, attr=attr)


def render_ai_chat(
    content: Any,  # noqa: ANN401
    *,
    attr: str,
    is_stream: bool = True,
) -> None:
    """
    顯示 AI 對話
    """
    with st.chat_message(Role.ai, avatar=Avatar.ai):
        if is_stream:
            response = st.write_stream(content)
            save_message(Role.ai, Avatar.ai, response, attr=attr)
        else:
            st.write(content)
            save_message(Role.ai, Avatar.ai, content, attr=attr)


def render_ai_chat_custom(
    role: str,
    avatar: str | None,
    content: Any,  # noqa: ANN401
    *,
    attr: str,
    is_stream: bool = True,
) -> None:
    """
    顯示 AI 對話 (自定義名稱與頭貼)
    """
    with st.chat_message(role, avatar=avatar):
        if is_stream:
            response = st.write_stream(content)
            save_message(role, avatar, response, attr=attr)
        else:
            st.write(content)
            save_message(role, avatar, content, attr=attr)


def render_system_chat(
    content: Exception | str, *, is_error: bool = True, attr: str | None = None
) -> None:
    """
    顯示系統對話
    """
    with st.chat_message(Role.system, avatar=Avatar.system):
        if is_error:
            st.error(content)
        else:
            st.write(content)
            save_message(Role.system, Avatar.system, content, attr=cast(str, attr))


def save_message(role: str, avatar: str | None, content: Any, *, attr: str) -> None:  # noqa: ANN401
    """
    保存對話紀錄
    """
    getattr(st.session_state, attr).append(
        MessageModel(role=role, avatar=avatar, content=content)
    )
