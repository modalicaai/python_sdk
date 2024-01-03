import requests
import json

"""
ModelHubClient: A Python SDK for Model Hub API

This SDK provides a seamless and efficient way for developers to interact with the Model Hub API. Model Hub is a versatile platform offering access to a variety of state-of-the-art AI models for text, chat, code, and image generation.

The ModelHubClient class simplifies the process of utilizing these models in your Python applications. Whether you're generating descriptive text, engaging in AI-driven chat, automating code generation, or creating vivid images, this SDK caters to a broad spectrum of AI functionalities.

Getting started is straightforward:
1. Import the ModelHubClient class.
2. Initialize it with your API key.
3. Use the provided methods to interact with different AI models.

Each method in this SDK corresponds to a specific Model Hub API endpoint, encapsulating the complexities of HTTP requests and JSON handling, thus allowing you to focus on building innovative and intelligent applications.

Example usage for each function is provided, demonstrating how to generate text, chat (with and without built-in history), code, and images. 
# -------------------------- EXAMPLES ----------------------------------
# Import the ModelHubClient
from model_hub_client import ModelHubClient

# Initialize the SDK with your API key
api_key = "YOUR_API_KEY"
sdk = ModelHubClient(api_key)

# Example 1: Generating Text
# --------------------------
# Here, we're using the generate_text method to get a description of Barack Obama.
# We specify the prompt and configurations for the language model.
text_prompt = "Who is Barack Obama?"
text_llm_configs = {
    "model_name": "text-bison@001",
    "temperature": 0.2,
    "max_tokens": 256
}
text_response = sdk.generate_text(text_prompt, text_llm_configs)
print("Text Generation Response:", text_response)

# Example 2: Generating Chat With Given History
# --------------------------
# This example demonstrates a single turn in a chat conversation.
# We provide a prompt, along with the message history and chat model configurations.
chat_prompt = "What is the capital of France?"
chat_message_history = [
    {"role": "user", "content": "What is the capital of France?"}
]
chat_model_configs = {
    "model_name": "gpt-3.5-turbo",
    "temperature": 0.9,
    "max_tokens": 256
}
chat_response = sdk.generate_chat_with_given_history(chat_prompt, chat_message_history, chat_model_configs)
print("Chat Response:", chat_response)

# Example 3: Generating Code
# --------------------------
# In this example, we're requesting the SDK to generate a Python for loop.
# The prompt is given along with configurations for the code model.
code_prompt = "Write a for loop in Python"
code_model_configs = {
    "model_name": "code-bison@002",
    "temperature": 0.9,
    "max_tokens": 256
}
code_response = sdk.generate_code(code_prompt, code_model_configs)
print("Code Generation Response:", code_response)

# Example 4: Generating Image
# ---------------------------
# Here, we're requesting the generation of an image based on a description.
# We provide a prompt and configurations for the image generation model.
image_prompt = "A landscape painting of a mountain at sunset"
image_model_configs = {
    "model_name": "imagegeneration@002",
    "size": "1024x768",
    "number_of_images": 1
}
image_response = sdk.generate_image(image_prompt, image_model_configs)
print("Image Generation Response:", image_response)

# Example 5: Generating Chat with Built-In History
# ------------------------------------------------
# This example demonstrates the use of the generate_chat method.
# The SDK maintains the history of the conversation internally. 
# We provide a new prompt and configurations for the chat model.
chat_with_history_prompt = "Tell me a joke"
chat_with_history_response = sdk.generate_chat(chat_with_history_prompt, chat_model_configs)
print("Chat with Built-In History Response:", chat_with_history_response)

# Resetting the Chat History
# --------------------------
# Finally, we reset the chat history when we want to start a new conversation.
sdk.reset_chat_history()

# -------------------- END OF EXAMPLES ----------------------------------


Note: Remember to replace 'YOUR_API_KEY' with your actual API key from Model Hub.
Version: 1.0
Release Date: Dec. 2023
"""

import requests
import json

class ModelHubClient:
    """
    A Python SDK for interacting with the Model Hub API.

    Attributes:
        api_key (str): The API key for authenticating with the Model Hub API.
        chat_history (list): Stores the history of messages for the chat functionality.
        base_url (str): The base URL for the Model Hub API.
    """

    def __init__(self, api_key):
        """
        Initializes the ModelHubClient with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Model Hub API.
        """
        self.api_key = api_key
        self.base_url = "https://api.modalica.ai/v1/model_hub"
        self.headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }
        self.chat_history = [{"role": "system", "content": ""}]

    def generate_text(self, prompt, llm_configs):
        """
        Generates text based on specific prompts or data inputs.
        ...
        """
        end_point = f"{self.base_url}/generate_text"
        prompt_and_config = {
            "prompt": prompt,
            "llm_configs": llm_configs
        }
        response = requests.post(end_point, json=prompt_and_config, headers=self.headers)
        return response

    def generate_chat_with_given_history(self, prompt, message_history, chat_model_configs):
        """
        Responds to user queries in a back-and-forth dialogue scenario.
        ...
        """
        end_point = f"{self.base_url}/generate_chat"
        prompt_and_config = {
            "prompt": prompt,
            "message_history": message_history,
            "chat_model_configs": chat_model_configs
        }
        response = requests.post(end_point, json=prompt_and_config, headers=self.headers)
        return response

    def generate_code(self, prompt, code_model_configs):
        """
        Automates the creation of code snippets.
        ...
        """
        end_point = f"{self.base_url}/generate_code"
        prompt_and_config = {
            "prompt": prompt,
            "code_model_configs": code_model_configs
        }
        response = requests.post(end_point, json=prompt_and_config, headers=self.headers)
        return response

    def generate_image(self, prompt, image_model_configs):
        """
        Generates images from descriptions or data patterns.
        ...
        """
        end_point = f"{self.base_url}/generate_image"
        prompt_and_config = {
            "prompt": prompt,
            "image_model_configs": image_model_configs
        }
        response = requests.post(end_point, json=prompt_and_config, headers=self.headers)
        return response

    def generate_chat(self, prompt, chat_model_configs):
        """
        Responds to user queries in a back-and-forth dialogue scenario using built-in history.
        ...
        """
        instructions = chat_model_configs.get('system', "")
        if instructions:
            self.chat_history[0]["content"] = instructions
        
        if not self.chat_history[0]["content"]: 
            # No instruction is provided at all, remove the first element of the array before sending it.
            chat_history = self.chat_history[1:]
        else: 
            chat_history = self.chat_history
        end_point = f"{self.base_url}/generate_chat"
        prompt_and_config = {
            "prompt": prompt,
            "message_history": chat_history,
            "chat_model_configs": chat_model_configs
        }
        response = requests.post(end_point, json=prompt_and_config, headers=self.headers)
        
        self.chat_history.append({"role": "user", "content": prompt})
        self.chat_history.append({"role": "assistant", "content": response.text})
        
        return response

    def reset_chat_history(self):
        """
        Resets the chat history to an empty list.
        """
        self.chat_history = [{"role": "system", "content": ""}]
