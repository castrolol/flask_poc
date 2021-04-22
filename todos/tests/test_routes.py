from todos.models.Task import Task


def test_should_returns(client):
    response = client.get('/')
    assert b"ok" == response.data


def test_should_returns_empty_list_initially(client):
    response = client.get('/todos')
    assert len(response.json['todos']) == 0


def test_should_create_new_todo(client):
    response = client.post("/todos", json={
        "id": "1",
        "name": "Item Foo",
        "done": False,
        "color": "#fff"
    })

    assert len(Task.query.all()) == 1

