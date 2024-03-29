from flask import Flask, request, jsonify, render_template, flash, make_response, after_this_request, redirect
from flask_sqlalchemy import SQLAlchemy
from parameters import master_username, db_password, endpoint, db_instance_name

import mysql.connector, json



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{master_username}:{db_password}@{endpoint}/{db_instance_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "userTable"
    
    userId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    jobDescription = db.Column(db.String(100))
 
    def __init__(self, task):
        self.task = task
 
    def __repr__(self):
        return f"User(firstName={self.firstName!r}, lastName={self.lastName!r}, jobDescription={self.jobDescription!r})"

# AWS RDS MySQL connection
# db = mysql.connector.connect(
#   host="your_rds_endpoint",
#   user="your_username",
#   password="your_password",
#   database="your_database_name"
# )

with app.app_context():
    db.create_all()

def create_object(results):
    return {result.firstName: result.jobDescription for result in results}


@app.route('/users', methods=['GET'])
def display():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    users = User.query.all()
    return jsonify(create_object(users))

@app.route('/users', methods=['POST'])
def add_user():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    try:
        if request.method == "POST":
            user = User(firstName=request.form.get("firstName"), lastName=request.form.get("lastName"), jobDescription=request.form.get("jobDescription"))
            db.session.add(user)
            db.session.commit()

            return redirect("/", 302)
    except:
        return redirect("/", 404)

@app.route('/health')
def index():
    return make_response("Successful health check for ALB!", 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=False)
