from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


# Simply does not let them delete anything if they are not a super user
class IsOwnerOrSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        # Checks to see if they are a super user, if not then they cannot
        # delete
        if_super_user = request.user.is_superuser
        # If they are not a super user
        if if_super_user:
            return True
        # ... they cannot delete the user entry
        else:
            if request.method == "DELETE":
                raise PermissionDenied(
                    'Sorry, you must be an admin to otherusers.')
            # ... but they can edit their own entry
            else:
                return True


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            raise PermissionDenied(
                'Sorry, you must be an admin to create new users.')
