import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig

# Load environment variables
load_dotenv()

# Get Gemini key from .env
gemini_key = os.getenv("GEMINI_API_KEY")

# Error if key not found
if not gemini_key:
    raise ValueError("Gemini API key not found in environment variables.")

# Set up the external client
external_client = AsyncOpenAI(
    api_key=gemini_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Choose model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Config for the run
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

# Define the agent
agent = Agent(
    name="PC Agent",
    instructions=(
        "You are 'SpecSmith', an expert AI in PC building. Guide users on choosing parts for any budget or use case. "
        "Know about CPUs (AM4/5, LGA 1700), chipsets, GPUs, RAM (DDR4/5), PSU wattage & grades, storage (NVMe/SATA), "
        "coolers, RGB cases, motherboards, and peripherals. Recommend optimized builds, explain terms simply, avoid "
        "outdated hardware unless asked, and prioritize compatibility, performance, and future-proofing."
    ),
)

# Run the agent
result = Runner.run_sync(
    agent,
    input="Hey PC Agent, I am Rahim Ali. I want to build a PC for gaming. Can you help me with a Ryzen build?",
    run_config=config
)

print(result.final_output)
