from django.urls import path, include
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from rest_framework.routers import SimpleRouter

router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(r'posts/(?P<post_id>[^/.]+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('follow', FollowViewSet)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
