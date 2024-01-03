from PIL import Image
import base64
from io import BytesIO
from IPython.display import display
from google.colab import files

def display_image(encoded_image):
  decoded_content = base64.b64decode(encoded_image)
  image = Image.open(BytesIO(decoded_content))
  display(image)

  
def upload_from_local_files():
    uploaded_files = files.upload()
    if not 1 <= len(uploaded_files) <= 100:
        raise Exception("Please upload between 1 to 100 files.")

    file_details = []
    for file_name, file_content in uploaded_files.items():
        file_details.append((file_name, file_content))

    return file_details