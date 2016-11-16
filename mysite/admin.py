from django.contrib import admin
from .models import Article
# Register your models here.

class ArticalAdmin(admin.ModelAdmin):
	list_display = ('title','pub_date','update_time','state',)


class MyModelAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super(MyModelAdmin,self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		else:
			return qs.filter(author=request.user)

admin.site.register(Article,ArticalAdmin)