from django.db import models
# Create your models here.


class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    # 文章标题(title)
    headline = models.CharField(null=True, blank=True, max_length=200)
    # 文章内容(content)
    content = models.TextField(null=True, blank=True)
    # 文章图片地址(img)
    img = models.CharField(null=True, blank=True, max_length=200)
    # 浏览量(views)
    views = models.IntegerField(null=True, blank=True)
    # 点赞量(favs)
    favs = models.IntegerField(null=True, blank=True)
    # 创建日期(createtime)
    createtime = models.DateField(auto_now=True)
    # 标签
    TAG_CHOICES = (
        ('life', 'life'),
        ('tech', 'tech'),
    )
    tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)

    def __str__(self):
        return self.headline


class Comment(models.Model):
    name = models.CharField(max_length=10)
    avatar = models.CharField(max_length=100, default="static/images/default.png")
    content = models.TextField()
    createTime = models.DateField(auto_now=True)
    belong_to = models.ForeignKey(to=Article, related_name="article_comments", null=True, blank=True)
    best = models.BooleanField(default=False)

    def __str__(self):
        return self.content
