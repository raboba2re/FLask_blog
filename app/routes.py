from app import app, db 
from flask import render_template, redirect

@app.route('/')
def home():
    return  render_template('index.html')
