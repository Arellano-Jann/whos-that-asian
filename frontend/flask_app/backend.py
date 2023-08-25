from flask import Flask, request
from ml.faceRecognition import main as FaceRecognition
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
faceName = "flask"

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
    faceName = "flask_on_change"
    face = request.files.get('face')
    return "predict_test"
    return FaceRecognition("test.jpg")


if __name__ == "__main__":
    app.run(debug=True)