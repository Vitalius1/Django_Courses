from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def make_course(self, name, content):
        self.create(name = name, content = content)
        return
    def show_course(self):
        return self.all()
    def show_course_by_id(self, id):
        return self.get(id = id)
    def remove(self, id):
        self.filter(id = id).delete()

class Course(models.Model):
    name = models.CharField(max_length = 255)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
# Create your models here.
