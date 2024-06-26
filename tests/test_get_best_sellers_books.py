import pytest
from common.books_utility import BooksUtility
from common.global_enum import GlobalEnum

def test_get_best_sellers_books(get_books_utility):

    best_sellers_books = get_books_utility.return_best_sellers_books()

    get_books_utility.check_variables_exists_in_item_response(best_sellers_books, GlobalEnum.BOOK_ITEM_KEYS.value)


def test_get_best_sellers_between_two_years(get_books_utility):
    best_sellers_between_two_years = []
    best_sellers_books = get_books_utility.return_best_sellers_books()

    for item in best_sellers_books:
        oldest_published_date = item['oldest_published_date']
        newest_published_date = item['newest_published_date']
        if GlobalEnum.OLD_YEAR.value in oldest_published_date and GlobalEnum.NEW_YEAR.value in newest_published_date:
            best_sellers_between_two_years.append(item)

    assert len(best_sellers_between_two_years) == 4, f"have more books btween requested years. " \
                                                     f"{best_sellers_between_two_years}"

def test_check_how_many_books_have_specific_list_name(get_books_utility):
    best_sellers_with_list_name = []
    best_sellers_books = get_books_utility.return_best_sellers_books()

    for item in best_sellers_books:
        if GlobalEnum.NAME_TO_SEARCH.value in item['list_name']:
            best_sellers_with_list_name.append(item)

    assert len(best_sellers_with_list_name) == 8, f"have more books with requested list name. " \
                                                     f"{best_sellers_books}"


