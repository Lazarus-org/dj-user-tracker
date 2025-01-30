from django.db import models
from django.utils.timezone import now
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ActiveUser(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        help_text="The authenticated user (if available). Null for anonymous users.",
        db_comment="Authenticated user associated with this active session."
    )
    ip_address = models.GenericIPAddressField(
        help_text="The IP address of the user.",
        db_comment="User's last known IP address."
    )
    user_agent = models.TextField(
        help_text="The User-Agent string of the request.",
        db_comment="Stores the browser or device information of the user."
    )
    last_activity = models.DateTimeField(
        auto_now=True,
        help_text="The last time the user was active.",
        db_comment="Timestamp of the last recorded activity."
    )
    session_key = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        unique=True,
        help_text="Session key for anonymous users.",
        db_comment="Unique session key to track unauthenticated users."
    )

    class Meta:
        unique_together = ("user", "ip_address", "session_key")  # Avoid duplicates
        verbose_name = "Active User"
        verbose_name_plural = "Active Users"

    def __str__(self):
        return f"{self.user or 'Anonymous'} - {self.ip_address} - {self.last_activity}"
