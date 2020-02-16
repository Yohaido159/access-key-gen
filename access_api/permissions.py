from rest_framework import permissions
from users.models import User

import json


class IsCanAccess(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.id != None:
            access_json = request.user.access
            access = json.loads(access_json)
            if obj.access == access:
                return True
        return False
