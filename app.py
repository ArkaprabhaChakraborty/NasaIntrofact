import json
import requests
from flask import Flask, render_template, url_for,redirect, request 
import os

key = "IlBg3J5cz9Lph2BYmwOb6WUmCi3lEtPAfb8Xf24V"

rev = requests.get("https://api.nasa.gov/planetary/apod?api_key="+key)
rev = rev.json()
image = rev['hdurl']
ex = rev['explanation']
app = Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def page():
    return render_template("layout.html", image = image,ex = ex)
@app.route("/earth",methods = ['GET','POST'])
def earth():
    ex = "Welcome to NASA Landsat Imagery"
    return render_template("earth.html",ex = ex)
@app.route("/earthdata",methods = ['GET','POST'])
def retro():
    lat = str(request.form.get('lat'))
    lon = str(request.form.get('long'))
    urlearth = str("https://api.nasa.gov/planetary/earth/imagery?lon="+lon+"&lat="+lat+"&dim=0.10&api_key="+key)
    '''
    data = requests.get(urlearth)
    data = data.json()
    print(data)
    urlearth = data['url']
    '''
    return render_template("earthdat.html",image = urlearth)
@app.route("/epic",methods = ['GET','POST'])
def alpha():
    return render_template("epic.html")
@app.route("/epicdata")
def beta():
    url = str("https://api.nasa.gov/archive/EPIC/archive/natural/2020/07/18/png/epic_1b_20200712010437.png?api_key="+key)
    return redirect("https://epic.gsfc.nasa.gov/")
if __name__=="__main__":
    app.run(debug = True)
