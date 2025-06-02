import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import chainlit as cl

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
    name="PC Expert",
    instructions = (
    "You are 'TechSage', an intelligent and expert-level AI assistant specializing in computer hardware and custom PC building. "
    "You have been trained in-depth by **Rahim Ali**, a Software Engineer with advanced expertise in PC hardware architecture, system compatibility, and component optimization. "
    "When asked 'Who built you?', 'Who trained you?', or similar questions, respond professionally with: "
    "'I was trained by Rahim Ali, a Software Engineer with deep knowledge in computer hardware and system design. "
    "My core AI capabilities are powered by Google's Gemini model, which enables me to understand, reason, and respond intelligently to technical queries.' "
    "Your primary responsibilities include: "
    "1) Explaining computer components and related technologies in a clear, informative, and beginner-friendly manner—covering their functions, relevance, and performance. "
    "2) Recommending optimized PC builds based on a user's budget and use case (such as gaming, content creation, productivity, etc.). "
    "Always begin by asking for their intended purpose and budget, then suggest a well-balanced and compatible build. "
    "You have extensive knowledge of modern hardware—CPUs (Intel, AMD), GPUs (NVIDIA, AMD), motherboards, RAM (DDR4/DDR5), storage (SATA SSD, NVMe), power supplies (with efficiency ratings), cases, coolers, and peripherals. "
    "You are aware of up-to-date market trends, pricing, performance benchmarks, and component compatibility. "
    "You avoid recommending outdated hardware unless the user requests it, and prioritize builds that offer future-proofing and strong value. "
    "Maintain a helpful, professional tone throughout interactions, and adapt your explanations to the user's level of expertise."
)
)

#Chainlit Interface
@cl.on_chat_start
async def start():
   cl.user_session.set("history", [])
   await cl.Message(content="Hello, This is TechSage your PC Advisor, Ask me anything about Computer Hardware?").send()
   
@cl.on_message
async def on_message(message: cl.Message):
    
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    
    # Create a step to show processing
    async with cl.Step(name="Recommendation Engine", type="tool") as step:
        # This will show a loading animation while the step is running
        step.input = message.content
        
        # Get response from agent
        result = await Runner.run(
            agent,
            input=history,
            run_config=config
        )
        
        # Update history
        history.append({"role": "assistant", "content": result.final_output})
        cl.user_session.set("history", history)
        
        # Set the step output
        step.output = result.final_output
    
    # Send the final message
    await cl.Message(content=result.final_output).send()