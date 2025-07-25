import datetime
from django.http import FileResponse, Http404, JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
import mimetypes
import os
def serve_media_file(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['X-Frame-Options'] = 'SAMEORIGIN' # or adjust as needed
        return response
    raise Http404()
