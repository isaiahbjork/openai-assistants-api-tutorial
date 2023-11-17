# OpenAI Assistants API Tutorial: Build an AI Math Tutor

[YouTube Tutorial](https://youtu.be/yGjweyV4Eeo): Watch the detailed walkthrough of this code and its functionalities.

## Overview
This repository contains the Python code used in my YouTube tutorial for building a personal AI math tutor using the OpenAI Assistant API. The tutorial walks you through the steps to create, run, and interact with an AI assistant capable of solving math problems.

## Getting Started
Before diving into the code, make sure you have the following prerequisites installed:
- Python 3.6 or higher
- `openai` Python package
- `python-dotenv` package for environment variable management

## Installation
1. Clone this repository.
2. Install the required packages:
   ```bash
   pip install openai python-dotenv
   ```

## Setting Up
1. Create a `.env` file in your project root.
2. Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
The script is divided into functions representing each step of setting up and using the OpenAI Assistant:
- `create_assistant()`: Sets up a new assistant with specific instructions and tools.
- `create_thread()`: Initializes an empty thread for the assistant.
- `create_message()`: Sends a message to the thread.
- `run_assistant()`: Runs the assistant to process the message.
- `retrieve_run()`: Retrieves the result of the assistant's processing.
- `get_messages()`: Lists all messages in a thread.

To execute a function, simply uncomment it in the script and run:
```python
python main.py
```

## Additional Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/overview): For more in-depth understanding and additional features.

## Feedback and Contributions
Your feedback is valuable! If you have suggestions or modifications, feel free to create an issue or a pull request. For specific queries related to the tutorial, drop a comment on the YouTube video.