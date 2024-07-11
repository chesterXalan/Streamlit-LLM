from typing import cast

from src.service.chain_bot import TranslateChain

chain = TranslateChain()


def test_chat_stream() -> None:
    """
    測試是否能正常翻譯 (使用stream)
    """
    stream = chain.chat("日文", "非常感謝您")
    result = "".join(s for s in stream)

    assert "ありがとうご" in result


def test_chat_not_stream() -> None:
    """
    測試是否能正常翻譯 (不使用stream)
    """
    result = chain.chat("英文", "非常感謝您", stream=False)
    result = cast(str, result)

    assert "thank you" in result.lower()
