from flask import Flask, request, send_file
from faceRecognition import FaceRecognition
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:5173"}})
faceName = "flask"

# Path for our main Svelte page
@app.route("/")
def base():
    # print("flask_print_base")
    return faceName

# # Path for all the static files (compiled JS/CSS, etc.)
# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory('../svelte', path)


# @app.route("/rand")
# def hello():
#     return str(random.randint(0, 100))

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    faceName = "flask_on_change"
    # print("flask_print_predict")
    face = request.files.get('image')
    # print(request.files)
    # return request
    if face.filename == '':
        return request
    # return send_file(face, mimetype='image/jpeg')
    # return "predict_test"
    fr = FaceRecognition()
    
    # face.save("output.jpg")
    # return fr.run_recognition("output.jpg")

    return fr.run_recognition(face)
    # return fr.run_recognition("test4.jpg")


if __name__ == "__main__":
    app.run(debug=True)