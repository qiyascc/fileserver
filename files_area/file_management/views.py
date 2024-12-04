from django.http import HttpResponse, Http404
from django.conf import settings
import os
from .models import File, FileType

def serve_file_by_type_and_name(request, file_type, file_name):
    try:
        # FileType ve File modellerinden dosyayı sorgula
        file_type_obj = FileType.objects.get(name=file_type)
        file_obj = File.objects.get(file_type=file_type_obj, file__icontains=file_name)

        # Dosyanın tam yolunu oluştur
        file_path = os.path.join(settings.MEDIA_ROOT, file_obj.file.name)
        
        # Dosyanın varlığını kontrol et ve gönder
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type="application/pdf")
                response['Content-Disposition'] = f'inline; filename="{file_name}"'
                return response
        else:
            raise Http404("File does not exist.")
    except (FileType.DoesNotExist, File.DoesNotExist):
        raise Http404("File not found.")
