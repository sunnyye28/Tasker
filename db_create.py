from app import db
from app.models import Task, User
from datetime import date 


db.create_all()

dummytask1 = Task("Write report on customer buying trends", date(2016, 6, 20), "High", "Incomplete")
dummytask2 = Task("Call product supplier", date(2016, 6, 5), "Medium", "Completed")

db.session.add(dummytask1)
db.session.add(dummytask2)

db.session.commit()