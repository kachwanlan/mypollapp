from django.contrib import admin

# Register your models here.
from .models import Question, Choice

#costumize the site headers
admin.site.site_header="Pollster Admin"
admin.site.site_title="Pollster Admin Area"
admin.site.index_title="Welcome to Pollster Admin Area"


#to have the choices under the question
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[('Question', {'fields':['question_text']}),
    ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),    
    ]
    inlines=[ChoiceInline]
admin.site.register(Question,QuestionAdmin)

#the registeration below is improved above
# admin.site.register(Question)
# admin.site.register(Choice)

