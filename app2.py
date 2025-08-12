# from flask import Flask, render_template, request
# import firebase_admin
# from firebase_admin import credentials, firestore

# app = Flask(__name__)

# # Nếu chưa init thì mới init
# if not firebase_admin._apps:
#     cred = credentials.Certificate("D:/KHMT 16-01/Dịch vụ thông tin/Bai3/firebase-key.json")
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

# @app.route("/", methods=["GET", "POST"])
# def index():
#     weather = None
#     not_found = False
    
#     if request.method == "POST":
#         id = request.form["id"]
#         doc = db.collection("weather").document(id).get()
#         if doc.exists:
#             weather = doc.to_dict()
#             weather["id"] = id
#         else:
#             not_found = True

#     return render_template("app2_search.html", weather=weather, not_found=not_found)

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)
from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta

app = Flask(__name__)

# Kết nối Firebase (nếu chưa init thì mới init)
if not firebase_admin._apps:
    cred = credentials.Certificate("D:/KHMT 16-01/Dịch vụ thông tin/Bai3/firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        start_str = request.form["start_date"]
        end_str = request.form["end_date"]

        # Chuyển sang datetime object
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_str, "%Y-%m-%d") + timedelta(days=1)  # để bao luôn ngày kết thúc

        # Query Firestore (nếu time lưu dưới dạng string thì cần convert sang datetime khi insert)
        query = db.collection("weather") \
                  .where("time", ">=", start_date) \
                  .where("time", "<", end_date) \
                  .stream()

        results = [doc.to_dict() for doc in query]

    return render_template("app2_search.html", results=results)

if __name__ == "__main__":
    app.run(debug=True, port=5002)

