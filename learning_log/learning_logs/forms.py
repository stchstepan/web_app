from django import forms #импортируем модуль forms

from .models import Topic, Entry #импортируем модели, с которыми будем работать

class TopicForm(forms.ModelForm):
    class Meta: #сообщает Django, на какой модели должна базироваться форма
        #и какие поля на ней должны находиться 
        model = Topic #форма создается на базе модели Topic
        fields = ['text'] #на форме размещается только поле text
        labels = {'text': ''} #приказывает Django не генерировать подпись
        #для текстового поля


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})} #включаем атрибут виджет.
        #Виджет представляет собой элемент формы HTML: однострочное или мнонострочное
        #текстовое поле, раскрывающийся список и т.д.
        #В данном случае forms.Textarea настраивает ширину текстовой области на 80
        #столбцов, вместо значения по умолчанию 40. 