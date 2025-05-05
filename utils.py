import base64
from PIL import Image
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def edit_image_with_prompt(image_path: str, prompt: str, output_path: str):
    # Get image size
    with Image.open(image_path) as img:
        width, height = img.size
        size_str = f"{width}x{height}"

    with open(image_path, "rb") as image_file:
        result = client.images.edit(
            model="gpt-image-1",
            image=image_file,
            prompt=prompt,
            quality="low",
        )

    # Decode and save image
    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open(output_path, "wb") as f:
        f.write(image_bytes)
