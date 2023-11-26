from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/uploadtxt', methods=['POST'])
def upload_file():

        if 'txtFile' in request.files:
            pdf = request.files['txtFile']
            filename = secure_filename(pdf.filename)
            pdf.save('./files/text/' + filename)
            return "File uploaded successfully", 200
        else:
            return "No file received", 400

if __name__ == '__main__':
    app.run(debug=True)
