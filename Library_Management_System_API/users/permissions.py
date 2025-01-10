from rest_framework.permissions import BasePermission

class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Check if the request.user is the same as the obj.

        :param request: The request object
        :param view: The view object
        :param obj: The object to be checked
        :return: True if the request.user is the same as the obj, False otherwise
        """
        return request.user == obj