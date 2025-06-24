
from django.contrib import admin
from django.urls import path , include
import debug_toolbar
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


admin.site.site_header = _('Project Management')
admin.site.site_title = _('Project Management')

urlpatterns = [
    path('__debug__',include(debug_toolbar.urls)),
    path('i18n/', include('django.conf.urls.i18n')),

]



urlpatterns += i18n_patterns (
    path('__debug__',include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('',include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    
)
