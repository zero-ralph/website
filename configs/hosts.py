from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'www', 'configs.subdomains.frontend', name='www'),
    host(r'admin', 'configs.subdomains.admin', name='admin'),
    
)
