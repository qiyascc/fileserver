from django.http import JsonResponse
from file_management.models import File

def all_files(request):
    files = File.objects.all()
    data = [
        {
            "id": file.id,
            "name": file.name or file.file.name,
            "type": file.file_type.name,
            "url": f"/media/{file.file.name}"
        }
        for file in files
    ]
    return JsonResponse(data, safe=False)

def file_detail(request, file_id):
    try:
        file = File.objects.get(id=file_id)
        data = {
            "id": file.id,
            "name": file.name or file.file.name,
            "type": file.file_type.name,
            "url": f"/media/{file.file.name}"
        }
        return JsonResponse(data)
    except File.DoesNotExist:
        return JsonResponse({"error": "File not found"}, status=404)
