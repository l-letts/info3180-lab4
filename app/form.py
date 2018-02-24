from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed



class UploadForm(FlaskForm):
    upload = FileField('image', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only jpg, jpeg and png images can be uploaded!')])
    

    
    
    
