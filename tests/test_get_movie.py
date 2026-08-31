from src.services.get_movie import GetMovie
from pytest import raises

class MockRequest:
    def __init__(self, body):
        self.json = body

def test_service_get_movie():
    mock_request = MockRequest({"movie_name": "the shining"})
    service = GetMovie()

    response = service.consult_movie(mock_request)

    assert response["title"] == "The Shining"
    assert response["released"] == "1980"
    assert response["genre"] == "Drama, Horror"
    assert response["director"] == "Stanley Kubrick"
    assert "synopsis" in response
    assert "cast" in response

def test_body_empty_error():
    mock_request = MockRequest({})
    service = GetMovie()

    with raises(Exception) as ex:
        service.consult_movie(mock_request)

    assert str(ex.value) == "Dados inválidos, verifique as informações enviadas."

def test_field_movie_name_not_in_body_error():
    mock_request = MockRequest({"name": "The Shining"})
    service = GetMovie()

    with raises(Exception) as ex:
        service.consult_movie(mock_request)

    assert str(ex.value) == "O nome do filme é obrigatório, verifique as informações enviadas."

def test_field_movie_name_not_a_string_error():
    mock_request = MockRequest({"movie_name": 123})
    service = GetMovie()

    with raises(Exception) as ex:
        service.consult_movie(mock_request)

    assert str(ex.value) == "O nome do filme deve ser uma string."