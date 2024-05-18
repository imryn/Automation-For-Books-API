import pytest
from services.books_service import BooksService
from common.books_utility import BooksUtility
from common.enviroment_settings import EnvironmentSettings

@pytest.fixture(scope="session")
def env_vars():
    return EnvironmentSettings().get_env_variable_dict()

@pytest.fixture(scope="session")
def get_books_service(env_vars):
    books = BooksService(books_url=env_vars['BOOKS_URL'], api_key=env_vars['API_KEY'])
    return books

@pytest.fixture(scope="session")
def get_books_utility(env_vars):
    books_utility = BooksUtility(books_url=env_vars['BOOKS_URL'], api_key=env_vars['API_KEY'])
    return books_utility

