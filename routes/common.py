"""shared request helpers for the routes"""
from flask import request

from models import ApiErrors


def json_body():
    """Return the request body as a dict, or raise ApiErrors (-> JSON 400).

    Uses force=True so a body sent as text/plain (navigator.sendBeacon) is
    still parsed, and silent=True so malformed JSON does not raise a 400 HTML
    page before the handler runs.
    """
    content = request.get_json(force=True, silent=True)
    if not isinstance(content, dict):
        api_errors = ApiErrors()
        api_errors.addError('body', 'expected a JSON object')
        raise api_errors
    return content
