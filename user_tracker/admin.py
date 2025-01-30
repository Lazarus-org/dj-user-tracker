from django.contrib import admin
from .models import ActiveUser

@admin.register(ActiveUser)
class ActiveUserAdmin(admin.ModelAdmin):
    list_display = ("user", "ip_address", "last_activity", "session_key")
    search_fields = ("user__username", "ip_address", "session_key")
    list_filter = ("last_activity",)
    readonly_fields = ("last_activity",)


    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False
    
    def has_delete_permission(self, request, obj = ...):
        return False