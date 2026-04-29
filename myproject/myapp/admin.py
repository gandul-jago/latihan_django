from django.contrib import admin
from myapp.models import StatusModel, JobTitle, Album, Song, Author, Book, Vehicle, Car

admin.site.register(StatusModel)
admin.site.register(JobTitle)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Vehicle)
admin.site.register(Car)