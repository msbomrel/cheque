import os
from flask import Flask, render_template, request,redirect, url_for, send_from_directory
from os.path import dirname, join, realpath
from werkzeug.utils import secure_filename
from Services import MainServices
import numpy
import scipy
import edgedetect
import preprocess
import segmentall
import process1
import recognizechars
import yetikai

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/images/')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename, extension):
    return '.' in filename and extension in ALLOWED_EXTENSIONS

def get_extension(filename):
    return filename.rsplit('.', 1)[1].lower()
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/')
def index():
    MainServices.clean_dir()
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'cheque' not in request.files:
            message = "No file part!"
            return render_template('index.html', message=message)
        cFile = request.files['cheque']

        if cFile.filename == '':
            message = "No selected file!"
            return render_template('index.html', message=message)
        else:
            MainServices.clean_dir()
            filename = secure_filename(cFile.filename)
            extension = get_extension(filename)
            if (allowed_file(filename,extension) == False):
                message = "File type not allowed!"
                return render_template('index.html', message=message)

            exact = os.path.join(UPLOAD_FOLDER, filename)
            cFile.save(exact)
            print exact
            return  render_template('index.html', img = filename)
    else:
        return redirect(request.url)


@app.route('/imageprocess')
def imageprocess():
    print "I am here"
    edgedetect.detect()
    process1.proc()
    yetikai.horaw()
    preprocess.preprocess()
    segmentall.segment()
    return render_template('results0.html')

@app.route('/predict')
def predict():
    print 'I am here1'
    sabai = recognizechars.khojyo_yesle()
    name = sabai[0]
    date = sabai[1]
    amountW = sabai[2]
    amountN = sabai[3]
    return render_template('results.html', name = name, date = date, amountW = amountW, amountN = amountN)


@app.errorhandler(Exception)
def all_exception_handler(error):
    return render_template('error1.html')

if __name__ == '__main__':
    app.run(debug = True)
