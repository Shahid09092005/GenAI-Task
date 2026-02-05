# AI Operations Assistant

A multi-agent AI system that processes natural-language tasks, plans steps, calls real APIs, and returns structured answers.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your API keys (get from OpenAI, GitHub, OpenWeatherMap).
3. Run: `python main.py "Get weather in New York and find top Python repos"`

## Architecture
- **Planner**: Generates JSON plans using LLM.
- **Executor**: Calls tools (GitHub, Weather APIs).
- **Verifier**: Validates and formats output.

## Example Output
For task "Get weather in New York and find top Python repos":