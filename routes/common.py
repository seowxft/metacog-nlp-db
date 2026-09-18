"""shared request helpers for the routes"""
import logging

from flask import current_app as app, g, has_request_context, request

from models import ApiErrors

logger = logging.getLogger(__name__)


def json_body():
    """Return the request body as a dict, or raise ApiErrors (-> JSON 400).

    Uses force=True so a body sent as text/plain (navigator.sendBeacon) is
    still parsed, and silent=True so malformed JSON does not raise a 400 HTML
    page before the handler runs.  An empty object carries no trial data, so it
    is rejected like any other unusable body.
    """
    content = request.get_json(force=True, silent=True)
    if not isinstance(content, dict) or not content:
        api_errors = ApiErrors()
        api_errors.addError('body', 'expected a non-empty JSON object')
        raise api_errors
    return content


def field(content, key):
    """Return str(content[key]), or None when the key is absent or JSON null.

    Missing keys are collected and reported once per request by
    log_missing_fields below, so a client that stops sending one field yields
    SQL NULL for it instead of losing the whole row to a KeyError.
    """
    if key not in content:
        if has_request_context():
            g.setdefault('missing_fields', []).append(key)
        return None
    value = content[key]
    return None if value is None else str(value)


@app.after_request
def log_missing_fields(response):
    missing = g.pop('missing_fields', None)
    if missing:
        logger.warning('%s %s: %s key(s) missing from the body, stored as NULL: %s',
                       request.method, request.path, len(missing), ', '.join(missing))
    return response
