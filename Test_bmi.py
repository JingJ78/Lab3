import Lab2.bmi as Lab2

def test_bmi_normal_weight():
    result = Lab2.calculate_bmi(1.5,55)
    assert (result == 0)

def test_bmi_over_weight():
    result = Lab2.calculate_bmi(1.5,80)
    assert (result == 1)


def test_bmi_under_weight():
    result = Lab2.calculate_bmi(1.5,30)
    assert (result == -1)