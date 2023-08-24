import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, { 
    'databaseURL' : "https://faceattendancerealtime-b24aa-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "farhan":
    {
        "name": "Farhan Jihad A",
        "major": "Embedded",
        "starting_year": 2021,
        "Total_attendance": 6,
        "Standing": "G",
        "year":4,
        "last_attendance_time": "2022-12-11 00:54:34"

    },
    "Biden1":
    {
        "name": "Joe Biden",
        "major": "Law firm",
        "starting_year": 2014,
        "Total_attendance": 4,
        "Standing": "G",
        "year":4,
        "last_attendance_time": "2022-12-11 00:54:34"

    },
    "alditaher1":
    {
        "name": "Aldi Taher",
        "major": "Vocalist",
        "starting_year": 2016,
        "Total_attendance": 6,
        "Standing": "G",
        "year":4,
        "last_attendance_time": "2022-12-11 00:54:34"

    },
    "ivan":
    {
        "name": "Irvananda Alghifary",
        "major": "Artist",
        "starting_year": 2022,
        "Total_attendance": 6,
        "Standing": "G",
        "year":4,
        "last_attendance_time": "2022-12-11 00:54:34"

    }
    
}

for key,value in data.items():
    ref.child(key).set(value)