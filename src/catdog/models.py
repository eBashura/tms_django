from django.db import models


class AnimalImage(models.Model):
    url = models.URLField()
    species = models.CharField(
        default='cat',
        max_length=5,
        choices=[('cat', 'Cat'), ('dog', 'Dog')],
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    type_of_img = models.CharField(
        default='png',
        max_length=5,
        choices=[('png', 'png'), ('gif', 'gif'), ('jpg', 'jpg'), ('jpeg', 'jpeg')],
    )
