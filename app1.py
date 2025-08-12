from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
# Khởi tạo Flask
app = Flask(__name__)

# Kết nối Firebase
cred = credentials.Certificate("D:/KHMT 16-01/Dịch vụ thông tin/Bai3/firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = request.form["temperature"]
        pressure = request.form["pressure"]
        data = {
            "name": name,
            "time": time,
            "temperature" : temperature,
            "pressure" : pressure
        }
        db.collection("weather").document(id).set(data)
        return render_template("app1_form.html", success=True)

    return render_template("app1_form.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
