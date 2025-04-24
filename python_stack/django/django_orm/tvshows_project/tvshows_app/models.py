from django.db import models

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now=True)

def create_tv_show(post):
    return Show.objects.create(title=post['title'], network=post['network'], release_date=post['releasedate'], description=post['description'])

def getshow(id):
    return Show.objects.get(id=id)

def edit_tv_show(post, id):
    my_show = Show.objects.get(id=id)
    print (my_show.title)
    my_show.title = post['new_title']
    my_show.network = post['new_network']
    my_show.release_date = post['new_releasedate']
    my_show.description = post['new_description']
    my_show.save()
    return my_show

def deleteshow(id):
    deleteshow=Show.objects.get(id=id)
    return deleteshow.delete()


