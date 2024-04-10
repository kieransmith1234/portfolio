from django.contrib import admin
from django.urls import path
from portfolio.views import IndexView, TimelineView, CodeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('timeline/', TimelineView.as_view(), name='timeline'),
    path('code/', CodeView.as_view(), name='code'),
]
