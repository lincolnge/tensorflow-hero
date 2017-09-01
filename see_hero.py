# coding: utf-8
import os

import simplejson
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

from label_image import judge_shape

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/'

bootstrap = Bootstrap(app)


def gen_file_name(filename):
    i = 1
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        name, extension = os.path.splitext(filename)
        filename = '%s_%s%s' % (name, str(i), extension)
        i += 1

    return filename


@app.route("/upload", methods=['POST'])
def upload():
    files = request.files['file']
    if files:
        filename = secure_filename(files.filename)
        filename = gen_file_name(filename)

        # save file to disk
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        files.save(uploaded_file_path)

        # return json for js call back
        result = judge_shape(uploaded_file_path)
        return simplejson.dumps({
            "files": [{
                "name": "识别结果 : " + result[0].name + " , 准确度：" + str(result[0].score),
                "size": str(result[0].score),
                "url": "http://suclogger.com/",
                "thumbnailUrl": "http://suclogger.com/",
                "deleteUrl": "http://suclogger.com/",
                "deleteType": "DELETE"}]
        })


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host= '0.0.0.0')