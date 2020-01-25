from app import app
from flask import Blueprint, render_template

@app.errorhandler(404)
def not_found_error():
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500