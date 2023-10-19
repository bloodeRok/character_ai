from datetime import datetime

from django.db import models

from web_app.constants.defaults import NAME_MAX_LENGTH


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=NAME_MAX_LENGTH)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    surname = models.CharField(max_length=NAME_MAX_LENGTH)
    character = models.CharField(max_length=NAME_MAX_LENGTH, default='')
    time = models.DateTimeField(default=datetime.now)

    def __repr__(self):
        return f"<User(" \
               f"pk={self.pk}, " \
               f"username={self.username}, " \
               f"name={self.name}, " \
               f"surname={self.surname}, " \
               f"character={self.character}, " \
               f"time={self.time}" \
               f")>"

    def __str__(self):
        return self.__repr__()
