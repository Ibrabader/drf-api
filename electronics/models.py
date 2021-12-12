from django.db import models
from django.contrib.auth import get_user_model

class Electronics(models.Model):
    product_name =models.CharField(max_length=255)
    description = models.TextField()
    relase_date = models.DateTimeField(auto_now = True, auto_now_add=False)
    update_date = models.DateTimeField(auto_now = False, auto_now_add=True)
    brand = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name