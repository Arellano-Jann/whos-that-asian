import face_recognition
import cv2
import os, sys
import numpy as np
import math
import time
    
class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True
    
    def __init__(self):
        pass
        
    def encode_faces(self):
        encoded = {}
        for image in os.listdir('images'):
            face_image = face_recognition.load_image_file(f'images/{image}')
            face_encoding = face_recognition.face_encodings(face_image)[0]
            
            # self.known_face_encodings.append(face_encoding)
            # self.known_face_names.append(image)
            encoded[image.split(".")[0]] = face_encoding           
            
        return encoded
        
    def unkown_image_encoded(image):
        face = fr.load_image_file()
        
        
        
    def run_recognition(self, image):
        faces = self.encode_faces()
        faces_encoded  = list(faces.values())
        known_face_names = list(faces.keys())
        
        # image_path = image  # Replace with the actual image path
        output_path = "output.jpg"  # Specify the path to save the copied image

        # with open(image_path, "rb") as image_file:
        #     image_data = image_file.read()

        with open(output_path, "wb") as output_file:
            output_file.write(image)
        
        img = cv2.imread(image, 1)
        # small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        # rgb_small_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        face_locations = face_recognition.face_locations(img)
        unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
        
        # print(unknown_face_encodings)
        # print(face_locations)
        
        face_names = []
        for face_encoding in unknown_face_encodings:
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)
            name = 'Unknown'
            
            face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            face_names.append(name)
            
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (0,255,0),2)
                cv2.rectangle(img, (left-20,bottom-15), (right+20, bottom+20), (0,255,0), cv2.FILLED)
                
                cv2.putText(img, name, (left - 20, bottom + 15), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255), 2)
            
        # cv2.imwrite(os.path.join("..", "output.jpg"), img)
            
        # while True:
        #     cv2.imshow('Image', img)
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         return face_names
        return face_names[0]

# def run_model(image):
#     fr = FaceRecognition()
#     return fr.run_recognition(image)
#     # print("in_main_backend")