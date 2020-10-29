from django.contrib import admin
from .models import Job, Highlights, Bio, BioPic, BackgroundImage, Certifications, Education

class HighlightsInline(admin.StackedInline):
    model = Highlights

class JobsAdmin(admin.ModelAdmin):
    inlines = [HighlightsInline]
    

admin.site.register(Job, JobsAdmin)
admin.site.register(Bio)
admin.site.register(BioPic)
admin.site.register(Certifications)
admin.site.register(BackgroundImage)
admin.site.register(Education)