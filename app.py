from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ratings.db"
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, default=0.0)

@app.route("/")
def index():
    data = Data.query.all()
    return render_template("index.html", data=data)

@app.route("/rate", methods=["POST"])
def rate():
    data_id = int(request.form["data_id"])
    rating = float(request.form["rating"])
    data = Data.query.get(data_id)
    data.rating = rating
    db.session.commit()
    return "Success"

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)