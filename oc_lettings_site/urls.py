from django.contrib import admin
from django.urls import path

import lettings.views
import profiles.views
from lettings.views import home, letting
from profiles.views import profile


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('lettings/index/', lettings.views.index, name='lettings-index'),
    path('lettings/<int:letting_id>/', letting, name='lettings-detail'),
    path('profiles/index/', profiles.views.index, name='profiles-index'),
    path('profiles/<str:username>/', profile, name='profiles-detail'),
    path('sentry-debug/', trigger_error),
    ]
