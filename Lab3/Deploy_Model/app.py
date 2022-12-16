from flask import Flask, render_template, request, send_from_directory
import os
app = Flask(__name__, static_folder="static")
UPLOAD_FOLDER = 'C:/Users/PC\Desktop/S8/MULTIPLATFORM/cross/Lab3/Deploy_Model/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return (render_template('index.html'))

#@app.route('/upload', methods = ['POST'])
def upload_file():
    f = request.files['file']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
    f.save(image_path)
    return render_template("index.html", filename=image_path)

@app.route('/upload', methods = ['POST'])
def upload():
    f = request.files['file']
    if f:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(image_path)
        return render_template('index.html', textResult='file uploaded successfully', imgPath='static/uploads/' + f.filename)
    return render_template('index.html', textResult='Please uploade a file',)

app.run()