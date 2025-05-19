import price_info as price

def test_total_cost_shopping():

    expected_result = 46.75
    result = price.total_cost_shopping()

    assert expected_result == result



def test_cost_of_fruit():

    expected_result = 7.0
    result = price.cost_of_fruits('orange',5)
    
    assert expected_result == result 