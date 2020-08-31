from ..base_imports import *


class Learning(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DRAFT)
    author = models.ForeignKey(User, related_name='learnings', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'learnings'
        ordering = ['-created']
    
    
    def __str__(self):
        return self.title

    
    def get_status(self):
        return self.STATUS_CHOICES[self.status][1]