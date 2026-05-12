from agno.agent import Agent 

from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq


def build_agent():
    return Agent(
        model=OpenAIResponses(id="gpt-5-mini"),
        markdown=True,

    )