from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserProfileViewSet, CategoryViewSet

router = DefaultRouter()

router.register("user", UserProfileViewSet, basename="users")
router.register("post", PostViewSet, basename="posts")
router.register("comment", CommentViewSet, basename="comments")
router.register("category", CategoryViewSet, basename="category")

urlpatterns = [

]+router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

