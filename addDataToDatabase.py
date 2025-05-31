import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendancerealtime-88687-default-rtdb.europe-west1.firebasedatabase.app/"
})


ref = db.reference('Students')

data = {
    "640010":
    {
        "name": "Asst. Prof. Dr. Pakpoom Chaisiriprasit",
        "major" : "Deputy Dean",
        "starting_year": 2016,
        "total_attendance" : 30,
        "standing" : "A",
        "year" : 4,
        "last_attendance_time" : "2025-3-22 01:50:39"

    },

    "6610304":
    {
        "name": "Derrick",
        "major" : "Computer Science",
        "starting_year": 2024,
        "total_attendance" : 10,
        "standing" : "B+",
        "year" : 2,
        "last_attendance_time" : "2025-2-25 00:54:34"

    },

    "6610408":
    {
        "name": "Min Khant Kyaw",
        "major" : "Computer Science",
        "starting_year": 2024,
        "total_attendance" : 5,
        "standing" : "A",
        "year" : 3,
        "last_attendance_time" : "2025-2-25 01:54:34"

    },

    "6610207":
    {
        "name": "Charkon",
        "major" : "Computer Science",
        "starting_year": 2024,
        "total_attendance" : 6,
        "standing" : "B",
        "year" : 2,
        "last_attendance_time" : "2025-2-25 01:54:39"

    },

        "6509563":
    {
        "name": "Kate",
        "major" : "International Business",
        "starting_year": 2023,
        "total_attendance" : 10,
        "standing" : "A",
        "year" : 3,
        "last_attendance_time" : "2025-3-20 02:5:39"

    }
}

for key,value in data.items():
    ref.child(key).set(value)