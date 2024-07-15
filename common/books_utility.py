import pytest
from services.books_service import BooksService

class BooksUtility():

    def __init__(self, books_url, api_key):
        self.books_url = books_url
        self.api_key = api_key
        self.books_service = BooksService(books_url=self.books_url, api_key=self.api_key)

    def check_variables_exists_in_item_response(self, best_sellers_books_response, book_item):
        for item, key_value in zip(best_sellers_books_response, book_item):
            if len(item[key_value]) != 0:
                raise Exception(f"the item does not have {key_value}. look at {item}")

    def return_best_sellers_books(self):
        try:
            best_sellers_books = self.books_service.get_best_sellers_books()

            if best_sellers_books['statusCode'] != 200:
                raise Exception(f"do not get best selllers book list. {best_sellers_books}")

            best_sellers_books_response = best_sellers_books['response']['results']
            return best_sellers_books_response

        except key as KeyError:
            print(f"return_best_sellers_books failed. look at {key} error")

