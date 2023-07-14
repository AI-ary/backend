from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False, null=False)

    class Meta:
        abstract=True # 이 모델은 데이터베이스 테이블을 만드는데 사용되지 않겠다.