from app import app, db
from flask import flash, redirect, render_template, request, session, url_for, g
from functools import wraps
from app.forms import LoginForm
from app.models import User, Task

# creating login_required function
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash("You need to log in first.")
			return redirect(url_for('login'))
	return wrap	 

	
	
@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	form = LoginForm(request.form)	
	if request.method == 'POST':
		u = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
		if u == None:
			flash("Invalid login credentials, please try again.")
		else:
			session["logged_in"] = True
			flash("Welcome, you are now logged in." )
			return redirect(url_for('main'))
	return render_template('login.html', form=form, error=error)
	
#@app.route('/tasks')
#@login_required	
#def main():
#	return render_template('tasks.html')	

#def register():
		
#def addTask():

#def completeTask():

#def deleteTask():

#def logout():
	