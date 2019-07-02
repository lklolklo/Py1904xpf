"""
WSGI config for test1 project.

项目发布需要使用到WSGI协议
django已经实现该协议

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test1.settings')

application = get_wsgi_application()
