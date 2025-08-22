def get_llm_response(prompt: str) -> str:
    """
    Sends the prompt to a locally running Qwen2 model using Ollama.
    Args:
        prompt: The complete prompt to be sent to the LLM.
    Returns:
        The text response from the LLM.
    """
    try:
        # Send the prompt to the specified model
        response = ollama.chat(
            model=GENERATOR_MODEL_ID,
            messages=[{'role': 'user', 'content': prompt}]
        )
        # Extract and return the content from the response
        return response['message']['content']
    except Exception as e:
        print(f"\nAn error occurred while calling the LLM via Ollama: {e}")
        return "Error: Could not get a response from the language model. Is Ollama running?"
