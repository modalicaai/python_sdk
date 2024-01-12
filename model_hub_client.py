import requests

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
        
        if not self.chat_history[0]["content"] or not instructions: 
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
