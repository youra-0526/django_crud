
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf. urls. static import static
from django.conf import settings
import blog.views # 추가


urlpatterns = [
    path('admin/', admin.site.urls),
    #read
    path('', blog.views.home, name="home"), # 추가
    path('blog/<int:id>', blog.views.detail, name="detail"),
    #create
    path('new',blog.views.new,name = 'new'),
    path('create', blog.views.create, name = 'create'),
    #update
    path('blog/edit/<int:id>',blog.views.edit, name ="edit"),
    path('blog/update/<int:id>',blog.views.update, name ="update"),
    #delete
    path('blog/delete/<int:id>',blog.views.delete, name ="delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
