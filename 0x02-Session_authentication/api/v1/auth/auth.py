#!/usr/bin/env python3
"""
manage the API authentication.
"""
from flask import request
from typing import List, TypeVar
import os

class Auth:
    """ auth class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header from the request. """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user. """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        if session_name is None:
            return None
        return request.cookies.get(session_name)
