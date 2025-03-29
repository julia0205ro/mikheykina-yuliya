import json
from random import randint, choice

from pytest import mark, param

from hw_4.files import DOG_BREEDS_JSON_FILE_PATH
from hw_4.validate_dog_classes import AllBreedsListResponse, SubbreedsListResponse, RandomImageDogResponse, \
    ImagesListResponse, MultiRandomImagesAllDogsResponse, MultiRandomImagesDogsBreedSubbreedResponse


class TestDogApi:
    STATUS_CODE: int = 200

    @staticmethod
    def get_dog_breeds(file) -> dict:
        """
        Чтение json файла LIST ALL BREEDS
        """
        with open(file) as f:
            return json.load(f)

    data: dict = get_dog_breeds.__func__(DOG_BREEDS_JSON_FILE_PATH)  # вызов метода для инициализации класса
    BREEDS: dict = data.get('message')  # список пород
    BREED: str = choice(list(BREEDS))  # рандомный выбор породы
    NUMBER_BREEDS: int = len(BREEDS)  # кол-во пород
    SUBBREEDS: dict = {breed: subbreed for breed, subbreed in BREEDS.items() if subbreed}  # словарь пород собак, имеющих подпороды
    BREED_WITH_SUBBREEDS: str = choice(list(SUBBREEDS))  # рандомный выбор породы с подпородами
    STATUS: str = data.get('status')  # статус ответа

    @mark.parametrize('endpoint', [
        param('breeds/list/all',
              id='list all breeds'),
        param(f'breed/{BREED_WITH_SUBBREEDS}/list',
              id='list all subbreeds from the breed'),
    ])
    def test_get_list_all_breeds(self, base_dog_url, request_dog_method, endpoint):
        url = f'{base_dog_url}/{endpoint}'
        response = request_dog_method(url=url)
        assert response.status_code == self.STATUS_CODE
        if endpoint.endswith('/all'):
            validated_data = AllBreedsListResponse.model_validate(response.json())
            assert validated_data.message == self.BREEDS
            assert validated_data.status == self.STATUS
        elif endpoint.endswith('/list'):
            validated_data = SubbreedsListResponse.model_validate(response.json())
            assert validated_data.message == self.SUBBREEDS.get(self.BREED_WITH_SUBBREEDS)
            assert validated_data.status == self.STATUS

    @mark.parametrize('endpoint', [
        param('breeds/image/random',
              id='random image from all dogs'),
        param(f'breed/{BREED}/images/random',
              id='random dog image from the breed'),
        param(f'breed/{BREED_WITH_SUBBREEDS}/{choice(SUBBREEDS.get(BREED_WITH_SUBBREEDS))}/images/random',
              id='random dog image from the subbreed')
    ])
    def test_get_random_image(self, base_dog_url, request_dog_method, endpoint):
        url = f'{base_dog_url}/{endpoint}'
        response = request_dog_method(url=url)
        assert response.status_code == self.STATUS_CODE
        validated_data = RandomImageDogResponse.model_validate(response.json())
        assert validated_data.status == self.STATUS

    @mark.parametrize('endpoint', [
        param(f'breed/{BREED}/images',
              id='array of all the images from the breed'),
        param(f'breed/{BREED_WITH_SUBBREEDS}/{choice(SUBBREEDS.get(BREED_WITH_SUBBREEDS))}/images',
              id='array of all the images from the subbreed')
    ])
    def test_get_all_images(self, base_dog_url, request_dog_method, endpoint):
        url = f'{base_dog_url}/{endpoint}'
        response = request_dog_method(url=url)
        assert response.status_code == self.STATUS_CODE
        validated_data = ImagesListResponse.model_validate(response.json())
        assert validated_data.status == self.STATUS

    @mark.parametrize('endpoint, number', [
        param(f'breeds/image/random', randint(1, 50),
              id='multi random image from all dogs'),
    ])
    def test_get_multi_random_images_from_all_dogs(self, base_dog_url, request_dog_method, endpoint, number):
        url = f'{base_dog_url}/{endpoint}/{number}'
        response = request_dog_method(url=url)
        assert response.status_code == self.STATUS_CODE
        validated_data = MultiRandomImagesAllDogsResponse.model_validate(response.json())
        assert validated_data.status == self.STATUS
        assert len(validated_data.message) == number

    @mark.parametrize('endpoint', [
        param(f'breed/{BREED}/images',
              id='multi random dog image from the breed'),
        param(f'breed/{BREED_WITH_SUBBREEDS}/{choice(SUBBREEDS.get(BREED_WITH_SUBBREEDS))}/images',
              id='multi random dog image from the subbreed'),
    ])
    def test_get_multi_random_images_from_breed_and_subbreed(self, base_dog_url, request_dog_method, endpoint):
        url = f'{base_dog_url}/{endpoint}'
        response = request_dog_method(url=url)
        number = randint(1, len(response.json().get('message')))
        url = f'{base_dog_url}/{endpoint}/random/{number}'
        response = request_dog_method(url=url)
        assert response.status_code == self.STATUS_CODE
        validated_data = MultiRandomImagesDogsBreedSubbreedResponse.model_validate(response.json())
        assert validated_data.status == self.STATUS
        assert len(validated_data.message) == number
