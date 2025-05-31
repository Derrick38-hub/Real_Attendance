import cv2
import os
import firebase_admin
from firebase_admin import credentials, storage, db
import pickle
import face_recognition
from datetime import datetime

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': "faceattendancerealtime-88687.firebasestorage.app",
    'databaseURL': "https://faceattendancerealtime-88687-default-rtdb.europe-west1.firebasedatabase.app/"
})
bucket = storage.bucket()

# Prepare folder
folderPath = 'Images'
os.makedirs(folderPath, exist_ok=True)

# Input user data
student_id = input("Enter Student ID (e.g., 6610304): ")
student_name = input("Enter Student Name: ")

filename = f"{student_id}.png"
filepath = os.path.join(folderPath, filename)

# Open webcam and capture face
cap = cv2.VideoCapture(0)
print("📷 Press 's' to capture face.")
while True:
    success, frame = cap.read()
    if not success:
        continue

    cv2.imshow("Face Registration", frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(filepath, frame)
        print("✅ Image saved:", filepath)
        break

cap.release()
cv2.destroyAllWindows()

# Upload to Firebase Storage
blob = bucket.blob(f'Images/{filename}')
blob.upload_from_filename(filepath)
print("☁️ Uploaded to Firebase Storage.")

# Re-encode all images in Images/
print("🔄 Updating EncodeFile.p ...")
imgList = []
studentIds = []

for path in os.listdir(folderPath):
    if path.endswith(".png"):
        imgList.append(cv2.imread(os.path.join(folderPath, path)))
        studentIds.append(os.path.splitext(path)[0])

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)
        if encodes:  # Only add if encoding found
            encodeList.append(encodes[0])
    return encodeList

encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]

with open("EncodeFile.p", 'wb') as f:
    pickle.dump(encodeListKnownWithIds, f)
print("✅ EncodeFile.p updated.")

# Add to Firebase Realtime Database
ref = db.reference(f'Students/{student_id}')
ref.set({
    "name": student_name,
    "major": "Unknown",
    "starting_year": 2025,
    "total_attendance": 0,
    "standing": "Pending",
    "year": 1,
    "last_attendance_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "status": "On Time"
})
print(f"🗃️ Student {student_name} ({student_id}) added to Firebase database.")
