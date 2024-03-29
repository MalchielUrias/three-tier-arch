from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import urllib.request, json
import requests

app = Flask(__name__)



@app.route('/')
def index():

    try:
        url = "http://localhost/api/"

        flash("Welcome To KubeCounty!")
        
        response = requests.get(url, timeout=60)

    except Exception as ex:
        exc = str(ex)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
    