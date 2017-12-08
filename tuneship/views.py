from flask import render_template, request
from . import application, db
from tuneship.models import Data, TunesData
from tuneship.forms import EnterDBInfo, RetrieveDBInfo,EnterTunesData

@application.route('/enterdb', methods=['GET', 'POST'])
def enterdb():
    form1 = EnterDBInfo(request.form)
    form2 = RetrieveDBInfo(request.form)

    if request.method == 'POST' and form1.validate():
        data_entered = Data(notes=form1.dbNotes.data)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', notes=form1.dbNotes.data)

    if request.method == 'POST' and form2.validate():
        try:
            num_return = int(form2.numRetrieve.data)
            query_db = Data.query.order_by(Data.id.desc().limit(num_return))
            for q in query_db:
                print(q.notes)
            db.session.close()
        except:
            db.session.rollback()
        return render_template('results.html', results=query_db, num_return=num_return)

    return render_template('enterdb.html', form1=form1, form2=form2)

@application.route('/entertunes', methods=['GET', 'POST'])
def entertunes():
    tunesForm = EnterTunesData(request.form)

    if request.method == 'POST' and tunesForm.validate():
        data_entered = TunesData(title=tunesForm.title.data,thumb_url=tunesForm.thumb_url.data, 
                                 media_url=tunesForm.media_url.data, iframe_string=tunesForm.iframe_string.data)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', notes=tunesForm.title.data)
    
    return render_template('entertunesdb.html',tunesForm=tunesForm)

@application.route('/')
def index():
    tunes = TunesData.query.all()
    return render_template('index.html', all_tunes = tunes)