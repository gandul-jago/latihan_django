from django.db import models

class StatusModel(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.name

class JobTitle(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    status = models.ForeignKey(StatusModel,
        related_name = 'status_status_model',
        blank = True, null = True,
        on_delete = models.SET_NULL
    )
    def __str__(self):
        return self.name


#ONE TO MANY
class Album(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    # 1 Album bisa punya banyak Song , Kalau Album dihapus semua Song ikut terhapus

    def __str__(self):
        return self.title
    
#MANY TO MANY
class Author(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 300)
    authors = models.ManyToManyField(Author, related_name='book_author')
    # 1 Book bisa punya banyak Author , 1 Author bisa punya banyak Book

    def __str__(self):
        return self.title

#ONE TO ONE
class Vehicle(models.Model):
    reg_no = models.IntegerField()
    owner = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.reg_no)

class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    #1 Vehicle cuma boleh punya 1 Car
    car_model = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.vehicle)