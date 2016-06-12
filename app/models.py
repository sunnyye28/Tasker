from app import db

class Task(db.Model):
	__tablename__ = "tasks"
	task_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	due_date = db.Column(db.Date, nullable=False)
	priority = db.Column(db.String, nullable=False)
	status = db.Column(db.String, nullable=False)
	
	def __init__(self, name, due_date, priority, status):
		self.name = name
		self.due_date = due_date
		self.priority = priority
		self.status = status
		
	def __repr__(self):
		return "<Task %r>" % self.body

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	username = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	
	def __init__(self, first_name, last_name, username, email, password):
		self.first_name = None
		self.last_name = None
		self.username = None
		self.email = None
		self.password = None
		
	def __repr__(self):
		return "<self %r>" % self.body
		
		
		
		
		