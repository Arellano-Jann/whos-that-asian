from flask import Flask, request
from ml.faceRecognition import main as FaceRecognition

app = Flask(__name__)

# # Path for our main Svelte page
# @app.route("/")
# def base():
#     return send_from_directory('../svelte', 'index.html')

# # Path for all the static files (compiled JS/CSS, etc.)
# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory('../svelte', path)


# @app.route("/rand")
# def hello():
#     return str(random.randint(0, 100))

@app.route("/predict")
def predict():
    face = request.files.get('face')
    return FaceRecognition(face)


if __name__ == "__main__":
    app.run(debug=True)