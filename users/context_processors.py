from .models import UserRole

def user_role_processor(request):
    role = None
    if request.user.is_authenticated:
        try:
            role = request.user.citizenprofile.role
        except Exception:
            role = None
    return {
        'user_role': role,
        'UserRole': UserRole,
    }
