# AI Assistant using Python and Streamlit

This is a simple AI Assistant application built with Python and Streamlit, leveraging the Groq API for natural language processing.

## Features

- User-friendly web interface powered by Streamlit
- Integration with Groq's language model API
- Ability to submit prompts and receive AI-generated responses

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-assistant-python.git
   cd ai-assistant-python
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run bot.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter your prompt in the text input field and click "Submit" to receive a response from the AI assistant.

## Configuration

The application currently uses the "llama3-8b-8192" model. You can modify the `model` parameter in the `bot.py` file to use a different model if desired.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
