# import firebase as firebase
import pyrebase
import Operation

firebaseConfig = {
    "apiKey": "AIzaSyAaTAc9C6O0o04zRkluiUpmYpsPXDPcSnE",
    "authDomain": "learning-assistant-c4f0c.firebaseapp.com",
    "databaseURL": "https://learning-assistant-c4f0c-default-rtdb.firebaseio.com",
    "projectId": "learning-assistant-c4f0c",
    "storageBucket": "learning-assistant-c4f0c.appspot.com",
    "messagingSenderId": "975200946254",
    "appId": "1:975200946254:web:b5f6308192bda1d1bf9b1f",
    "measurementId": "G-KR2V6DB0Z3"
}

firebase = pyrebase.initialize_app(firebaseConfig)
#db = firebase.database()
auth = firebase.auth()
# storage = firebase.storage()

#lectures = db.child().get()
#result = db.child().order_by_child("session").equal_to("BCS 3.2").get()

#print(lectures.val())
#df = list(result.val().items())
#print(df)

#data = {"nme": "John", "age": 30, "address": "Kenya"}
#db.push(data)

# User sign up , creating new user account

def signup():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("account created successfully")
    except:
        print("Email already exists")

# signup()

def login():
    print("Login ....")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        print("Successfully /logged in")
    except:
        print("Invalid email or password")

ans = input("Are you a new user ? [ yes / no ] ")

if ans == "yes":
    signup()
elif ans == "no":
    login()
