from flask import flask

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER ="./app/static/uploads"

app = flask(__name__)
app.config.from_object(__name__)
Allowed_Uploads = ['jpg','png','jpeg']
UploadFolder = app.config['UPLOAD_FOLDER']
from app import views

 
