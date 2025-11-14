from dotenv import load_dotenv
load_dotenv()


from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "give me hello world code in python")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.