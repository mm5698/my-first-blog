from django.conf import settings
from django.db import models
from django.utils import timezone

# ���f�����`(object)
# models.Model:�|�X�g��Django Model(�f�[�^�x�[�X�ɕۑ����ׂ����̂��`)
class Post(models.Model):
    # ���̃��f���ւ̃����N
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # ���������������ꂽ�e�L�X�g���`����t�B�[���h
    title = models.CharField(max_length=200)
    
    # ���������̒����e�L�X�g�p
    text = models.TextField()
    
    # ���t�Ǝ��Ԃ̃t�B�[���h
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # �u���O�����J���郁�\�b�h
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
