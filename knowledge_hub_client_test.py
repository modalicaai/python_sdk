import unittest
from knowledge_hub_client import KnowledgeHubClient
import json
import time

class TestKnowledgeHubClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "W0kCXZtS0mxR7WpXcS6qIM7zmdJ8zaKi5CyBL99Eof5y9VoBgkMWVZ2xGovIh6ba"  
        self.sdk = KnowledgeHubClient(self.api_key)
        self.text_file_name = "examples/sample.pdf"  # Update with the path to your test PDF file
        self.image_file_name = "examples/logo.png"  # Update with the path to your test image file

    def test_create_corpus(self):
        # We can delete the corpus and then see if we can
        response = self.sdk.delete_corpus()

        response = self.sdk.create_corpus()
        self.assertEqual(response.status_code, 200)
        # The second call should not override the corpus. We'll give an error saying that the corpus exists.
        response = self.sdk.create_corpus()
        self.assertEqual(response.status_code, 201)
        # We delete the corpus
        response = self.sdk.delete_corpus()
        self.assertEqual(response.status_code, 200)

    def test_core_functions_in_order(self):
        # We can delete the corpus and then see if we can
        response = self.sdk.delete_corpus()
        # We first need to create a corpus
        response = self.sdk.create_corpus()
        self.assertEqual(response.status_code, 200)

        with open(self.text_file_name, "rb") as file:
            file_content = file.read()
        response = self.sdk.add_media(self.text_file_name, file_content)
        self.assertEqual(response.status_code, 200)
        
        with open(self.image_file_name, "rb") as file:
            file_content = file.read()
        response = self.sdk.add_media(self.image_file_name, file_content)
        self.assertEqual(response.status_code, 200)

        response = self.sdk.describe_corpus()
        data_dict = json.loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data_dict['embedding_model'], 'clip-vit-b-32')
        
        # Delay sometime to make sure that the DBs are updated. 
        time.sleep(5)        
        QUERY_TEST = "cat"
        configs = {"top_k": 2, "filters": {"file_type": {"$in": ["PDF", "TXT"]}}}
        response = self.sdk.query_media(QUERY_TEST, configs)
        self.assertEqual(response.status_code, 200)
        data_dict = json.loads(response.text)
        self.assertEqual(len(data_dict), 2)

        response = self.sdk.delete_media([self.text_file_name])
        self.assertEqual(response.status_code, 200)
        
        # We delete the corpus after testing
        response = self.sdk.delete_corpus()

if __name__ == '__main__':
    unittest.main()
