from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS gibi güvenli metodlara herkes erişebilir
        if request.method in SAFE_METHODS:
            return True
        # Diğer işlemler sadece staff (admin) kullanıcıya açıktır
        return request.user and request.user.is_staff
