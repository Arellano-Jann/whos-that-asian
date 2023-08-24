import face_recognition
import cv2
import os, sys
import numpy as np
import math
import time

def face_confidence(face_distance, face_match_threshold=0.6):
    range = 1.0 - face_match_threshold
    linear_val = (1.0-face_distance)/(range*2.0)
    
    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val-.5) *2, .2)))*100
        return str(round(value,2)) + '%'
    
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
        
        img = cv2.imread(image, 1)
        # small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        # rgb_small_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        face_locations = face_recognition.face_locations(img)
        unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
        
        print(unknown_face_encodings)
        print(face_locations)
        
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
            
        cv2.imwrite(os.path.join("..", "output.jpg"), img)
            
        while True:
            cv2.imshow('Image', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return face_names
            
        
        
        
    # def run_recognition(self):
    #     cap = cv2.VideoCapture(0)
        
    #     if not cap.isOpened():
    #         sys.exit("Video source not found")
        
    #     time.sleep(5)
    #     while True:
    #         ret, frame = cap.read()
    #         if not ret:
    #                 print("empty frame")
    #                 break
    #         if self.process_current_frame:
    #             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    #             rgb_small_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #             self.face_locations = face_recognition.face_locations(rgb_small_frame)
    #             self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
                
    #             print(self.face_locations)
                
    #             self.face_names = []
    #             for face_encoding in self.face_encodings:
    #                 matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
    #                 name = 'Unknown'
    #                 confidence = 'Unknown'

    #                 face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
    #                 print(self.known_face_encodings)
    #                 best_match_index = np.argmin(face_distances)
                    
    #                 if matches[best_match_index]:
    #                     name = self.known_face_names[best_match_index]
    #                     confidence = face_confidence(face_distances[best_match_index])
                        
    #                 self.face_names.append(f'{name} ({confidence})')
                    
    #                 for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
    #                     top*=4
    #                     right*=4
    #                     bottom*=4
    #                     left*=4
                        
    #                     cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255),2)
    #                     cv2.rectangle(frame, (left,bottom-35), (right, bottom), (0,0,255), cv2.FILLED)
                        
    #                     cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255), 1)
                    
    #                 cv2.imshow('frame', frame)
    #                 time.sleep(2)
    #                 if cv2.waitKey(1) == ord('q'):
    #                     break
                
                    
    #             cap.release()
    #             cv2.destroyAllWindows()
                
                
                
                
if __name__ == '__main__':
    fr = FaceRecognition()
    fr.run_recognition("test.jpg")

# def main(image):
#     fr = FaceRecognition()
#     fr.run_recognition(image)