# AI Agents

This project implements an AI-powered research assistant using LangChain and Anthropic's Claude model. The assistant can answer queries, perform web searches, retrieve information from Wikipedia, and save results to a file.

## Features

- **Query Answering**: Uses AI models to answer user queries.
- **Tool Integration**:
  - Wikipedia search
  - DuckDuckGo search
  - Save results to a file
- **Structured Output**: Generates structured responses with titles, summaries, references, and tools used.
- **Extensible**: Easily add more tools or customize the assistant's behavior.

## Requirements

- Python 3.8 or higher
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Agent.git
   cd AI-Agent

2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Create a .env file to store your API keys
touch .env

Add API keys to your .env file
    OPENAI_API_KEY=your_openai_api_key
    ANTHROPIC_API_KEY=your_anthropic_api_key

## Usage
1. Run the script:
python main.py

2. Enter your query when prompted: "What can I help you with today?"

3. The assistant will process your query, use the necessary tools, and provide a structured response.

## Tools 
Wikipedia Tool: Retrieves information from Wikipedia.
DuckDuckGo Search Tool: Performs web searches.
Save Tool: Saves the generated summary or data to a file.

## File Structure
AI-Agent/
├── main.py               # Main script
├── tools.py              # Custom tools for the assistant
├── requirements.txt      # Python dependencies
├── .env                  # API keys (not included in the repository)
├── README.md             # Project documentation
└── venv/                 # Virtual environment (excluded via .gitignore)

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
LangChain for the framework.
Anthropic for the Claude model.
OpenAI for GPT-based models.






