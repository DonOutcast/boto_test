import pytest

from boto_test

@pytest.mark.asyncio
async def test_message_handler():
    requester = MockedBot(MessageHandler(message_handler))
    calls = await requester.query(MESSAGE.as_object(text="Hello!"))
    answer_message = calls.send_message.fetchone().text
    assert answer_message == "Hello!"
