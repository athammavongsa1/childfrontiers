# childfrontiers URL Configuration

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Directs url requests for UI to UI app
urlpatterns += [
    path('UI/', include('UI.urls')),
]

# Directs base URL requests to UI app
urlpatterns += [
    path('', RedirectView.as_view(url='/UI/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


