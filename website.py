import os
import webbrowser

from flask import Flask, flash, redirect, request, send_file, render_template
from werkzeug.utils import secure_filename

import getDates

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def display():
    return render_template('index.html')

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    try:
        os.remove('downloads/classes.csv')
    except:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #downloads the file locally
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            getDates.main() #generate the csv
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return send_file('downloads/classes.csv', as_attachment=True)#serves the csv for download
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
def main():
    webbrowser.open_new_tab("http://localhost:9090")
    if 'downloads' not in os.listdir():
        os.mkdir('downloads')
    if 'uploads' not in os.listdir():
        os.mkdir('uploads')
    app.run(host='0.0.0.0', port=9090,debug=False)
    

if __name__ == "__main__":
    main()
