
def check_variables_exists_in_item_response(best_sellers_books_response, book_item):
    for item, key_value in zip(best_sellers_books_response, book_item):
        if len(item[key_value]) != 0:
            raise Exception(f"the item does not have {key_value}. look at {item}")