BASE = '/api/tasks'


def test_create_task(client):
    payload = {
        'title': 'Ship release notes',
        'description': 'Summarize the latest sprint',
        'status': 'pending',
        'priority': 'high',
    }
    res = client.post(BASE, json=payload)

    assert res.status_code == 201
    data = res.get_json()
    assert data['title'] == payload['title']


def test_create_task_rejects_whitespace_only_title(client):
    res = client.post(BASE, json={'title': '   ', 'description': 'Nope'})

    assert res.status_code == 400
    data = res.get_json()
    assert data['error'] == 'Validation failed'
    assert 'title' in data['errors']


def test_update_task_rejects_whitespace_only_title(client):
    res = client.put(f'{BASE}/1', json={'title': '   '})

    assert res.status_code == 400
    data = res.get_json()
    assert data['error'] == 'Validation failed'
    assert 'title' in data['errors']


def test_missing_task_returns_404(client):
    res = client.get(f'{BASE}/999')

    assert res.status_code == 404
    assert res.get_json()['error'] == 'Task not found'
