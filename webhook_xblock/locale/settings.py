"""
Django settings for webhook_xblock project.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os

SECRET_KEY = os.getenv('DJANGO_SECRET', 'open_secret')

# Application definition

INSTALLED_APPS = (
    'statici18n',
    'webhook_xblock',
)

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# statici18n
# https://django-statici18n.readthedocs.io/en/latest/settings.html

STATICI18N_DOMAIN = 'text'
STATICI18N_PACKAGES = (
    'webhook_xblock.translations',
)
STATICI18N_ROOT = 'webhook_xblock/public/js'
STATICI18N_OUTPUT_DIR = 'translations'

# Plugin settings
WEBHOOK_USER_MODULE_BACKEND = "webhook_xblock.edxapp_wrapper.backends.user_s"
WEBHOOK_GRADE_MODULE_BACKEND = "webhook_xblock.edxapp_wrapper.backends.grade_s"
