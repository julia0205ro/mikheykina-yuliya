from pytest import mark, param

from hw_4.validate_brewery_classes import SingleBreweryResponse, BreweriesResponse


class TestBreweryApi:
    STATUS_CODE: int = 200

    @mark.parametrize('obdb_id, name', [
        param('b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0', 'MadTree Brewing 2.0',
              id='get brewery MadTree Brewing 2.0'),
        param('4b677b60-fef1-42e2-90ef-dadc1bd7fb06', '14er Brewing Company',
              id='get brewery 14er Brewing Company'),
    ])
    def test_get_single_brewery(self, base_brewery_url, request_brewery_method, obdb_id, name):
        url = f'{base_brewery_url}/{obdb_id}'
        response = request_brewery_method(url=url)
        assert response.status_code == self.STATUS_CODE
        validated_data = SingleBreweryResponse.model_validate(response.json())
        assert validated_data.name == name

    def test_get_all_breweries(self, base_brewery_url, request_brewery_method):
        url = f'{base_brewery_url}'
        response = request_brewery_method(url=url)
        assert response.status_code == self.STATUS_CODE
        validated_data = BreweriesResponse.model_validate(response.json())
        assert validated_data.root[0].name == '(405) Brewing Co'
        assert validated_data.root[-2].name == '1912 Brewing'

    @mark.parametrize('city, number', [
        param('Bend', 5,
              id='get 4 breweries by city Bend'),
        param('Denver', 2,
              id='get 2 breweries by city Denver'),
        param('Gary', 1,
              id='get 1 brewery by city Gary'),
    ])
    def test_get_breweries_by_city(self, base_brewery_url, request_brewery_method, city, number):
        params = {
            'by_city': city,
        }
        url = f'{base_brewery_url}'
        response = request_brewery_method(url=url, params=params)
        assert response.status_code == self.STATUS_CODE
        validated_data = BreweriesResponse.model_validate(response.json())
        assert len(validated_data.root) >= number

    @mark.parametrize('country, number', [
        param('United States', 50,
              id='get 50 breweries by country United States'),
        param('South Korea', 50,
              id='get 50 breweries by country South Korea'),
    ])
    def test_get_breweries_by_country(self, base_brewery_url, request_brewery_method, country, number):
        params = {
            'by_country': country,
        }
        url = f'{base_brewery_url}'
        response = request_brewery_method(url=url, params=params)
        assert response.status_code == self.STATUS_CODE
        validated_data = BreweriesResponse.model_validate(response.json())
        assert len(validated_data.root) == number

    @mark.parametrize('name', [
        param('1st Republic Brewing Co',
              id='get "1st Republic Brewing Co" brewery'),
        param('Abandon Brewing',
              id='get "Abandon Brewing" brewery'),
        param('1817 Brewery',
              id='get "1817 Brewery" brewery'),
    ])
    def test_get_breweries_by_name(self, base_brewery_url, request_brewery_method, name):
        params = {
            'by_name': name,
        }
        url = f'{base_brewery_url}'
        response = request_brewery_method(url=url, params=params)
        assert response.status_code == self.STATUS_CODE
        validated_data = BreweriesResponse.model_validate(response.json())
        assert len(validated_data.root) == 1
