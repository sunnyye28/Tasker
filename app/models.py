from app import db

class Task(db.Model):
	__tablename__ = "tasks"
	task_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	due_date = db.Column(db.String, nullable=False)
	priority = db.Column(db.String, nullable=False)
	status = db.Column(db.String, nullable=False)
	
	def __init__(self, name, due_date, priority, status):
		self.name = name
		self.due_date = due_date
		self.priority = priority
		self.status = status
		
	#def __repr__(self):
	#	return "<self %r>" % self.body

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	username = db.Column(db.String, nullable=False, unique=True)
	email = db.Column(db.String, nullable=False, unique=True)
	password = db.Column(db.String, nullable=False)
		
	
	def __init__(self, first_name=None, last_name=None, username=None, email=None, password=None):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email
		self.password = password
		
	#def __repr__(self):
	#	return "<self %r>" % self.body
		
		
		
		
		