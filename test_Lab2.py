import Lab2

def test_find_min_max():
    inputlist = [23,21,25,29,33,27,31]
    expected = [21,33]
    result = Lab2.find_min_max(inputlist)
    assert(result==expected)

def test_cal_avg():
    inputlist = [23,21,25,29,33,27,31]
    expected = 27
    result = Lab2.calc_average(inputlist)
    assert(result==expected)
    
def test_find_median_odd():
    inputlist = [33, 23, 26, 25, 29, 31, 21]
    expected = 26
    result = Lab2.calc_median_temperature(inputlist)
    assert(result==expected)

def test_find_median_even():
    inputlist = [33, 23, 26, 25, 29, 31, 21, 37]
    expected = 27.5
    result = Lab2.calc_median_temperature(inputlist)
    assert(result==expected)