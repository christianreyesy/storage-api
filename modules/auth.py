import datetime
import binascii
from functools import wraps
from os import environ, urandom
import hashlib
from bottle import response, request
import jwt
import models.auth as mauth


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac(
        'sha512',
        password.encode('utf-8'),
        salt,
        100000
    )
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac(
        'sha512',
        provided_password.encode('utf-8'),
        salt.encode('ascii'),
        100000
    )
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def generate_token(data):
    return jwt.encode(data, environ["APP_SECRET"], algorithm="HS256")


def validate_token(token):
    data = jwt.decode(token, environ["APP_SECRET"], algorithms=["HS256"])
    return data


def auth_required(*args, **kwargs):
    _route_function_first = None
    roles_accepted = []
    if len(args) == 1 and callable(args[0]):
        _route_function_first = args[0]
    else:
        roles_accepted = kwargs.get("roles", [])

    def _auth_require_wrapper(_route_function):
        @wraps(_route_function)
        def _auth_required(*args, **kwargs):
            auth_header = request.headers.get("Authorization", "")
            # Bearer <token>
            token = validate_token(auth_header.split(" ")[-1])
            roles = token.get("roles", [])
            valid_role = (
                len(roles_accepted) == 0
                or
                any((role in roles for role in roles_accepted))
            )
            if not auth_header or not token or not valid_role:
                response.status = 403
                return {}
            return _route_function(*args, **kwargs)
        return _auth_required
    if _route_function_first:
        returnable = _auth_require_wrapper(_route_function_first)
    else:
        returnable = _auth_require_wrapper
    return returnable


def validate_user(email=None, phone=None, username=None, password=None):
    try:
        user = mauth.User.get(mauth.User.username == username)
        returnable = verify_password(user.password, password)
    except:
        returnable = False
    return returnable


def register_user(email=None, phone=None, username=None, password=None):
    user = mauth.User.create(
        email=email,
        phone=phone,
        username=username,
        password=hash_password(password),
        join_date=datetime.date.today()
    )
    return user
