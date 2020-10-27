from rest_framework import permissions


class UpdateOwnAccount(permissions.BasePermission):
    """ 인증시 정보 수정가능 """

    def has_object_permission(self, request, view, obj):
        """ Safe Method를 제외한 Method가 올 시 """
        """ 계정정보수저 쓰기권한을 소유자에게 부여 """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnMailList(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """ 메일링리스트 쓰기 권한을 소유자에게 부여"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_account.id == request.user.id

