from enum import Enum

LLAMA_STACK_URL: str = "http://139.5.188.61:5001"
MODEL: str = "Llama3.3-70B-Instruct"


class ToolTypes(Enum):
    AGENT_TRANSFER = "agent_transfer"
    EXTERNAL_API_CALL = "external_api_call"
