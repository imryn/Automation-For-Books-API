import pytest

@pytest.mark.parametrize("author_value", ["stephen king", "lewis carroll"])
def test01_search_book_by_exist_author_name(get_books_service, author_value):
    book_reviews = get_books_service.get_review(author=author_value)

    assert book_reviews['statusCode'] == 200, f"no reviews related to authour requested. {book_reviews}"
    book_reviews_response = book_reviews['response']['results']

    for item in book_reviews_response:
        assert item['book_author'].lower() == author_value, f"found book that his author is not related to " \
                                                                f"requested author. {item}"

def test_search_book_by_not_exist_author_name(get_books_service):
    book_reviews = get_books_service.get_review(author="test123")

    assert book_reviews['statusCode'] == 200, f"send invalue variable related to authour requested. {book_reviews}"
    book_reviews_response = book_reviews['response']['results']

    assert len(book_reviews_response) == 0 , f"get reviews on books even though you sent invalid author " \
                                             f"name {book_reviews_response}"

def test_search_review_on_book_with_invalid_query_param(get_books_service):
    book_reviews = get_books_service.get_review(test="stephen king")

    book_reviews['statusCode'] == 400, f"getting reviews on books with invalid query param {book_reviews}"

def test02_make_sure_each_review_object_as_all_variables(get_books_service):
    book_reviews = get_books_service.get_review(author="lewis carroll")

    assert book_reviews['statusCode'] == 200, f"no reviews related to authour requested. {book_reviews}"
    book_reviews_response = book_reviews['response']['results']

    for item in book_reviews_response:
        assert len(item['url']) != 0, f"no url for book review. {item}"
        assert len(item['publication_dt']) != 0, f"no publication_dt for book review. {item}"
        assert len(item['book_title']) != 0, f"no book_title for book review {item}"
        assert len(item['uuid']) != 0, f"no uuid for book review {item}"
        assert len(item['uri']) != 0, f"no uri for book review {item}"
        assert len(item['isbn13']) != 0, f"no isbn13 for book review {item}"