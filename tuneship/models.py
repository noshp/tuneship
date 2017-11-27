from . import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    notes = db.Column(db.String(128), index=True, unique=False)

    def __init__(self, notes):
        self.notes = notes
    
    def __repr__(self):
        return '<Data %r>' % self.notes

class TunesData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), index=True, unique=False)
    thumb_url = db.Column(db.String(128), index=True, unique=False)
    media_url = db.Column(db.String(256), index=True, unique=True)
    iframe_string = db.Column(db.String(256), index=True, unique=True)