from PIL import Image
import io
import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def generate_image(input: str):
    """Create an image based on input"""
    image_bytes = query({
        "inputs": input,
    })
    # You can access the image with PIL.Image for example

    image = Image.open(io.BytesIO(image_bytes))
    name = input.split(" ")[0]
    image.save(f"outputs/generate_{name}.jpg")
    return image