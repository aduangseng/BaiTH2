from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Nếu chưa init thì mới init
if not firebase_admin._apps:
    cred = credentials.Certificate("D:/KHMT 16-01/Dịch vụ thông tin/Bai3/firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    not_found = False

    if request.method == "POST":
        id = request.form["id"]
        doc = db.collection("weather").document(id).get()
        if doc.exists:
            weather = doc.to_dict()
            weather["id"] = id
        else:
            not_found = True

    return render_template("app2_search.html", weather=weather, not_found=not_found)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

