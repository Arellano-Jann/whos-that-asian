from flask import Flask, request
from ml.faceRecognition import main as FaceRecognition

app = Flask(__name__)
faceName = "Unknown"

# Path for our main Svelte page
@app.route("/")
def base():
    return faceName

# # Path for all the static files (compiled JS/CSS, etc.)
# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory('../svelte', path)


# @app.route("/rand")
# def hello():
#     return str(random.randint(0, 100))

@app.route("/predict", methods=['POST'])
def predict():
    face = request.files.get('face')
    return FaceRecognition("test.jpg")


if __name__ == "__main__":
    app.run(debug=True)