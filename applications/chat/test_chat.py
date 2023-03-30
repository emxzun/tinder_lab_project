import asyncio
from channels.testing import WebsocketCommunicator
from applications.chat.consumers import ChatConsumer
import unittest

class Test_chat(unittest.TestCase):

    async def test_chat(self):
        communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "/ws/hobby/")
        connected, _ = await communicator.connect()
        message = {'message': 'Hello, world!', 'username': 'admin', 'room': 'hobby'}
        await communicator.send_json_to(message)
        try:
            response = await asyncio.wait_for(communicator.receive_json_from(), timeout=60)
            print(response)
        except asyncio.TimeoutError:
            print("Timed out waiting for response")
        await communicator.disconnect()
