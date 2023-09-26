import firebase_admin
from firebase_admin import credentials, initialize_app
from firebase_admin.firestore import client

def write_img(image_string: str, id: str):
    """
    Write the image data to Firestore.

    Args:
        image_string (str): The image data as a string.
        id (str): The ID of the document in Firestore.

    Returns:
        None
    """
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate('./serviceAccountKey.json')
    initialize_app(cred)

    # Create a Firestore client
    db = client()

    # Save the image bytes to Firestore
    doc_ref = db.collection('images').document(id)
    doc_ref.set({'image_data': image_string})

def fetch_image(id: str) -> str:
    """
    Fetches the image data for a given image ID from Firestore.

    Args:
        id (str): The ID of the image to fetch.

    Returns:
        str: The image data.
    """

    # Initialize Firebase Admin SDK
    cred = credentials.Certificate('./serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

    # Create a Firestore client
    db = client()

    # Fetch the data from Firestore
    doc_ref = db.collection('images').document(id)
    doc = doc_ref.get()
    image_data = doc.get('image_data')  
    return image_data



