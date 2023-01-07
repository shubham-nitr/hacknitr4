import cv2
import face_recognition
import numpy as np

diksha_image = face_recognition.load_image_file("/home/diksha/Downloads/diksha.jpg")
diksha_encoding = face_recognition.face_encodings(diksha_image)[0]

bhaiya_image = face_recognition.load_image_file("/home/diksha/Downloads/WhatsApp Image 2022-12-18 at 15.52.35.jpeg")
bhaiya_encoding = face_recognition.face_encodings(bhaiya_image)[0]
known_face_encodings = [
    diksha_encoding,
    bhaiya_encoding
]
known_face_names =[
    'Diksha',
    'Shubham'
]
face_locations= []
face_encodings= []
face_names= []
process_this_frame = True

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    resize = cv2.resize(frame, (0,0), fx= 0.25, fy=0.25)
    res = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB)
    if process_this_frame:
        face_locations = face_recognition.face_locations(res)
        face_encodings = face_recognition.face_encodings(res, face_locations)

        face_names=[]
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name ='Unknown'

            if True in matches:
                first_match_index =matches.index(True)
                name= known_face_names[first_match_index]

            #face_distances =face_recognition.face_distance(known_face_encodings, face_encoding)
            #best_match_index =np.argmin(face_distances)
            #if matches[best_match_index]:
             #   name= known_face_names[best_match_index]
            face_names.append(name)

    process_this_frame =not process_this_frame

    for (a, b, c, d), name in zip(face_locations, face_names):
        a*=4
        b*=4
        c*=4
        d*=4

        cv2.rectangle(frame, (d,a),(b,c), (0,255,0), 2)
        #cv2.rectangle(frame, (d, c-35), (b,c), (0,0,255), cv2.FILLED)
        cv2.putText(frame, name, (d+4, c-4), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)

    cv2.imshow('Image', frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()