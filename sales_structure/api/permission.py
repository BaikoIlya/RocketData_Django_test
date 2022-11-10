from rest_framework import permissions


class WorkerOnly(permissions.BasePermission):
    """
    Ограничение для пользователей.
    Работник может получить доступ только к объекту в котором трудиться.
    Посмотреть список всех организация, среднюю задолженность и отфильтровать
    по продукту, могут только пользователи к которых установлен статус
    is_stuff в значение True
    """
    def has_permission(self, request, view):
        if request.META['PATH_INFO'].strip('/')[-1].isdigit():
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user in obj.workers.all()
