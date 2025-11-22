def is_admin(user):
    return user.is_superuser or user.profile.role == "admin"
