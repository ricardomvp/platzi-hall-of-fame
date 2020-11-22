from django.db import models

# Create your models here.
class Username(models.Model):
    id=models.AutoField(primary_key=True)
    #GitHub username
    username = models.CharField(max_length=50, unique=True)
    #Response from GitHub API
    username_info = models.TextField()
    repos_info = models.TextField()

    def __str__(self):
        return '{}'.format(self.username)
