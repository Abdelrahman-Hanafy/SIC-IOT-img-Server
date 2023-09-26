from flask import Flask, request
from PIL import Image
from firestore import write_img , fetch_image

app = Flask(__name__)

@app.route("/img/<id>", methods=['GET'])
def get_image(id):
    img = fetch_image(id)
    return {"image": img}

@app.route("/img", methods=['POST'])
def post_image():
    write_img(request.json["image"], request.json["id"])
    return "OK"


# run flask app to listen 
if __name__ == "__main__":
    app.run(port=5000, debug=True)