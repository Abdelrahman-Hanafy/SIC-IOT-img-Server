# Image Encoding and Decoding

This project provides functions for encoding and decoding images in base64 format.

## Installation

To use this project, you need to have Python installed. You also need to install the required dependencies by running the following command:

`pip install -r requirements.txt`

## Usage

### Encoding an Image

To encode an image file to a base64 string, use the `encode_img` function in `util.py`. The function takes the path to the image file as an argument and returns the base64 encoded string.

Example usage:

```python
from util import encode_img

image_path = "path/to/image.jpg"
encoded_image = encode_img(image_path)
print(encoded_image)
```

### Decoding an Image

To decode a base64 encoded image string and display the image, use the `decode_image` function in `util.py`. The function takes the base64 encoded image data as an argument.

Example usage:

```python
from util import decode_image

image_data = "base64_encoded_image_data"
decode_image(image_data)
```

### Server

The server implementation allows you to upload images to a Firestore database. To start the server, run the following command:

`python server.py`

The server will be running on `http://localhost:5000`. You can use the provided client implementation to upload images to the server.

#### Endpoints

- POST /img: Uploads an image to the Firestore database. Expects a JSON object in the request with the image data as string and image id.

```JSON
{
    "id" : "image_id",
    "image" : "image_data"
}
```

- GET /img/`id`: Retrieves a image_data of this id from the Firestore database.

#### Firestore Integration

To use Firestore as the database for storing the uploaded images, you need to set up a Firestore project and obtain the necessary credentials. Once you have the credentials, replace the placeholder values in the `serviceAccountKey.json` file with your own credentials.

### Client

The client implementation allows you to upload images to the server and retrieve them from the Firestore database. To start the client, run the following command:

`python client.py`

The client will prompt you to enter the path to the image file that you want to upload. After uploading the image, you can use the client to retrieve the uploaded images from the Firestore database.

## Contributing

Contributions are welcome! If you find any issues or have any suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
