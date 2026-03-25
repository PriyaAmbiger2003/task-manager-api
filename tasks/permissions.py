from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTaskPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        
        if request.method in SAFE_METHODS:
            return True

        
        if request.method == "DELETE":
            return obj.created_by == request.user

       
        if request.method in ["PUT", "PATCH"]:
            # Assigned user OR creator can attempt update
            return (
                obj.assigned_to == request.user or
                obj.created_by == request.user
            )

        
        return False
