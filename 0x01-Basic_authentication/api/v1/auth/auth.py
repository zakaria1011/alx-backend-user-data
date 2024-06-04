#!/usr/bin/env python3
"""
manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user. """
        return None
