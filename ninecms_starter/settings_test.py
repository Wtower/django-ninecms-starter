""" Debug settings for 9cms starter """

from ninecms_starter.settings import *

DEBUG = True

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [  # disable overriden templates
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
        },
    },
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

LANGUAGES = (  # at least 2
    ('el', 'Greek'),
    ('en', 'English'),
)

IMAGE_STYLES.update({
    'thumbnail-upscale': {
        'type': 'thumbnail-upscale',
        'size': (150, 150)
    },
})
