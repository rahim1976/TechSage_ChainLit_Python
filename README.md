# TechSage PC Advisor

A conversational AI chatbot that provides expert advice on PC hardware and recommends optimized PC builds based on budget constraints.

## 🚀 Project Overview

TechSage PC Advisor is an AI-powered chatbot application built with Chainlit and Google's Gemini 2.0 Flash model. It serves as a virtual PC hardware expert that can:

- Explain any computer part or technology in detail  
- Recommend optimized PC builds based on budget and use case  
- Provide compatibility information between different components  
- Suggest the best value components for various needs  

## 🌟 Features

- **Interactive Web Interface** – Easy-to-use chat interface built with Chainlit  
- **Context-Aware Conversations** – Maintains conversation history for more natural interactions  
- **Specialized Knowledge** – Comprehensive understanding of PC hardware components  
- **Budget-Based Recommendations** – Suggests optimal builds within price constraints  

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

This will start a local web server. Open the URL displayed in your terminal (typically http://localhost:8000 ) in your web browser to interact with TechSage PC Advisor.

## Usage Examples
You can ask TechSage questions like:

- "What's the difference between DDR4 and DDR5 RAM?"
- "Can you recommend a gaming PC build for $1500?"
- "Explain what an NVMe SSD is and its advantages."
- "What's the best CPU for video editing under $300?"

## Project Structure

- **main.py** : The main application file that sets up the AI agent and Chainlit interface
- **.chainlit/** : Configuration files for the Chainlit interface
- **.env** : Environment variables file (you need to create this)

## Troubleshooting
If you encounter any issues:
- Ensure your .env file is properly set up with the correct API key
- Verify all required packages are installed
- Check that you're running the command from the project root directory
- If you get module import errors, you may need to install additional dependencies

## Acknowledgements
- This project uses Chainlit for the chat interface
- Powered by Google's Gemini 2.0 Flash model