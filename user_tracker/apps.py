from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserTrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_tracker"
    verbose_name = _("Django User Tracker")

