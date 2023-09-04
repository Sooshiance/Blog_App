from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django_jalali.db import models as jmodels


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='کاربر')
    title          = models.CharField(max_length=256, verbose_name='سر برگ', unique=True, primary_key=True)
    txt            = models.CharField(max_length=16384, verbose_name='متن')
    is_private     = models.BooleanField(default=False, verbose_name='خصوصی')
    admin_approval = models.BooleanField(default=False, verbose_name='تایید مدیر')
    created_at     = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    updated_at     = jmodels.jDateTimeField(auto_now=True, verbose_name='به روز شده')
    
    def __str__(self) -> str:
        return f"{self.user} {self.title} {self.admin_approval} {self.is_private} {self.pk}"
    
    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post           = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment', verbose_name='پست')
    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment', verbose_name='کاربر')
    txt            = models.CharField(max_length=4096, verbose_name='متن')
    admin_approval = models.BooleanField(default=False, verbose_name='تایید مدیر')
    created_at     = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    
    def __str__(self) -> str:
        return f"{self.user} {self.post} {self.admin_approval} {self.pk}"
    
    class Meta:
        ordering = ['-created_at']


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like', verbose_name='کاربر')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like', verbose_name='پست')
    vote = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], verbose_name='امتیاز')
    
    @property
    def vote_avg(self):
        return
    
    def __str__(self) -> str:
        return f"{self.user} {self.post} {self.vote}"


class Complaicent(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_complaine', verbose_name='کاربر')
    comment        = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='complained_comment', verbose_name='دیدگاه')
    txt            = models.CharField(max_length=4096, verbose_name='متن اعتراض')
    admin_approval = models.BooleanField(default=False, verbose_name='تایید مدیر')
    created_at     = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    
    def __str__(self) -> str:
        return f"{self.user} {self.comment} {self.admin_approval}"
    
    class Meta:
        ordering = ['-created_at']
