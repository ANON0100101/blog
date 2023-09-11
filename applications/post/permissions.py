from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsOwnerAdminOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        print(request.method)
        print(SAFE_METHODS)
        if request.method == 'GET':
            return request.user.is_authenticated
           
        return request.user.is_authenticated and request.user ==obj.owner or request.user.is_staff