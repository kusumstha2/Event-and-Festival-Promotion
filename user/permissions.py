from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Allows access only to users with the 'admin' role.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role and request.user.role.name.lower() == 'admin')


class IsOrganizer(permissions.BasePermission):
    """
    Allows access only to users with the 'organizer' role.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role and request.user.role.name.lower() == 'organizer')


class IsSelfOrAdmin(permissions.BasePermission):
    """
    User can only access their own data unless they are an admin.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj or (request.user.role and request.user.role.name.lower() == 'admin')


class IsReadOnly(permissions.BasePermission):
    """
    Grants access only to safe methods (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
