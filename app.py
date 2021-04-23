from flask import Flask, render_template, url_for, request, session, redirect
from flask.helpers import flash
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import FileField
import os
import bcrypt
import requests
from config_on import  MONGO_URI, ALLOWED_EXTENSIONS, UPLOAD_FOLDER
import uuid
from werkzeug.utils import secure_filename

BASE_PATH ='/home/lorenzo/Desktop/fullstack_v3/'
app = Flask(__name__)

#app.config['MONGO_DBNAME'] = MONGODB_NAME
app.config['MONGO_URI'] = MONGO_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mongo = PyMongo(app)


class MyForm(FlaskForm):
    image = FileField('image')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    app.config['SECRET_KEY'] = str(uuid.uuid4()).encode('utf-8')
    return render_template('index.html')


@app.route('/logged', methods=['GET', 'POST'])
def logged():
    form = MyForm()
    if 'username' in session:
        if form.validate_on_submit() and request.method == 'POST':
            print("Uploaded")
            
            if 'image' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['image']
            
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                imgBt = file.read()
                print("ASKING")
                
                resp = requests.post(
                    "http://127.0.0.1:5002/predict", files={"file": imgBt})
                print(resp)
                resp.raise_for_status()
                result_class = resp.json()
                print(result_class)
                if str(result_class) != 'random':
                    print("NOT RANDOM")
                    resp = requests.post(
                        "http://127.0.0.1:5009/predict", files={"file": imgBt})
                    print(resp)
                    resp.raise_for_status()
                    result_class = resp.json()
                    print(result_class)
                    file.save(os.path.join(
                        app.config['UPLOAD_FOLDER'], filename))
                    full_filename = os.path.join(
                        app.config['UPLOAD_FOLDER'], filename)
                    
                    print(full_filename)
                    
                    return render_template('result.html', result_class=result_class, user_image = full_filename)
                else:
                    return "Please try with another photo containing bees or ants"
        return render_template('logged.html', form=form)
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    print('LOGIN')
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            
           
            session['username'] = request.form['username']
            
            return redirect(url_for('logged'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    print('REGISTER')
    app.config['SECRET_KEY'] = str(uuid.uuid4()).encode('utf-8')
    if request.method == 'POST':
    
        users = mongo.db.users 
        existing_user = users.find_one({'name' : request.form['username']})
        if existing_user is None: #CHECK IF THE USERNAME ALREADY EXISTS IN THE DB
    
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True, port=5000)
