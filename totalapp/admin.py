from django.contrib import admin
from totalapp.models import User
from totalapp.models import Albums
from totalapp.models import UserAlbums
from totalapp.models import Sources

admin.site.register(User)
admin.site.register(Albums)
admin.site.register(UserAlbums)
admin.site.register(Sources)
