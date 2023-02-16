import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'django-insecure-vqtu7ddz*c%pehw!cv90y7rl05bv$jo@#4#3=542!^olb6h(g9'

#settings.pyからそのままコピー
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}
DEBUG = True