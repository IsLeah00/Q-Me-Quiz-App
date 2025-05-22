from flask import request, redirect, url_for
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended.exceptions import NoAuthorizationError

def check_auth_access():
    guest_only_paths = ["/login", "/register", "/api/login", "/api/register"]

    if request.path not in guest_only_paths:
        return None

    try:
        verify_jwt_in_request()
        return redirect("/home")
    except NoAuthorizationError:
        return None
