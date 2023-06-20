from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

""" Тест 1 (Негативный). Проверяет, что запрос не возврвщает статус 200 при вводе неверного логина (почты) """
def test_get_for_invalid_user(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' not in result

"""Тест 2 (Негативный). Проверяет, что запрос не возврвщает статус 200 при вводе неверного пароля """
def test_get_for_invalid_user(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' not in result

""" Тест 3 (Негативный). Проверяет, что запрос не возврвщает статус 200 при вводе неверных логина и пароля"""
def test_get_for_invalid_user(email=invalid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' not in result

""" Тест 4 (Негативный). Прроверяет, что запрос не возвращает статус 200 при выводе списка животных в случае неверного
 ключа auth_key"""
def test_get_all_pets_with_valid_key(filter=""):
    """Вводим неверный ключ"""
    _, auth_key = 123654789
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert len(result['pets']) > 0

"""Тест 5 (Позитивный). Проверяет, что запрос возвращает статус 200 при добавлении питомца без фото"""

def test_add_new_pet_without_photo(name='MMM', animal_type='двортерьер',
                                     age='4'):
    """Проверяем что можно добавить питомца с корректными данными"""

       # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

"""Тест 6 (Позитивный). Проверяет, что можно добавить фото питомца"""
def test_add_photo_pet(pet_id='pet_id', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    #  Запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Берём id первого питомца из списка и отправляем запрос на добавление фото
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_pet(auth_key, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name



