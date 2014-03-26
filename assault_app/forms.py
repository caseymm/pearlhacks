from django.forms import ModelForm
from assault_app.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['created', 'author', 'body', 'school']

form = CommentForm()

comment = Comment.objects.get(pk=1)
form = CommentForm(instance=comment)