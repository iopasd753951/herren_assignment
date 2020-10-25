from rest_framework import permissions


class UpdateOwnAccount(permissions.BasePermission):
    """ 인증시 정보 수정가능 """

    def has_object_permission(self, request, view, obj):
        """ Safe Method를 제외한 Method가 올 시 """
        """ 쓰기권한을 소유자에게 부여 """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.email == request.user.email
