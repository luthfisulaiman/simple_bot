import json

import pytest


@pytest.fixture
def client():
    """Return Flask test client that is configured for testing.

    Testing configuration should be placed in `tests/.env` file.
    """
    from csuibot.main import app
    app.config['TESTING'] = True
    return app.test_client()


def do_post(client, payload):
    base_path = '/bot'
    return client.post(base_path, data=json.dumps(payload),
                       content_type='application/json')


def test_get_index(client):
    rv = client.get('/')

    assert rv.status_code == 200
    assert rv.get_data(as_text=True) == 'Bot is Running'


def test_post_webhook(client):
    payload = dict(update_id=12345)
    rv = do_post(client, payload)

    assert rv.status_code == 200
