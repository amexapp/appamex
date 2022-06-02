from django.contrib import admin
from .models import Encargado, Work, States, StatesPago, UploadDoc
admin.site.register(Encargado)
admin.site.register(Work)
admin.site.register(States)
admin.site.register(StatesPago)
admin.site.register(UploadDoc)
