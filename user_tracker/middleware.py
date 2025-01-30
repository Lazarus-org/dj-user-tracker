from django.utils.timezone import now
from .models import ActiveUser
from django.contrib.sessions.models import Session

class ActiveUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.track_active_user(request)
        return response

    def track_active_user(self, request):
        ip = self.get_client_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "")

        if request.user.is_authenticated:
            # Track authenticated users
            ActiveUser.objects.update_or_create(
                user=request.user,
                ip_address=ip,
                defaults={"user_agent": user_agent, "last_activity": now()},
            )
        else:
            # Track anonymous users using session
            session_key = request.session.session_key
            if not session_key:
                request.session.create()  # Create session if it doesn't exist
                session_key = request.session.session_key

            ActiveUser.objects.update_or_create(
                user=None,  # Anonymous user
                ip_address=ip,
                defaults={"user_agent": user_agent, "last_activity": now(), "session_key": session_key},
            )

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR", "")
        return ip
