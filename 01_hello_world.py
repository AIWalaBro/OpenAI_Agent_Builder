from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool

# Load .env file to get API key
load_dotenv()

# Read key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Create async OpenAI client
client = AsyncOpenAI(api_key=openai_api_key)

# ----------- TOOL -----------
@function_tool
def get_weather(city: str) -> str:
    # Dummy logic for example (no external API)
    return f"The weather in {city} is sunny and 30°C."

# ----------- AGENT -----------
agent = Agent(
    name="Weather Assistant",
    instructions="You are a weather assistant. Use tools when needed.",
    model=OpenAIChatCompletionsModel(
        model="gpt-4.1-mini",      # working & quota-friendly model
        openai_client=client,
    ),
    tools=[get_weather],
)

# ----------- QUERY FROM USER -----------
query = "How is the weather in Delhi today?"

# ----------- RUN AGENT -----------
result = Runner.run_sync(
    agent,
    query,
)

# ----------- PRINT FINAL ANSWER -----------
print("Final Output:\n")
print(result.final_output)
