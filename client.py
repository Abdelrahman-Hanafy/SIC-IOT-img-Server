import requests
from urllib.parse import urljoin
from util import decode_image, encode_img

URL = "http://localhost:5000/"

def fetch_image(id: str):
    end_point = f"/img/{id}"
    response = requests.get(urljoin(URL,end_point))
    data = response.json()
    img = data["image"]
    decode_image(img)

def post_image(path: str):
    img = encode_img(path)
    end_point = "/img"
    data = {
        "id": "samlogo",
        "image": img
    }
    response = requests.post(urljoin(URL,end_point),json=data)
    if response.text == "OK":
        print("Added Successfully!")

if __name__ == "__main__":
    ...