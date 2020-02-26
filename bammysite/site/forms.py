from flask_wtf import FlaskForm
from wtforms import FileField,StringField
from flask_ckeditor import CKEditorField

class NewsForm(FlaskForm):
	news_title = StringField('new-story__title')
	image = FileField('news_photo')
	news_body = CKEditorField('story-info')
#NewsForm.news_body(class_='ckeditor')