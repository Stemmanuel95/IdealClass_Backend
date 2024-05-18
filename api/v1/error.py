from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    payload = {"error": HTTP_STATUS_CODES.get(status_code, "Unknown error")}

    if message:
        payload["message"] = message
    response = jsonify(payload)
    response.status_code = status_code

    return response


def bad_request(message):
    """Error Handler for Bad request error"""
    return error_response(400, message)


def not_found(message):
    """Error Handler for Not found error"""
    return error_response(404, f"{message} Not found")


def unauthorized_error():
    """Error Handler for unauthorized error"""
    return error_response(401, "Unauthorized")


def forbidden_error():
    """Error Handler for forbidden error"""
    return error_response(403, "Forbidden")
