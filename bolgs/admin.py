from django.contrib import admin

# Register your models here.
from .models import SignUP
from .form import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    form = SignUpForm
    # class Meta:
    #     model = SignUP


admin.site.register(SignUP, SignUpAdmin)
