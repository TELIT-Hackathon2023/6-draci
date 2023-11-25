from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdfFile' in files:
        pdf = request.files['pdfFile']
        filename = secure_filename(pdf.filename)
        custom_filename = 'check.pdf'
        pdf.save('./files/'+custom_filename)

if __name__ == '__main__':
    app.run(debug=True)