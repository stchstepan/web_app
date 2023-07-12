from django.contrib import admin
from .models import Topic, Entry #импортируем модель из models.py
#. (точка) перед models сообщает Django, что модель следует 
#искать в одном каталоге с admin.py

admin.site.register(Topic) #данный вызов сообщает Django, что
#управление моделью должно осуществляться через административный
#сайт
admin.site.register(Entry)