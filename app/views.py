from app import app, db
from flask import flash, redirect, render_template, request, session, url_for, g
from functools import wraps
 

@app.route('/', methods=['GET'])
def login():
	return render_template('')