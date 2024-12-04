from django.db import models

class FileType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class File(models.Model):
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.file.size > 20 * 1024 * 1024:  # 20 MB limit
            raise ValueError("File size exceeds 20MB")
        
        if self.name:
            # Dosya uzantısını koruyarak yeniden adlandırma
            ext = self.file.name.split('.')[-1]
            self.file.name = f"{self.name}.{ext}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file.name
