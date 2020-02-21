from bammysite.site import sitemod
from flask import flash,current_app, jsonify, render_template, url_for, request,g,redirect,flash,session,json
from bammysite import db,ma,mail
from bammysite.models import  Parent,Student,Siblings,subscriber,parent_schema
from bammysite.models import parents_schema,student_schema,students_schema,sibling_schema,siblings_schema,News,Admin,news_schema,multinews_schema
from flask_mail import Message
from flask_cors import cross_origin
from flask import current_app
from werkzeug.utils import secure_filename
#from bammysite.uploads import images
import hashlib, random, requests, os, smtplib
import json, datetime


# reference key gen
def refgen(key):
	rand = [i for i in key]
	random.shuffle(rand)
	rand = ''.join(rand)
	rand = hashlib.md5(rand.encode('utf-8')).hexdigest()
	return rand

# helps make objects json serializable
def myconverter(o):
	if isinstance(o,News):
		return o.__str__()

# check that current users have a session
@sitemod.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']

@sitemod.route('/feeds',methods=['GET','POST'])
def feeds():
	news = News.query.all()
	t_stamp = [i.date_created for i in news]
	t_stamp = sorted(t_stamp,key=lambda item:item, reverse=True)
	news = [News.query.filter_by(date_created=i).first() for i in t_stamp]
	current_app.logger.info(news)
	return jsonify(multinews_schema.dump(news))

@sitemod.route('/')
@sitemod.route('/index',methods=['GET','POST'])
def index():
	news = News.query.all()
	t_stamp = [i.date_created for i in news]
	t_stamp = sorted(t_stamp,key=lambda item:item, reverse=True)
	return render_template('index.html')

# application
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
@sitemod.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'POST':
		# fetch parent-data from form
		pname = request.form['name']
		raddress = request.form['raddress']
		oaddress = request.form['oaddress']
		tel = request.form['tel']
		email = request.form['email']
		family = request.form['family']
		etel = request.form['Etel']
		siblings = request.form['siblings']
		
		# fetch student data
		sname = request.form['sname']
		dob = request.form['dob']
		bg = request.form['bg']
		bp = request.form['bp']
		state = request.form['state']
		gen = request.form['gen']
		lga = request.form['lga']
		school = request.form['school']
		school_address = request.form['school_address']
		class_ = request.form['class_']
		year = request.form['year']
		sex = request.form['sex']
		ail = request.form['ail']
		occ = request.form['occupation']

		# fetch sibling data
		s_name = request.form['s_name']
		s_class = request.form['s_class']
		s_year = request.form['s_year']

		# Sibling object
		sibling = Siblings(s_name=s_name,s_class_=s_class,s_year=s_year)

		# create parent object
		parent = Parent(pname=pname,raddress=raddress,occupation=occ,oaddress=oaddress,tel=tel,email=email,family=family,etel=etel)

		# Student object
		student = Student(sname=sname,dob=dob,bg=bg,bp=bp,state=state,gen=gen,lga=lga,sex=sex,ail=ail,school=school,school_address=school_address,class_=class_,year=year)

		pay_cred = request.form['payment-cred']
		if 'file' not in request.files:
			return redirect(url_for('site.register'))
		if pay_cred.filename == '':
			error = 'No file selected'
			return render_template('register_index.html',error=error)
		if pay_cred and allowed_file(pay_cred.filename):
			filename = secure_filename(image.filename)
			image.save(os.path.join(current_app.config['UPLOADED_IMAGES_DEST'],'payments'+filename))
			news = News(title=headline,body=info,img_data=image.filename)

			db.session.add_all([parent,student,sibling])
			db.commit()

	"""	PBFPubKey = "FLWPUBK_TEST-a8dfe7089beab0ea37afb880ccb4dfe4-X"
		txref = refgen(''.join([i for i in 'Bammy2020#']))
		customer_email = email
		customer_phone = tel
		amount = 2000

		response = requests.post("https://api.ravepay.co/flwv3-pug/getpaidx/api/v2/hosted/pay",data={'customer_phone':tel,'customer_email':email,'amount':amount,'txref':txref,'PBFPubKey':PBFPubKey})
		response.encoding = 'utf-8'
		response.text
		current_app.logger.info(response.status_code)
		current_app.logger.info(response.json()['data']['link'])

		return redirect(response.json()['data']['link'])"""

	return render_template('register_index.html')


@sitemod.route('/admin_login',methods=['GET','POST'])
def admin_login():
	if request.method == 'POST':
		session.pop('user',None)
		email = request.form['admin-login__email']
		password = request.form['admin-login__password']
		user = Admin.query.filter_by(admin_email=email).first()
		if user != None:
			password = user.admin_password
			if request.form['admin-login__password'] == password:
				session['user'] = request.form['admin-login__email']
				return redirect(url_for('site.admin'))
			else:
				error='Password incorrect - forgot password?'
				return render_template('admin_login.html')
		else:
			error = 'No user with that email was found'
			return render_template('admin_login.html',error=error)

	return render_template('admin_login.html')

@sitemod.route('/admin')
def admin():
	from .forms import NewsForm
	form = NewsForm()
	if 'user' in session:
		if 'mail_msg' in session:
			msg = session['mail_msg']
			return render_template('admin_main.html',msg=msg,form=form)
		else:
			return render_template('admin_main.html',form=form)
	return render_template('admin_login.html',form=form)

@sitemod.route('/admin_logout')
def admin_logout():
	if 'user' in session:
		session.pop('user',None)
	return redirect(url_for('site.admin_login'))



@sitemod.route('/send_newsletter',methods=['GET','POST'])
def send_newsletter():
	if request.method == 'POST':
		users = subscriber.query.all()
		recipients = [user.sub_email for user in users]
		subject = request.form['newsletter__title']
		news_body = request.form['newsletter-content']
		with mail.connect() as conn:
			for user in users:
				msg = Message(subject=subject,sender=current_app.config['MAIL_DEFAULT_SENDER'],recipients=recipients)
				msg.body = render_template('newsletter.txt',news_body=news_body,subject=subject)
				msg.html = render_template('newsletter.html',news_body=news_body,subject=subject)

				try:
					conn.send(msg)
				except smtplib.SMTPException:
					return redirect(url_for('site.admin'))
		session['mail_msg'] = 'Mail sent successfully'

	return redirect(url_for('site.admin'))

@sitemod.route('/admin_signup',methods=['GET','POST'])
def admin_signup():
	if request.method == 'POST':
		admin_email = request.form['email']
		password = request.form['password']

		admin = Admin(admin_email=admin_email,admin_password=password)
		db.session.add(admin)
		db.session.commit()
	return render_template('signup.html')

# Newsletter
@sitemod.route('/news_signup',methods=['GET','POST'])
def news_signup():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		new_subscriber = subscriber(sub_name=name,sub_email=email)
		db.session.add(new_subscriber)
		db.session.commit()

		# find parent with same details
		user = Parent.query.filter_by(email=email).first()
		if user != None:
			new_subscriber.parentid = user.id
			db.session.commit()
		else:
			try:
				user = Parent.query.filter_by(pname=name).first()
				new_subscriber.parentid = user.id
			except AttributeError:
				pass

		msg = "Congrats you've successfully registered on our mailing list"

		return render_template('index.html')
	return render_template('index.html')

# config for uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@sitemod.route('/add_news',methods=['GET','POST'])
def add_news():
	from .forms import NewsForm
	form = NewsForm()
	if request.method == 'POST':
		"""current_app.config['UPLOADED_IMAGES_DEST'] = os.getcwd()+"\\bammysite\\static\\uploads"
		headline = request.form['news_headline']
		info = request.form['story-info']
		image = request.files['image']
		filename = photos.save(image)
		rec = Photo(filename=filename, user=g.user.id)
		rec.store()
		if image and allowed_file(image.filename):
			filename = secure_filename(image.filename)
			image.save(os.path.join(current_app.config['UPLOADED_IMAGES_DEST'],filename))
			news = News(title=headline,body=info,img_data=image.filename)
		news = News(title=headline,body=info)
"""
		headline = request.form['news_headline']
		info = request.form['story-info']
		image = request.files['image']
		filename = secure_filename(image.filename)
		#image.save(os.path.join(current_app.config['UPLOADED_IMAGES_DEST'],filename))
		image.save(os.path.join(current_app.config['UPLOADED_IMAGES_DEST'],filename))
		if image and allowed_file(image.filename):
			news = News(title=headline,body=info,img_data=image.filename)
		else:
			news = News(title=headline,body=info)
		
		db.session.add(news)
		db.session.commit()

		news = News.query.filter_by(title=headline).first()
		if news != None:
			msg = 'News created successfully!'
			return render_template('admin_main.html',msg=msg,form=form)

	return render_template('admin_main.html',form=form)

@sitemod.route('/news',methods=['GET','POST'])
@cross_origin()
def news():
	all_news = News.query.all()
	return jsonify(multinews_schema.dump(all_news))

@sitemod.route('/about',methods=['GET','POST'])
def about():
	return render_template('about.html')

@sitemod.route('/newspage',methods=['GET','POST'])
def newspage():
	title='Events'
	return render_template('newspage.html',title=title)


"""@sitemod.route('/pay-checkout')
def pay-checkout():
	"""
