title = "How to connect Jan.ai to Ollama(non-.cpp)"
date = 2025-03-19T18:23:00+02:00
tags = [
  "llm",
  "keywords",
  "humans",
  "context",
  "window",
  "parameters",
  "deepseek",
  "openai",
  "llama",
  "model",
  "jan",
  "ollama",
]
published = true
+++++

Running LLMs locally is great for privacy and olline access. 

My current setup is to use Jan.ai and Ollama. However, instructions on this setup seem to elude others, so I figure I'd share how I did it.

Since Jan.AI works with OpenAI compatible APIs. You can hook them up by creating a new Engine. 

1) Open Jan
2) Click the settings icon in the lower left corner.
3) Under "General" select the "Engines" tab. 
4) Select "Install Engine" and fill out the following details, leaving any extra fields blank.
Engine Name: Ollama
Chat Completions URL: http://localhost:11434/v1/chat/completions
Model List URL: http://localhost:11434/v1/models
API Key: ollama
5) Click "Install"


Now when you create a new thread, you should be able to select "Ollama" from the cloud tab, and then select the pre-downloaded model from the list. 

Enjoy!