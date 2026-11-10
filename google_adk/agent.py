from google.adk.agents.llm_agent import Agent
from .tools import read_file, write_file, list_file


root_agent = Agent(
    model='gemini-3.8-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge.' \
    'You can read/write/list files in your root directory',
    tools=[read_file, write_file, list_file]
)
