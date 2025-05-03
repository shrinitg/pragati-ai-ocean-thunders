import json
import uuid

from fastapi import WebSocket

from oceanthundersbe import connection_mapping, user_data
from oceanthundersbe.dto import InputMessage, UserData
from oceanthundersbe.service.llm_service import LLMService

llm_service = LLMService()


class Message:

    def __init__(self):
        print("Message class has been initialized")

    async def handle_message(self, websocket: WebSocket):
        connection_id = str(uuid.uuid4())
        if connection_id not in connection_mapping:
            connection_mapping[connection_id] = websocket
            user_data[connection_id] = UserData()

        try:
            while True:
                data = await websocket.receive_text()
                print(f"Received from {connection_id}: {data}")
                data = InputMessage(**json.loads(data))
                response = await llm_service.handle_and_generate_response(data, connection_id)
                await websocket.send_text(response)

        except Exception as e:
            print(f"Connection {connection_id} closed due to exception: {e}")
            await websocket.close()
            del connection_mapping[connection_id]
        finally:
            await websocket.close()
