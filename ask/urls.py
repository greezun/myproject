from django.contrib import admin
from django.urls import include, path

urlpatterns = {
    path('qa/', include('qa.urls')),
    path('admin/', admin.site.urls),
    path('/', include('qa.urls')),
    path('login/', include('qa.urls')),
    path('signup/', include('qa.urls')),
    path('question/\d+/$/ ', include('qa.urls')),
    path('ask/', include('qa.urls')),
    path('popular/', include('qa.urls')),
    path('new/', include('qa.urls'))
}
