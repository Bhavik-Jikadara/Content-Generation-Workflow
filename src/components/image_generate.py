from PIL import Image
import io
import os
import requests
from crewai_tools import tool

# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
# headers = {"Authorization": "Bearer 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"}
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.content
# def generate_image(input: str):
#     """Create an image based on input"""
#     image_bytes = query({
#         "inputs": input,
#     })
#     # You can access the image with PIL.Image for example

#     image = Image.open(io.BytesIO(image_bytes))
#     name = input.split(" ")[0]
#     image.save(f"images/generate_{name}.jpg")
#     return image

@tool("Image Generate Tool")
def image_generate(context: str):
    """This is Image generate tool"""
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    hugginface_api_key = os.getenv("HUGGINGFACE_API_KEY")
    headers = {"Authorization": f"Bearer {hugginface_api_key}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    image_bytes = query({
        "inputs": context,
    })
    name = context.split(" ")[0]
    image = Image.open(io.BytesIO(image_bytes)).resize((1024, 1024))
    image.save(f"outputs/images/generate_{name}.jpg")
    return image
