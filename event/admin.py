from django.contrib import admin
from event.models import Artists, Events, Fans, Polls, Questions

"""class ArtistsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'': ('name',)}


class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class FansAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('ticket',)}


class PollsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class QuestionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}"""



admin.site.register(Artists)
admin.site.register(Events)
admin.site.register(Fans)
admin.site.register(Polls)
admin.site.register(Questions)
