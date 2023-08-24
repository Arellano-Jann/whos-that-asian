# whos-that-asian

npm create svelte@latest whos-that-asian
cd whos-that-asian
npm install
npm run dev

# For raw facial recognition

pip install dlib
pip install opencv-python
pip install face_recognition
cd ml
python faceRecognition.py

# Explanation of faceRecognition.py

The main function will use cv2 and face_recognition to look at the given image and compare them to the database of images to see if there are any matches. It will then surround the face with a box and label it, then output a file of the labelled face to the whos-that-asian directory (the parent directory of ml)