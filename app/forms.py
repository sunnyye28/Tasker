from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, DateField, IntegerField, SelectField
from wtforms.validators import Required, Email, EqualTo, Length

class LoginForm(Form):
	username = StringField("Username", validators=[Required()])
	password = PasswordField("Password", validators=[Required()])
	
class RegisterForm(Form):
	first_name =  StringField("First Name", validators=[Required()])
	last_name = StringField("Last Name", validators=[Required()])
	username = StringField("Username", validators=[Required()])
	email = StringField("Email Address", validators=[Required()])
	password = PasswordField("Password", validators=[Required(), Length(min=6, max=40)])
	confirm_password = PasswordField("Confirm Password", validators=[Required(), Length(min=6, max=40), EqualTo("password", message="Passwords must match")])

class AddTask(Form):
	name = StringField("Task Name", validators=[Required()])
	due_date = DateField("Due Date", validators=[Required()])
	priority = SelectField("Priority", validators=[Required()])
	status = SelectField("Status", validators=[Required()])
	

