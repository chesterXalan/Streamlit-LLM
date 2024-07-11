from src.service.chat_bot import ChatGPT

chat_bot = ChatGPT()

PASS_LENGTH = 2


def test_chat_stream() -> None:
    """
    測試是否能正常聊天 (使用stream)
    """

    stream = chat_bot.chat([{"role": "user", "content": "哈囉"}])

    result = ""
    for chunk in stream:
        response = chunk.choices[0].delta.content
        if response:
            result += response

    assert len(result) >= PASS_LENGTH


def test_chat_not_stream() -> None:
    """
    測試是否能正常聊天 (不使用 stream)
    """
    response = chat_bot.chat([{"role": "user", "content": "哈囉"}], stream=False)
    result = response.choices[0].message.content

    assert len(result) >= PASS_LENGTH
