from flask import Flask, render_template, request,redirect, url_for 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class AnserDb(db.Model):
    NameKey = db.Column(db.Integer, primary_key=True)
    q0Db = db.Column(db.String(50), nullable=True)
    q1Db = db.Column(db.Integer, nullable=True)
    q2Db = db.Column(db.Integer, nullable=True)
    q3Db = db.Column(db.Integer, nullable=True)
    q4Db = db.Column(db.Integer, nullable=True)
    q5Db = db.Column(db.Integer, nullable=True)
    q6Db = db.Column(db.String(50), nullable=True)
    
with app.app_context():
    db.create_all()
@app.route("/")
def index():
    message = request.args.get('message', '')  # URLパラメータからメッセージを取得
    return render_template("index.html", message=message)

@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        q0 = request.form.get("q0")
        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        q3 = request.form.get("q3")
        q4 = request.form.get("q4")
        q5 = request.form.get("q5")
        q6 = request.form.get("q6")
        if not q0 or not q1 or not q2 or not q3 or not q4 or not q5 or not q6:  # いずれかの質問が未回答の場合
            message = "すべて入力してください"
            return redirect(url_for('index', message=message))
        else:
            answer_db=AnserDb()
            answer_db.q0Db=q0
            answer_db.q1Db=q1
            answer_db.q2Db=q2
            answer_db.q3Db=q3
            answer_db.q4Db=q4
            answer_db.q5Db=q5
            answer_db.q6Db=q6
            db.session.add(answer_db)  
            db.session.commit()
            ad = db.session.query(AnserDb)
            sql_statement = ad.statement
            print(sql_statement)
            return render_template("result.html", q0=q0,q1=q1, q2=q2, q3=q3, q4=q4, q5=q5,q6=q6)
@app.route("/db")
def show_db():
    rows = AnserDb.query.all()
    return render_template("db.html", rows=rows)
if __name__ == "__main__":
    app.run(debug=True)

