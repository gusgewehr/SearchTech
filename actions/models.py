from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class Favorite(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    content     = models.BigIntegerField()
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField(blank=True, null=True, editable=False) 
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()          

        self.modified = timezone.now()
        return super(Favorite, self).save(*args, **kwargs) 

    class Meta:
        constraints = [
            # impede q o mesmo usuario tenha o mesmo conteudo mais que uma vez como favorito
            models.UniqueConstraint(fields=['user', 'content'], name='fav_user_content')
        ]

class Comment(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    content     = models.BigIntegerField()
    text        = models.TextField(max_length=(4000))
    allowed     = models.BooleanField(default= True)
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField(blank=True, null=True, editable=False) 
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()          

        self.modified = timezone.now()
        return super(Comment, self).save(*args, **kwargs) 

class Like(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    content     = models.BigIntegerField()
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField(blank=True, null=True, editable=False) 
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()          

        self.modified = timezone.now()
        return super(Like, self).save(*args, **kwargs) 

    class Meta:
        constraints = [
            # impede q o mesmo usuario tenha o mesmo conteudo mais que uma vez
            models.UniqueConstraint(fields=['user', 'content'], name='like_user_content')
        ]

class Share(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    content     = models.BigIntegerField()
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField(blank=True, null=True, editable=False) 
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()          

        self.modified = timezone.now()
        return super(Share, self).save(*args, **kwargs)   
