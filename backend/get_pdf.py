from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():

        if 'pdfFile' in request.files:
            pdf = request.files['pdfFile']
            filename = secure_filename(pdf.filename)
            custom_filename = 'check.pdf'
            pdf.save('./files/' + custom_filename)
            return "File uploaded successfully", 200
        else:
            return "No file received", 400

if __name__ == '__main__':
    app.run(debug=True)

