from rest_framework.permissions import BasePermission


class UserIsActive(BasePermission):
    """If user is active"""
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
