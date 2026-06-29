# Swahili Slang Bot

A chatbot that teaches and translates Swahili slang. Slang terms and their meanings are stored locally and looked up by an LLM agent (Llama3, run locally) each time a query is made.

## How it works
1. Slang terms and definitions live in `slang.json`.
2. `translator.py` handles lookup/translation logic.
3. `main.py` runs the bot, routing each query through a locally hosted Llama3 model.

## Tech Stack
- Python
- Llama3 (run locally, no external API calls)

## Getting Started

\`\`\`bash
python main.py
\`\`\`

Requires a local Llama3 instance running and accessible to the script.

## Why
Swahili slang shifts fast and isn't well represented in standard translation tools. This project is a step toward a translator that actually keeps up.
