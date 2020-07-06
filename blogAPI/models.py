from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.


class UserProfile(AbstractUser):
    bio = models.TextField()
    profile_image = models.FileField(upload_to="profile_img")

    def __str__(self):
        return self.email


class Category(models.Model):
    category = models.CharField(max_length=350)

    def __str__(self):
        return self.category


class Post(models.Model, HitCountMixin):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    featured_image = models.FileField(upload_to="images")
    summary = models.CharField(max_length=100)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field="object_p",
        related_query_name="hit_count_generic_relation")
    post_tags = TaggableManager()

    def post_summary(self):
        self.summary = self.post[:100]
        return self.summary

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.summary = self.post_summary()
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    email = models.EmailField()
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return "comment made by {}".format(self.user.first_name)

    def anonymous_user(self):
        if self.user is None:
            self.user.full_name = "Anonymous"
            self.user.profile_image = models.FileField(default="default.png")



