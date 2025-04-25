from django.db import models

class CourseManager(models.Manager):
    def course_validator(self, post):
        errors={}
        if len(post['name'])<2:
            errors['name']="Name should be at least five characters"
        if len(post['description'])<10:
            errors['description']="Description should be at least 15 characters"
        return errors
    

class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)
    objects=CourseManager()

def create_course(post):
    return Course.objects.create(name=post['name'], description=post['description'])

def get_all_courses():
    return Course.objects.all()

def getcourse(id):
    return Course.objects.get(id=id)

def deletecourse(id):
    deletecourse=Course.objects.get(id=id)
    return deletecourse.delete()

