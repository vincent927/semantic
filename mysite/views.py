from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
	return render(request, 'index.html')



# def add(request):
# 	a = request.GET['a']
# 	b = request.GET['b']
# 	c = int(a) + int(b)
# 	return HttpResponse(str(c))

def add(request,a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

# def home(request):
# 	string=u"我在自强学堂学习Django，用它来建网站"
# 	return render(request,'home.html',{'string':string})

# def home(request):
# 	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
# 	return render(request,'home.html',{'TutorialList':TutorialList})

# def home(request):
# 	info_dict={'site':u'自强学堂','content':u'各种IT技术教程'}
# 	return render(request,'home.html',{'info_dict':info_dict})

def home(request):
	List = map(str,range(100))
	return render(request,'home.html',{'List':List})