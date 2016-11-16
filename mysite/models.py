from __future__ import  unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
#coding:utf-8
# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name


class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __str__(self):  # __str__ on Python 3
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()

	def __str__(self):  # __str__ on Python 3
		return self.name

@python_2_unicode_compatible
class Entry(models.Model):
	blog = models.ForeignKey(Blog)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	authors = models.ManyToManyField(Author)
	n_comments = models.IntegerField()
	n_pingbacks = models.IntegerField()
	rating = models.IntegerField()

	def __str__(self):  # __str__ on Python 3
		return self.headline


class Article(models.Model):
	title = models.CharField(u'标题', max_length=256)
	content = models.TextField(u'内容')

	pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
	state = models.IntegerField(u'状态',default=0)

	def __str__(self):
		return self.title