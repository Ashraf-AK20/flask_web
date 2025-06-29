from flask import Flask, redirect, render_template, request, jsonify, url_for

app = Flask(__name__) 
@app.route('/welcome/<s>')
def index(s):
    if(s == "admin"):
        return  redirect(url_for('welcome_admin',asd=s))
    else:
        return welcome_guest(s) 


@app.route('/admin/<asd>')
def welcome_admin(asd):
    return '<h1>Welcome admin - 100 points %s !</h1>' % request.headers


@app.route('/guest/<name>')
def welcome_guest(name):
    return render_template('1.html', name=name)

app.run(debug=True)
