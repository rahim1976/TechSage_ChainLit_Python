# TechSage PC Advisor

A conversational AI chatbot that provides expert advice on PC hardware, software, and system optimization through specialized AI agents.

## 🚀 Project Overview

TechSage PC Advisor is an AI-powered chatbot application built with Chainlit and Google's Gemini 2.0 Flash model. It serves as a virtual PC expert system with multiple specialized agents that can:

- Provide expert hardware recommendations and build advice
- Offer software troubleshooting and operating system guidance
- Explain computer components and technologies in detail
- Recommend optimized PC builds based on budget and use case
- Provide compatibility information between different components
- Suggest the best value components for various needs
- Handle both hardware and software-related queries through specialized agents

## 🌟 Features

- **Multi-Agent System** – Specialized agents for different aspects of PC expertise:
  - Hardware Agent: Expert in PC components, builds, and hardware optimization
  - Software Agent: Specialist in operating systems, software, and troubleshooting
  - Main Advisor: Intelligent router that directs queries to the appropriate specialist

- **Smart Query Routing** – Automatically detects query type and routes to the appropriate specialist agent
- **Interactive Web Interface** – Easy-to-use chat interface built with Chainlit
- **Context-Aware Conversations** – Maintains conversation history for more natural interactions
- **Specialized Knowledge** – Comprehensive understanding of both PC hardware and software
- **Budget-Based Recommendations** – Suggests optimal builds within price constraints
- **Real-time Response Streaming** – Provides immediate feedback with smooth response streaming

## ⚙️ Prerequisites

- Python 3.7 or higher
- A Gemini API key from Google

## 📦 Installation

- Clone this repository:
```bash
git clone https://github.com/rahim1976/Ai_Agent_With_ChainLit.git
```

- Install the required packages:
```bash
uv pip install -r requirements.txt
```

- Create a .env file in the project root directory and add your Gemini API key:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

## Running the Application
To start the application, run:
```bash
chainlit run main.py
```

This will start a local web server. Open the URL displayed in your terminal (typically http://localhost:8000) in your web browser to interact with TechSage PC Advisor.

## Usage Examples
You can ask TechSage questions like:

Hardware-related queries:
- "What's the difference between DDR4 and DDR5 RAM?"
- "Can you recommend a gaming PC build for $1500?"
- "Explain what an NVMe SSD is and its advantages."
- "What's the best CPU for video editing under $300?"

Software-related queries:
- "What's the difference between Windows 10 and Windows 11?"
- "How do I fix a blue screen error?"
- "What's the best antivirus software?"
- "How do I optimize my Windows startup?"

## Project Structure

- **main.py**: The main application file that sets up the AI agents and Chainlit interface
- **.chainlit/**: Configuration files for the Chainlit interface
- **.env**: Environment variables file (you need to create this)

## Agent System Architecture

The system consists of three specialized agents:

1. **Hardware Agent**
   - Expert in PC components and builds
   - Handles hardware recommendations and compatibility
   - Provides detailed component explanations
   - Offers build optimization advice

2. **Software Agent**
   - Specialist in operating systems and software
   - Handles software troubleshooting
   - Provides OS comparison and recommendations
   - Offers software optimization advice

3. **Main Advisor**
   - Intelligent query router
   - Analyzes user queries to determine the appropriate specialist
   - Maintains conversation context
   - Ensures seamless handoff between agents

## Troubleshooting
If you encounter any issues:
- Ensure your .env file is properly set up with the correct API key
- Verify all required packages are installed
- Check that you're running the command from the project root directory
- If you get module import errors, you may need to install additional dependencies

## Recent Updates
- Implemented multi-agent system with specialized hardware and software agents
- Added intelligent query routing based on content analysis
- Improved response streaming and message handling
- Enhanced agent type detection for better query routing
- Added clear agent identification in responses

## Acknowledgements
- This project uses Chainlit for the chat interface
- Powered by Google's Gemini 2.0 Flash model
- Developed by Rahim Ali
