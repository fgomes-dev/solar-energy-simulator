def calculate_savings(kwh, price_per_kwh):
    return round(kwh * price_per_kwh, 2)

def test_calculate_savings():
    assert calculate_savings(500, 0.2) == 100.00
    assert calculate_savings(0, 0.2) == 0.00
    assert calculate_savings(123.45, 0.15) == 18.52
