from enum import Enum

class GlobalEnum(Enum):
    BOOK_ITEM_KEYS = ['list_name', 'display_name',
                 'list_name_encoded', 'oldest_published_date',
                 'newest_published_date', 'updated']

    OLD_YEAR = "2015"
    NEW_YEAR = "2017"
    NAME_TO_SEARCH = 'Hardcover'
x