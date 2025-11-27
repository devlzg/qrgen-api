from django.db import models
import uuid

class QRCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"QRCode {self.id} created at {self.created_at} with content {self.content}"
