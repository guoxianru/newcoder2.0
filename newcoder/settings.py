"""
Django settings for newcoder project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将目录加入项目环境
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%2%*k6t5z1-%lb#x6(#w#8c4ai*$0y(%qsf&r+6893l9$iwu3v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'user.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 项目应用
    'apps.blog.apps.BlogConfig',
    'apps.user.apps.UserConfig',
    # 第三方应用
    'django_summernote',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'newcoder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 侧边栏推荐文章
                'blog.global_tuijian.recommend',
                # 微信
                # 'blog.wx_token.getSignPackage'
            ],
        },
    },
]

WSGI_APPLICATION = 'newcoder.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newcoder',
        'USER': 'root',
        'PASSWORD': '1111',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


# 生产环境静态目录
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../statics')

# 开发环境静态目录
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 媒体上传路径
MEDIA_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_DIRS = [os.path.join(BASE_DIR, 'static')]

# 富文本设置
SUMMERNOTE_CONFIG = {
    # 是否使用IFrame的方式，不使用的话必须加载Bootstrap/jQuery。
    'iframe': True,
    # 以下为SummerNote自定义设置
    'summernote': {
        # 隐身模式
        'airMode': False,
        # 编辑器的尺寸
        'width': '960',
        'height': '660',
        # 语言设置
        'lang': 'zh-CN',
        # 设置字体列表
        'fontNames': ['Arial', 'Arial Black', 'Comic Sans MS', 'Courier New', '宋体', '微软雅黑']
    },
    # 附加样式表,多个主题时默认加载最后一个，建议注释不使用的主题。
    'css': (
        '/static/summernote/theme/paper.css',
    ),
}
