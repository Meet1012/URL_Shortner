from django.db import models

# Create your models here.

class url_schema(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    shortCode = models.CharField(max_length=10)
    count = models.IntegerField(default=0)
    createdAt = models.CharField(max_length=100)
    updatedAt = models.CharField(max_length=100)

    def __hash__(self) -> int:
        return hash((self.id, self.url, self.shortCode, self.createdAt, self.updatedAt))