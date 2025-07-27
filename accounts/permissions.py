from rest_framework import permissions


class IsCustomAdmin(permissions.BasePermission):
    """Permission personnalisée pour vérifier si un utilisateur est admin selon le champ 'role'."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'




class IsOwnerOrAdmin(permissions.BasePermission):
    """Autorise l'accès uniquement si l'utilisateur est lui-même ou un admin."""

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user == obj or request.user.role == "admin")



"""after i will use isinstnace here , for more comprehension and clairity"""
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "student"

class IsProfesseur(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "professeur"

class IsSecretaireClasse(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "secretaire_classe"

class IsSecretaireGeneral(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return request.user.is_authenticated and request.user.role == "secretaire_general"