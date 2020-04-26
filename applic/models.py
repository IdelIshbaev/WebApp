from django.db import models

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    def __str__(self):
        return self.message_text
class Person(models.Model):
    name = models.CharField(max_length=200)
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name
