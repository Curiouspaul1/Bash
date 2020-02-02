from bammysite import db,ma
from datetime import datetime

# Parent's data
class Parent(db.Model):
	# Parent's details
	__tablename__ = 'Parent'
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	pname = db.Column(db.String(100))
	raddress = db.Column(db.String(100))
	oaddress = db.Column(db.String(100))
	tel = db.Column(db.String(100))
	email = db.Column(db.String(100))
	family = db.Column(db.String(100))
	siblings = db.Column(db.String(50))
	etel = db.Column(db.String(50))

	#relationship
	student = db.relationship('Student',backref='stud_parent')
	siblings = db.relationship('Siblings',backref='sib_parent')
	subscriber = db.relationship('subscriber',backref='sub_parent')
# Model below describes prospective student's data

class Student(db.Model):
	# Ward's details
	__tablename__ = 'Student'
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	sname = db.Column(db.String(100))	
	dob = db.Column(db.String(100))
	bg = db.Column(db.String(100))
	bp = db.Column(db.String(100))
	state = db.Column(db.String(50))
	gen = db.Column(db.String(50))
	lga = db.Column(db.String(50))
	sex = db.Column(db.String(10))
	ail = db.Column(db.String(10))

	school = db.Column(db.String(200))
	school_address = db.Column(db.String(200))
	class_ = db.Column(db.String(100))
	year = db.Column(db.String(100))
	parentid = db.Column(db.Integer,db.ForeignKey('Parent.id'))

# sibling details
class Siblings(db.Model):
	__tablename__ = 'Siblings'
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	s_name = db.Column(db.String(100))
	s_class_ = db.Column(db.String(100))
	s_year = db.Column(db.String(100))
	parentid = db.Column(db.Integer,db.ForeignKey('Parent.id'))


# subscriber's data
class subscriber(db.Model):
	__tablename__ = 'Subscriber'
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	sub_name = db.Column(db.String(100))
	sub_email = db.Column(db.String(100))
	parentid = db.Column(db.Integer,db.ForeignKey('Parent.id'))

class News(db.Model):
	__tablename__ = 'News'
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	title = db.Column(db.String(100))
	body = db.Column(db.Text)
	date_created = db.Column(db.DateTime,default=datetime.utcnow)
	img_data = db.Column(db.Text())

class Admin(db.Model):
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	admin_email = db.Column(db.String(100))
	admin_password = db.Column(db.String(100))

# Parent's Serialization Schema
class ParentSchema(ma.Schema):
	class Meta:
		fields = ('id','name','email','etel','tel','family','siblings','oaddress','raddress')

parent_schema = ParentSchema()
parents_schema = ParentSchema(many=True)

# Student's Serialization Schema
class StudentSchema(ma.Schema):
	class Meta:
		fields = ('id','name','dob','bg','bp','sex','ail','state','gen','lga','school','school_address','class_','year','parentid')

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# sibling schema
class SiblingSchema(ma.Schema):
	class Meta:
		fields = ('id','name','class_','year','parentid')

sibling_schema = SiblingSchema()
siblings_schema = SiblingSchema(many=True)

# News' Serialization schema
class NewsSchema(ma.Schema):
	class Meta:
		fields = ('id','title','body','date_created','img_data')

news_schema = NewsSchema()
multinews_schema = NewsSchema(many=True)