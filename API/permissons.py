from rest_framework import permissions


class MyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        else:
            return request.user.is_staff
