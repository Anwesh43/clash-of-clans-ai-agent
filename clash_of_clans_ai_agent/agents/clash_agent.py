from pydantic_ai import Agent 
from tools.clash_tools import getAvailableTools 
from prompts.clash_prompt import SYSTEM_PROMPT

agent = Agent(
    model = 'openai:gpt-5.2',
    tools = getAvailableTools(),
    system_prompt = SYSTEM_PROMPT
)

async def analyseClashOfClanData(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')
