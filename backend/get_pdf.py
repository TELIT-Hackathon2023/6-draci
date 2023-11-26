from flask import Flask, request, jsonify,render_template
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO
from threading import Timer
import json
import  model
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/upload', methods=['POST'])
def upload_file():

        if 'pdfFile' in request.files:
            pdf = request.files['pdfFile']
            filename = secure_filename(pdf.filename)
            custom_filename = 'check.pdf'
            pdf.save('./files/' + custom_filename)
            summary=model.getSummaryValues(f"./files/{custom_filename}")
            with open("output.json", "w") as json_file:
                json.dump("{ %s }" % summary, json_file)
            return "File uploaded successfully", 200
        else:
            return "No file received", 400

def emit_json_file():
    try:
        with open('./json/output.json', 'r') as file:
            data = json.load(file)
            socketio.emit('jsonData', data)
            print("Sent file ...")
    except FileNotFoundError:
        print("File not found ...")

    # Schedule the next emission after 20 seconds
    Timer(20, emit_json_file).start()

@socketio.on('sendJson')
def handle_message(data):
    with open('./json/output.json', 'r') as file:
        data = json.load(file)
        socketio.emit('jsonData', data)

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit_json_file()
        

if __name__ == '__main__':

    app.run(debug=True)

