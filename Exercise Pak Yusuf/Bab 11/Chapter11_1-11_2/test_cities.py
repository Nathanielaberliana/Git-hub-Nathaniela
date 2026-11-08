from city_functions import city_country


def test_city_country():
    """Apakah 'santiago' dan 'chile' menghasilkan 'Santiago, Chile'?"""
    formatted = city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'


def test_city_country_population():
    """Apakah kota, negara, dan populasi diformat dengan benar?"""
    formatted = city_country('santiago', 'chile', population=5000000)
    assert formatted == 'Santiago, Chile - population 5000000'