from django.db import models

class Post(models.Model):
	iden = models.CharField(max_length=100)
	content = models.CharField(max_length=100)
	domain = models.CharField(max_length=100, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
class Article(models.Model):
	content = models.TextField(u'Content')
	frontId = models.CharField(u'frontId', max_length=50, null=True, blank=True)
	

	def __unicode__(self):
		return self.frontId
		
class IDForm(models.Model):
	account = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	userRule = models.CharField(u'userRule', max_length=50, null=True, blank=True)
	login_stats = models. BooleanField()

	def __unicode__(self):
		return self.account

class StateForm(models.Model):
	account = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	userRule = models.CharField(u'userRule', max_length=50, null=True, blank=True)

	def __unicode__(self):
		return self.account
		
class QuestionForm(models.Model):
	account = models.CharField(max_length=100)
	data = models.TextField(u'data')

	def __unicode__(self):
		return self.account
		
class LogForm(models.Model):
	user = models.CharField(max_length=100)
	logData = models.CharField(u'logData', max_length=50, null=True, blank=True)
	feature = models.TextField(u'feature')
	locate = models.TextField(u'locate')
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.user