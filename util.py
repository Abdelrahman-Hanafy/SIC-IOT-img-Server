from PIL import Image
from io import BytesIO
import base64

def decode_image(image_data: str):
    """
    Decode base64 image data and display the image.
    
    Args:
        image_data (str): The base64 encoded image data.
    """
    # Decode the base64 image data
    new_bytes = base64.b64decode(image_data)
    
    # Read the bytes back into an image
    new_photo = Image.open(BytesIO(new_bytes))
    
    # Display the image
    new_photo.show()

def encode_img(path: str) -> str:
    """
    Encode an image file to base64 string.
    
    Args:
        path (str): The path to the image file.
        
    Returns:
        str: The base64 encoded string representation of the image.
    """
    # Open the image file
    image = Image.open(path)

    # Convert the image to bytes
    stream = BytesIO()
    image.save(stream, format='JPEG')
    photo_bytes = stream.getvalue()

    # Convert the photo bytes to a base64 string
    image_string = base64.b64encode(photo_bytes).decode('utf-8')

    return image_string
