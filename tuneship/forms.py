from flask_wtf import FlaskForm
from wtforms import TextField, validators

class EnterDBInfo(FlaskForm):
    dbNotes = TextField(label='Items to add to DB', description='db_enter',validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])

class RetrieveDBInfo(FlaskForm):
    numRetrieve = TextField(label='Number of DB items to get', description="db_get", validators=[validators.required(), validators.Regexp('^\d{1}$', message=u'Enter a number between 1 and 10')])

class EnterTunesData(FlaskForm):
    title = TextField(label='Title of media link', description='db_enter', validators=[validators.required(),validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])
    thumb_url = TextField(label='Link for thumbnail image', description='db_enter', validators=[validators.required(),validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])
    media_url = TextField(label='Media link', description='db_enter', validators=[validators.required(),validators.Length(min=0, max=256, message=u'Enter 256 characters or less')])
    iframe_string = TextField(label='iframe string', description='db_enter', validators=[validators.required(),validators.Length(min=0, max=256, message=u'Enter 128 characters or less')])