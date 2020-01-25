from app import app
from flask import render_template
from .data import get_monitoring_data

@app.route('/')
@app.route('/index')
def index():
    """ Return index web page """
    data = get_monitoring_data()
    return render_template('monitoring.html', title='Demo', data=data)


