def city_country(city, country, population=None):
    """Kembalikan 'Kota, Negara', dengan populasi kalau diberikan."""
    formatted = f"{city.title()}, {country.title()}"
    if population:
        formatted += f" - population {population}"
    return formatted
