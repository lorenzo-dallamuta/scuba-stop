from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return super().has_permission(request, view)


class IsOwner(permissions.IsAuthenticated):
    """
    this permission type is coupled with:

    request object instances that have either an obj.profile.user (e.g. orders) or a obj.user (e.g. profiles) attribute

    viewsets that filter the queryset to match the request's user value with the appropriate records (e.g. OrderViewSet, ProfileViewSet)
    """

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.user == request.user
        return obj.user == request.user


class IsOwnerOrAdmin(IsOwner, permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        isowner = super().has_object_permission(request, view, obj)
        return isowner or request.user.is_staff
