import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class KnowledgeHubClient:
    """Python SDK for interacting with the Knowledge Hub API."""

    def __init__(self, api_key):
        """Initialize the KnowledgeHubClient with the provided API key.

        Args:
            api_key (str): Your API key for the Knowledge Hub API.
        """
        self.api_key = api_key
        self.base_url = "https://api.modalica.ai/v1/knowledge_hub"
        self.headers = {
            "X-API-Key": self.api_key
        }

    def create_corpus(self, embedding_model="clip-vit-b-32"):
        """Create a new corpus for media files.

        Args:
            embedding_model (str, optional): The embedding model to use. Defaults to "clip-vit-b-32".

        Returns:
            The response from the API.
        """
        endpoint = f"{self.base_url}/create_corpus"
        multipart_data = MultipartEncoder(
            fields={'configs': f'{{"embedding_model": "{embedding_model}"}}'}
        )
        headers = self.headers.copy()
        headers["Content-Type"] = multipart_data.content_type
        response = requests.post(endpoint, data=multipart_data, headers=headers)
        return response

    def add_media(self, file_name, file_content):
        """Add media files to the corpus.

        Args:
            file_name (str): The name of the file.
            file_content: The content of the file.

        Returns:
            The response from the API.
        """
        endpoint = f"{self.base_url}/add_media"
        multipart_data = MultipartEncoder(
            fields={'listOfFiles': (file_name, file_content)}
        )
        headers = self.headers.copy()
        headers["Content-Type"] = multipart_data.content_type
        response = requests.post(endpoint, data=multipart_data, headers=headers)
        return response

    def query_media(self, query, configs):
        """Execute queries against media in the corpus.

        Args:
            query (str): The search query.
            configs (dict): Query configurations.

        Returns:
            The response from the API.
        """
        endpoint = f"{self.base_url}/query_media"
        headers = self.headers.copy()
        headers["Content-Type"] = "application/json"
        payload = {"query": query, "configs": configs}
        response = requests.post(endpoint, json=payload, headers=headers)
        return response

    def describe_corpus(self):
        """Get statistics and insights about the media files in the corpus.

        Returns:
            The response from the API.
        """
        endpoint = f"{self.base_url}/describe_corpus"
        response = requests.post(endpoint, headers=self.headers)
        return response

    def delete_media(self, file_names):
        """Delete media files from the corpus.

        Args:
            file_names (list of str): The names of the files to delete.

        Returns:
            The response from the API.
        """
        endpoint = f"{self.base_url}/delete_media"
        data = {"listOfFiles": file_names}
        response = requests.post(endpoint, headers=self.headers, data=data)
        return response

    def delete_corpus(self):
        """Delete the entire corpus.

        Returns:
            The response from the API.
        """
        endpoint = f"{self.base_url}/delete_corpus"
        response = requests.post(endpoint, headers=self.headers)
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("URL:", response.url)
        print("Content:", response.text)
        # If you expect a JSON response, you can also add:
        # print("JSON:", response.json())
        print("Elapsed Time:", response.elapsed)
        return response