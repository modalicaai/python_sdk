import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class MediaProcessorClient:
    """Python SDK for interacting with the Media Processor API."""

    def __init__(self, api_key):
        """Initialize the MediaProcessorClient with the provided API key.

        Args:
            api_key (str): Your API key for the Media Processor API.
        """
        self.api_key = api_key
        self.headers = {
            "X-API-Key": self.api_key
        }
        self.base_url = "https://api.modalica.ai/v1/media_processor"

    def _make_request(self, endpoint, data, headers, is_json=True):
        """Internal method to make an HTTP request to the given endpoint.

        Args:
            endpoint (str): The specific API endpoint.
            data: The data payload for the request.
            headers (dict): Headers for the request.
            is_json (bool): Flag to indicate if the request is JSON type.

        Returns:
            The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        if is_json:
            response = requests.post(url, json=data, headers=headers)
        else:
            response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def chunkify_text(self, file_name, file_content, configs={"max_chunk_size": 1000}):
        """Chunkify a text file.

        Args:
            file_name (str): The name of the file.
            file_content: The content of the file.
            configs (dict, optional): Configuration options for chunkification.

        Returns:
            The chunkified text response.
        """
        multipart_data = MultipartEncoder(
            fields={
                'configs': json.dumps(configs),
                'listOfFiles': (file_name, file_content, 'application/pdf')
            }
        )
        headers = self.headers.copy()
        headers["Content-Type"] = multipart_data.content_type
        return self._make_request("chunkify_text", multipart_data, headers, is_json=False)

    def embed_text(self, file_name, file_content, configs={"max_chunk_size": 1000}):
        """Embed a text file.

        Args:
            file_name (str): The name of the file.
            file_content: The content of the file.
            configs (dict, optional): Configuration options for embedding.

        Returns:
            The embedded text response.
        """
        multipart_data = MultipartEncoder(
            fields={
                'configs': json.dumps(configs),
                'listOfFiles': (file_name, file_content, 'application/pdf')
            }
        )
        headers = self.headers.copy()
        headers["Content-Type"] = multipart_data.content_type
        return self._make_request("embed_text", multipart_data, headers, is_json=False)

    def embed_text_snippets(self, snippets, configs={"embedding_model": "clip-vit-b-32"}):
        """Embed text snippets.

        Args:
            snippets (list of str): The text snippets to embed.
            configs (dict, optional): Configuration options for embedding.

        Returns:
            The embedded snippets response.
        """
        payload = {
            "configs": configs,
            "snippets": snippets
        }
        return self._make_request("embed_text_snippets", payload, self.headers)

    def embed_image(self, file_name, file_content, configs={"embedding_model": "clip-vit-b-32"}):
        """Embed an image file.

        Args:
            file_name (str): The name of the file.
            file_content: The content of the file.
            configs (dict, optional): Configuration options for embedding.

        Returns:
            The embedded image response.
        """
        multipart_data = MultipartEncoder(
            fields={
                'configs': json.dumps(configs),
                'listOfFiles': (file_name, file_content)
            }
        )
        headers = self.headers.copy()
        headers["Content-Type"] = multipart_data.content_type
        return self._make_request("embed_image", multipart_data, headers, is_json=False)
