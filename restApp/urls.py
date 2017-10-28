from django.conf.urls import url, include
from django.contrib import admin

from . import views as restAppViews

urlpatterns = [
	# Home Page
	url(r'^$', restAppViews.home, name="home"),

	url(r'^admin/', admin.site.urls),
	url(r'^snippets/', include('snippets.urls'))
]
