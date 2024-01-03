import unittest
from media_processor_client import MediaProcessorClient
from media_processor_client_test_constants import *

class TestMediaProcessorClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "W0kCXZtS0mxR7WpXcS6qIM7zmdJ8zaKi5CyBL99Eof5y9VoBgkMWVZ2xGovIh6ba"
        self.sdk = MediaProcessorClient(self.api_key)
        self.text_file_name = "examples/sample.pdf"  # Update with the path to your test PDF file
        self.image_file_name = "examples/logo.png"  # Update with the path to your test image file
        self.snippets = ["Sample snippet 1", "Sample snippet 2", "Sample snippet 3"]

    def test_chunkify_text(self):
        with open(self.text_file_name, "rb") as file:
            file_content = file.read()
        response = self.sdk.chunkify_text(self.text_file_name, file_content)
        self.assertEqual(response, SAMPLE_PDF_CHUNKS)

    def test_embed_text(self):
        with open(self.text_file_name, "rb") as file:
            file_content = file.read()
        response = self.sdk.embed_text(self.text_file_name, file_content)
        self.assertEqual(response, CHUNKS_EMBEDDING)

    def test_embed_text_snippets(self):
        response = self.sdk.embed_text_snippets(self.snippets)
        self.assertEqual(response, SNIPPETS_EMBEDDING)
        
    def test_embed_image(self):
        with open(self.image_file_name, "rb") as file:
            image_content = file.read()
        response = self.sdk.embed_image(self.image_file_name, image_content)
        self.assertEqual(response, IMAGE_EMBEDDING)

if __name__ == '__main__':
    unittest.main()
