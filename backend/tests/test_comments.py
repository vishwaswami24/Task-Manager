BASE = '/api/tasks/1/comments'


def test_create_comment(client):
    payload = {'author': 'Alice', 'content': 'Hello world'}
    res = client.post(BASE, json=payload)
    assert res.status_code == 201


def test_list_comments(client):
    client.post(BASE, json={'author':'A','content':'first'})
    client.post(BASE, json={'author':'B','content':'second'})
    res = client.get(BASE)
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)


def test_get_update_delete(client):
    res = client.post(BASE, json={'author':'X','content':'temp'})
    cid = res.get_json()['id']
    res = client.get(f'{BASE}/{cid}')
    assert res.status_code == 200
    res = client.put(f'{BASE}/{cid}', json={'author':'Y','content':'updated'})
    assert res.status_code == 200
    res = client.delete(f'{BASE}/{cid}')
    assert res.status_code == 204


def test_create_comment_rejects_whitespace_only_fields(client):
    res = client.post(BASE, json={'author': '   ', 'content': '   '})
    assert res.status_code == 400
    data = res.get_json()
    assert data['error'] == 'Validation failed'
    assert 'author' in data['errors']
    assert 'content' in data['errors']


def test_patch_comment_allows_partial_updates(client):
    res = client.post(BASE, json={'author': 'Alice', 'content': 'Original'})
    cid = res.get_json()['id']

    res = client.patch(f'{BASE}/{cid}', json={'content': 'Updated only'})

    assert res.status_code == 200
    data = res.get_json()
    assert data['author'] == 'Alice'
    assert data['content'] == 'Updated only'


def test_list_comments_for_missing_task_returns_404(client):
    res = client.get('/api/tasks/999/comments')
    assert res.status_code == 404
    assert res.get_json()['error'] == 'Task not found'
