from django.db import models

# Create your models here.

class UseCase(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    id = models.OneToOneField(Attribute,on_delete=models.CASCADE,primary_key=True)
    value = models.CharField(max_length=50)
    use_case = models.ForeignKey(UseCase,on_delete=models.CASCADE)

    def __str__(self):
        return self.value
