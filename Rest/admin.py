from django.contrib import admin
from Rest.models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
	list_display=['id','title','desc']

admin.site.register(Note,NoteAdmin)
