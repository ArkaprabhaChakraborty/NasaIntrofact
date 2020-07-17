import json
import requests
from flask import Flask, render_template, url_for,redirect 

key = "IlBg3J5cz9Lph2BYmwOb6WUmCi3lEtPAfb8Xf24V"

rev = requests.get("https://api.nasa.gov/planetary/apod?api_key="+key)
rev = rev.json()
image = rev['hdurl']
ex = rev['explanation']
print(rev)
app = Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def page():
    return render_template("layout.html", image = image,ex = ex)
@app.route("/earth",methods = ['GET','POST'])
def earth():
    ex = "Welcome to NASA Landsat Imagery"
    return render_template("earth.html",ex = ex)
if __name__=="__main__":
    app.run(debug = True)
