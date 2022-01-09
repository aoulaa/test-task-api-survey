from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quizz/', include(('quizz.urls', 'quizz'), namespace='quizzes')),
]

urlpatterns += doc_urls
