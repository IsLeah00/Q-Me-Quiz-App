from flask import request, redirect, url_for
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

def check_guest_access():
    safe_paths = ["/login", "/register", "/api/login", "/api/register"]
    
    if request.path.startswith("/static/") or request.path in safe_paths:
        return None

    try:
        verify_jwt_in_request()
        return None
    except NoAuthorizationError:
        if request.path.startswith("/api/"):
            return {"error": "Unauthorized"}, 401
        return redirect(url_for("auth.login_page"))
