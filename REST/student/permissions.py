from rest_framework.permissions import BasePermission

class IsSameUserOrAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj