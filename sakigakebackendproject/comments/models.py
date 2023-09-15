from django.db import models
from assignment.models import Assignment
from django.conf import settings



class Comment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE,null=True)
    commentor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()   
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['updated_at']

    def __str__(self):
        return f"{self.commentor} - {self.created_at}"
