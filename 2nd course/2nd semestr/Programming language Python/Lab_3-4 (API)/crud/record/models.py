from django.db import models
from crud.user.models import Users

class Records(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    content = models.TextField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True,)

