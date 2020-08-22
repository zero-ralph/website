from .auth import urlpatterns as auth_urls
from .homepage import urlpatterns as homepage_urls


urlpatterns = auth_urls
urlpatterns += homepage_urls