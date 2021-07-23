from django.conf import settings
from django.db import models
from django.utils import timezone

# モデルを定義(object)
# models.Model:ポストがDjango Model(データベースに保存すべきものを定義)
class Post(models.Model):
    # 他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # 文字数が制限されたテキストを定義するフィールド
    title = models.CharField(max_length=200)
    
    # 制限無しの長いテキスト用
    text = models.TextField()
    
    # 日付と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログを公開するメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
