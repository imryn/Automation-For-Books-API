from common.http_client import HttpClient

class BooksService(HttpClient):

    def __init__(self, books_url, api_key):
        self.books_url = books_url
        self.api_key = api_key

    def get_review(self, **kwargs):
        response = self.get(f"{self.books_url}/reviews.json?api-key={self.api_key}", params=kwargs)
        return response

    def get_best_sellers_books(self):
        response = self.get(f"{self.books_url}/lists/names?api-key={self.api_key}")
        return response