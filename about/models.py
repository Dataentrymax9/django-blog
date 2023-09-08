from django.db import models

class About(models.Model):
    about_heading = models.CharField(max_length=250)
    abou_desc = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'


    def __str__(self):
        return self.about_heading
    
class SocialLink(models.Model):
    platfrom = models.CharField(max_length=50)
    links = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platfrom
    
