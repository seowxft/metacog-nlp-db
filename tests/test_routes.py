"""End-to-end tests for the ten data routes.

Run with `pytest tests/` (pytest is in requirements-dev.txt).

`app` reads DATABASE_URL at import time, so this module points it at a
throwaway sqlite file before importing it.  Nothing here reads the pilot
export: every payload is built from the model column names with dummy values.
"""
import os
import sqlite3
import tempfile

import pytest

DB_PATH = os.path.join(tempfile.mkdtemp(prefix="metacog-nlp-db-test-"), "test.db")
os.environ["DATABASE_URL"] = "sqlite:///" + DB_PATH

import app as app_module  # noqa: E402
from models import ApiErrors  # noqa: E402
from models import (  # noqa: E402
    Feedback,
    MemPreTutorialData,
    MemQuizTest,
    MemTaskData,
    MemTutorialData,
    PerQuizTest,
    PerTaskData,
    PerTutorialData,
    PrePostConf,
    PsychQuiz,
)

# route path == table name for all ten routes
MODELS = {
    "feedback": Feedback,
    "mem_pre_tutorial_data": MemPreTutorialData,
    "mem_quiz_test": MemQuizTest,
    "mem_task_data": MemTaskData,
    "mem_tutorial_data": MemTutorialData,
    "per_quiz_test": PerQuizTest,
    "per_task_data": PerTaskData,
    "per_tutorial_data": PerTutorialData,
    "pre_post_conf": PrePostConf,
    "psych_quiz": PsychQuiz,
}
ROUTES = sorted(MODELS)


@pytest.fixture(scope="module")
def client():
    with app_module.app.test_client() as test_client:
        yield test_client


def columns(route):
    """Every column the route is expected to fill (i.e. all but the pkey)."""
    return [key for key in MODELS[route].__table__.columns.keys() if key != "id"]


def payload(route, user_id):
    body = {key: "%s-value" % key for key in columns(route)}
    body["userID"] = user_id
    return body


def rows_for(route, user_id):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    try:
        found = connection.execute(
            'SELECT * FROM "%s" WHERE "userID" = ?' % route, (user_id,)
        ).fetchall()
    finally:
        connection.close()
    return [dict(row) for row in found]


def post(client, route, user_id, **kwargs):
    return client.post("/%s/%s" % (route, user_id), **kwargs)


@pytest.mark.parametrize("route", ROUTES)
def test_full_row_round_trips(client, route):
    user_id = "roundtrip-%s" % route
    body = payload(route, user_id)

    response = post(client, route, user_id, json=body)

    assert response.status_code == 200
    assert response.get_json() == {"success": "yes"}
    stored = rows_for(route, user_id)
    assert len(stored) == 1
    for key in columns(route):
        assert stored[0][key] == body[key]


@pytest.mark.parametrize("route", ROUTES)
def test_missing_key_is_stored_as_null(client, route):
    user_id = "missing-%s" % route
    body = payload(route, user_id)
    dropped = columns(route)[-1]
    del body[dropped]

    response = post(client, route, user_id, json=body)

    assert response.status_code == 200
    stored = rows_for(route, user_id)
    assert len(stored) == 1
    assert stored[0][dropped] is None


@pytest.mark.parametrize("route", ROUTES)
def test_json_null_is_stored_as_null_not_the_string_none(client, route):
    user_id = "null-%s" % route
    body = payload(route, user_id)
    nulled = columns(route)[-1]
    body[nulled] = None

    response = post(client, route, user_id, json=body)

    assert response.status_code == 200
    stored = rows_for(route, user_id)
    assert len(stored) == 1
    assert stored[0][nulled] is None
    assert stored[0][nulled] != "None"


def test_text_value_longer_than_the_declared_length_is_stored_intact(client):
    user_id = "long-text"
    body = payload("pre_post_conf", user_id)
    body["selfKnowledge"] = "s" * 12000
    body["mouseMovements"] = "m" * 12000

    response = post(client, "pre_post_conf", user_id, json=body)

    assert response.status_code == 200
    stored = rows_for("pre_post_conf", user_id)
    assert len(stored) == 1
    assert stored[0]["selfKnowledge"] == body["selfKnowledge"]
    assert stored[0]["mouseMovements"] == body["mouseMovements"]


def test_empty_object_body_inserts_an_all_null_row(client):
    # An empty JSON object is still a JSON object, so json_body() accepts it and
    # field() turns every absent key into NULL (spec items 9 and 10).
    user_id = "empty-body"

    response = post(client, "pre_post_conf", user_id, json={})

    assert response.status_code == 200
    connection = sqlite3.connect(DB_PATH)
    try:
        stored = connection.execute(
            "SELECT * FROM pre_post_conf WHERE userID IS NULL AND selfKnowledge IS NULL"
        ).fetchall()
    finally:
        connection.close()
    assert len(stored) >= 1


def test_list_body_returns_a_json_400(client):
    response = post(client, "pre_post_conf", "list-body", json=[{"userID": "x"}])

    assert response.status_code == 400
    assert response.is_json
    assert response.get_json() == {"body": ["expected a JSON object"]}


def test_text_plain_json_body_is_accepted(client):
    import json

    user_id = "text-plain"
    body = payload("pre_post_conf", user_id)

    response = post(
        client,
        "pre_post_conf",
        user_id,
        data=json.dumps(body),
        content_type="text/plain",
    )

    assert response.status_code == 200
    assert len(rows_for("pre_post_conf", user_id)) == 1


@pytest.mark.parametrize("route", ROUTES)
def test_get_is_not_allowed(client, route):
    response = client.get("/%s/get-check" % route)

    assert response.status_code == 405


def test_add_error_twice_keeps_both_messages():
    errors = ApiErrors()
    errors.addError("selfKnowledge", "first")
    errors.addError("selfKnowledge", "second")

    assert errors.errors == {"selfKnowledge": ["first", "second"]}
