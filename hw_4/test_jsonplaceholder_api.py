import requests
from pytest import mark, param

from hw_4.validate_jsonplaceholder_classes import AllPostsResponse, SinglePostResponse


class TestJsonplaceholderApi:

    def test_get_all_posts(self, base_jsonplaceholder_url, request_jsonplaceholder_method):
        url = f'{base_jsonplaceholder_url}/posts'
        response = request_jsonplaceholder_method(url=url)
        assert response.status_code == 200
        validated_data = AllPostsResponse.model_validate(response.json())
        assert validated_data.root[6].title == 'magnam facilis autem'

    @mark.parametrize('id, title', [
        param(5, 'nesciunt quas odio',
              id='get post by 5 id'),
        param(11, 'et ea vero quia laudantium autem',
              id='get post by 11 id'),
    ])
    def test_get_single_post(self, base_jsonplaceholder_url, request_jsonplaceholder_method,
                             id, title):
        url = f'{base_jsonplaceholder_url}/posts/{id}'
        response = request_jsonplaceholder_method(url=url)
        assert response.status_code == 200
        validated_data = SinglePostResponse.model_validate(response.json())
        assert validated_data.title == title

    @mark.parametrize('title, body, userId', [
        param('new first test post', 'some text', 4,
              id='create first test post'),
        param('new second test post', 'some text', 9,
              id='create second test post'),
    ])
    def test_create_post(self, base_jsonplaceholder_url, request_jsonplaceholder_method,
                         title, body, userId):
        url = f'{base_jsonplaceholder_url}/posts'
        data = {
            'title': title,
            'body': body,
            'userId': userId,
        }
        response = requests.post(url=url, json=data)
        assert response.status_code == 201
        validated_data = SinglePostResponse.model_validate(response.json())
        assert validated_data.title == title
        assert validated_data.body == body
        assert validated_data.userId == userId

    @mark.parametrize('id, new_title', [
        param(7, 'new title for 7 id',
              id='update title for 7 id'),
        param(29, 'new title for 29 id',
              id='update title for 29 id'),
    ])
    def test_update_title_post(self, base_jsonplaceholder_url, request_jsonplaceholder_method,
                               id, new_title):
        url = f'{base_jsonplaceholder_url}/posts/{id}'
        data = {
            'title': new_title,
        }
        response = requests.patch(url=url, json=data)
        assert response.status_code == 200
        validated_data = SinglePostResponse.model_validate(response.json())
        assert validated_data.title == new_title

    @mark.parametrize('id', [
        param(18,
              id='delete post by 18 id'),
        param(40,
              id='delete post by 40 id'),
    ])
    def test_delete_post(self, base_jsonplaceholder_url, request_jsonplaceholder_method, id):
        url = f'{base_jsonplaceholder_url}/posts/{id}'
        response = requests.delete(url=url)
        assert response.status_code == 200
