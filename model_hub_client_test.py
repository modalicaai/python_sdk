import unittest
from model_hub_client import ModelHubClient

class TestModelHubClient(unittest.TestCase):
    def setUp(self):
        # Initialize the SDK with your API key
        self.api_key = "W0kCXZtS0mxR7WpXcS6qIM7zmdJ8zaKi5CyBL99Eof5y9VoBgkMWVZ2xGovIh6ba"
        self.sdk = ModelHubClient(self.api_key)

    def test_generate_text(self):
        # Test generating text
        text_prompt = "Who is Barack Obama?"
        text_llm_configs = {
            "model_name": "text-bison@001",
            "temperature": 0.05,
            "max_tokens": 256
        }
        text_response = self.sdk.generate_text(text_prompt, text_llm_configs)
        print(text_response)
        self.assertIsNotNone(text_response)
        # Add more assertions here as necessary

    def test_generate_chat_with_given_history(self):
        # Test generating chat with given history
        chat_prompt = "What is the closest city to the previous one? Give me only one-word response."
        chat_message_history = [
            {"role": "user", "content": "What is the capital of France?"}
        ]
        chat_model_configs = {
            "model_name": "gpt-3.5-turbo",
            "temperature": 0.05,
            "max_tokens": 256
        }
        chat_response = self.sdk.generate_chat_with_given_history(chat_prompt, chat_message_history, chat_model_configs)
        print(chat_response)
        self.assertIsNotNone(chat_response)
        # Add more assertions here as necessary

    def test_generate_code(self):
        # Test generating code
        code_prompt = "Write a for loop in Python"
        code_model_configs = {
            "model_name": "code-bison@002",
            "temperature": 0.05,
            "max_tokens": 256
        }
        code_response = self.sdk.generate_code(code_prompt, code_model_configs)
        print(code_response)
        self.assertIsNotNone(code_response)
        # Add more assertions here as necessary

    def test_generate_image(self):
        # Test generating an image
        image_prompt = "A landscape painting of a mountain at sunset"
        image_model_configs = {
            "model_name": "imagegeneration@002",
            "size": "1024x768",
            "number_of_images": 1
        }
        image_response = self.sdk.generate_image(image_prompt, image_model_configs)
        self.assertIsNotNone(image_response)
        # Add more assertions here as necessary

    def test_generate_chat(self):
        # Test generating chat with built-in history
        chat_prompt_1 = "Who's obama?"
        chat_prompt_2 = "Who is his wife?"
        chat_model_configs = {
            "model_name": "gpt-3.5-turbo",
            "temperature": 0.05,
            "max_tokens": 256,
            "system": "Response must be shorter than 5 words."
        }
        chat_with_history_response_1 = self.sdk.generate_chat(chat_prompt_1, chat_model_configs)
        chat_with_history_response_2 = self.sdk.generate_chat(chat_prompt_2, chat_model_configs)
        print(chat_with_history_response_1)
        print(chat_with_history_response_2)
        self.assertIsNotNone(chat_with_history_response_1)
        self.assertIsNotNone(chat_with_history_response_2)
        # Add more assertions here as necessary

if __name__ == '__main__':
    unittest.main()
