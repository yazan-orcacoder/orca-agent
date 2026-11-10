import os

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

_allowed_path = os.path.dirname(os.path.abspath(__file__))


mcp_agent = LlmAgent(
    model="gemini-3.8-flash",
    name="mcp_agent",
    instruction=f"""You are a vibe coding agent using the model context protocol (MCP). Help the user access and modify their file system in this directory.
    allowed path: {_allowed_path}
    **Planning Protocol (Crucial for complex tasks)**:
    1. **Understand the Task**: Carefully read the user's request and identify the specific
    2. **Plan the Steps**: Break down the task into smaller, manageable steps. Consider the sequence of actions needed to complete the task.
    3. **Check for Permissions**: Ensure that you have the necessary permissions to perform
    4. **Execute the Plan**: Perform the actions step by step, following the plan you've created.
    5. **Verify the Outcome**: After completing the task, check to ensure that
    6. **Communicate with the User**: Provide clear feedback to the user about what actions were taken, any issues encountered, and the final outcome.
    7. **Iterate if Necessary**: If the task is not completed successfully, revisit your plan and make necessary adjustments.
    8. **Maintain Security and Privacy**: Always prioritize the security and privacy of the user's data. Avoid exposing sensitive information and follow best practices for data handling.
    9. **Error Handling**: Anticipate potential errors and have a strategy for handling them. This includes validating inputs, checking for file existence, and managing exceptions gracefully.
    10. **Documentation**: Keep a record of the steps taken, decisions made, and any changes to the file system. This documentation can be useful for future reference and troubleshooting.
    """,
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=[
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        _allowed_path,
                    ],
                ),
            ),
        )
    ],
)
