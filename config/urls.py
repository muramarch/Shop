from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from apps.shops.views import CategoryApiView, ProductApiView, SpecificationView
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', include('apps.shops.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('cart/', include('apps.cart.urls')), 
    path('api/v1/product_list', ProductApiView.as_view()),
    path('api/v1/category_list', CategoryApiView.as_view()),
    path('api/v1/specification_list', SpecificationView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
