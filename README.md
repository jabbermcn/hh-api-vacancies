# My HH.ru API Interaction App

This application interacts with the HH.ru API to retrieve a list of vacancies based on specified query parameters.

## Query Parameters

- `per_page`: Number of vacancies per page (Default: 10)
- `text`: Search text within the vacancy fields specified in the `search_field` parameter. Use the [query language](https://hh.ru/article/1175) for more advanced search.
- `search_field`: Scope of the search. Refer to the [vacancy_search_fields](https://api.hh.ru/dictionaries) dictionary.
- `experience`: List of experience levels. Refer to the [experience](https://api.hh.ru/dictionaries) dictionary.
- `professional_role`: Professional role ID. Refer to the [professional_roles](https://api.hh.ru/professional_roles) dictionary.
- `period`: Number of days within which the search is performed.
- `order_by`: Sorting order for the list of vacancies. Refer to the [vacancy_search_order](https://api.hh.ru/dictionaries) dictionary.
- `area`: Region ID. Refer to the [areas](https://api.hh.ru/areas) dictionary.

## Usage

1. Install the required dependencies:
   pip install -r requirements.txt
