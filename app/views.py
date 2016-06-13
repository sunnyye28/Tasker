from app import app, db
from flask import Flask, flash, redirect, render_template, request, session, url_for, g
from functools import wraps
from app.forms import LoginForm, RegisterForm
from app.models import User, Task
from sqlalchemy.exc import IntegrityError

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
	
	

@app.route('/register', methods=['POST', 'GET'])
def register():
	error = None
	form = RegisterForm(request.form, csrf_enabled=False)
	if form.validate_on_submit():
		new_user = User(
						form.first_name.data,
						form.last_name.data,
						form.username.data,
						form.email.data,
						form.password.data						
					)
		
		try:
			db.session.add(new_user)
			db.session.commit()
			flash("Account succesfully registered! Please log in.")
			return redirect(url_for('login'))
		except IntegrityError:
			error = "Sorry, an account already exists with that username and/or email"
	else:
		flash_errors(form)
		
	return render_template('register.html', form=form, error=error)

	
def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')
		
		
@app.route('/tasks')
@login_required	
def main():
	
	incomplete_tasks = Task.query.filter_by(status="Incomplete").order_by(Task.due_date.asc()) 
	completed_tasks = Task.query.filter_by(status="Completed").order_by(Task.due_date.asc())
	
	return render_template('main.html', incomplete_tasks=incomplete_tasks, completed_tasks=completed_tasks)
	
	#open_tasks = db.session.query(FTasks).filter_by(status='1').order_by(FTasks.due_date.asc())
	#closed_tasks = db.session.query(FTasks).filter_by(status='0').order_by(FTasks.due_date.asc())
	#return render_template('tasks.html', form = AddTask(request.form), open_tasks=open_tasks, closed_tasks=closed_tasks)	

@app.route('/logout')
@login_required	
def logout():
	session.pop('logged_in', None)
	flash("You succesfully logged out.")
	return redirect(url_for('login'))
		
#def addTask():

#def completeTask():

#def deleteTask():


	