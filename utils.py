import os
from uuid import uuid4

from django.utils import timezone


def uuid_name_upload_to(filename):
    ymd_path = timezone.now().strftime('%Y/%m/%d') # 업로드하는 년/월/일 별로
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환
    return '/'.join([
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,
])