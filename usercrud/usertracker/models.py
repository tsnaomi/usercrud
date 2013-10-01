from django.db import models
from django.contrib import admin

class User (models.Model):

    user_firstname = models.CharField(max_length=100)
    user_lastname = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)

    def __str__(self):
        return self.user_firstname + " " + self.user_lastname


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
