import os
import tempfile
import pytest
from app import app, init_db

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index(client):
    """Test the index page."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Prompt Library' in rv.data

def test_add_prompt(client):
    """Test adding a new prompt."""
    rv = client.post('/add', data=dict(
        title='Test Prompt',
        content='This is a test prompt.',
        category='Testing'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test Prompt' in rv.data

def test_view_prompt(client):
    """Test viewing a single prompt."""
    rv = client.post('/add', data=dict(
        title='Test Prompt',
        content='This is a test prompt.',
        category='Testing'
    ), follow_redirects=True)
    assert rv.status_code == 200
    rv = client.get('/prompt/1')
    assert rv.status_code == 200
    assert b'Test Prompt' in rv.data

def test_edit_prompt(client):
    """Test editing a prompt."""
    rv = client.post('/add', data=dict(
        title='Test Prompt',
        content='This is a test prompt.',
        category='Testing'
    ), follow_redirects=True)
    assert rv.status_code == 200
    rv = client.post('/edit/1', data=dict(
        title='Updated Prompt',
        content='This is an updated prompt.',
        category='Updated'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b'Updated Prompt' in rv.data

def test_delete_prompt(client):
    """Test deleting a prompt."""
    rv = client.post('/add', data=dict(
        title='Test Prompt',
        content='This is a test prompt.',
        category='Testing'
    ), follow_redirects=True)
    assert rv.status_code == 200
    rv = client.post('/delete/1', follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test Prompt' not in rv.data

def test_view_nonexistent_prompt(client):
    """Test viewing a nonexistent prompt."""
    rv = client.get('/prompt/999')
    assert rv.status_code == 404

def test_edit_nonexistent_prompt(client):
    """Test editing a nonexistent prompt."""
    rv = client.get('/edit/999')
    assert rv.status_code == 404
