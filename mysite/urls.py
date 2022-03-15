from django.conf import settings
from django.urls import include, path,re_path
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.views.static import serve

from search import views as search_views

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    # path('login/', include('login.urls')),  # 添加
    path('', include('login.urls')),  # 添加

    path('search/', search_views.search, name='search'),
    path('image_style/', include('image_style.urls')),  # 修改 原 path('', include('image_style.urls')),
    path('image_classification/', include('image_classification.urls')),  # 修改 原 path('', include('image_classification.urls')),
    path('image_color/', include('image_color.urls')),
    path('image_restore/', include('image_restore.urls')),
    path('testapp/', include('testapp.urls')),
    # re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
