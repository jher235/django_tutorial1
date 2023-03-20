from django.contrib import admin
from .models import Question,Choice

# Register your models here.

#1
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

#2
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','pub_date','was_published_recently')
    
    fieldsets = [
        (None,              {'fields':['question_text']}),
        ('Date information',{'fields' :['pub_date']}),
    ]
    inlines = [ChoiceInline]
    
    list_filter = ['pub_date']
    search_fields = ['question_text']
                 

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)

#username: admin
#password: qqqqq

#2
#username: jher
#password: jher235

