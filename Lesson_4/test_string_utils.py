import pytest
from string_utils import StringUtils

utils = StringUtils()

# capitalize #
# 1 вариант capitalize
def test_capitalize():
# Позитивные проверки
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("привет") == "Привет"
    assert utils.capitilize("skypro привет") == "Skypro привет"
    assert utils.capitilize("123") == "123"
# Негативные проверки
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("000") == "000"
    assert utils.capitilize("987тест123") == "987тест123"
    assert utils.capitilize("__!№;%:?") == "__!№;%:?"

# 2 вариант capitalize
@pytest.mark.parametrize('input_string, expected_output', 
                         [('skypro', "Skypro"),
                          ("привет", "Привет"),
                          ("skypro привет", "Skypro привет"),
                          ("123", "123"),
                          ("", ""),
                          (" ", " "),
                          ("000", "000"),
                          ("987тест123", "987тест123"),
                          ("__!№;%:?", "__!№;%:?")])
def test_capitalize (input_string, expected_output):
    assert utils.capitilize(input_string) == expected_output

# trim #
# 1 вариант trim
def test_trim():
    assert utils.trim("   skypro") == "skypro"

# 2 вариант trim
@pytest.mark.parametrize('string, output', 
                         [('       Skypro', "Skypro"),
                          ("          привет", "привет"),
                          ("      skypro Привет!     ", "skypro Привет!     "),
                          ("", ""),
                          ("       ", "")])
def test_trim (string, output):
    assert utils.trim (string) == output
# Зафейленная проверка trim
@pytest.mark.xfail()
def test_trim_with_input():
    assert utils.trim(12345) == '12345'
    assert utils.trim('SPECIAL') == 'SPECIAL'

# to_list #
# 1 вариант to_list
def test_to_list():
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
# 2 вариант to_list
@pytest.mark.parametrize('string, delimeter, result',
                         [('яблоко,банан,апельсин', ",", ['яблоко', 'банан', 'апельсин']),
                          ("1-2-3-4-5", "-", ['1', '2', '3', '4', '5']),
                          ("", None, []),
                          ("1,2,3,4 5", None, ['1', '2', '3', '4 5']),])
def test_to_list (string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

# contains #
#1 вариант contains
def test_contains():
    utils = StringUtils()
    assert utils.contains("SkyPro", "S")
    assert not utils.contains("SkyPro", "U")\
#2 вариант contains
@pytest.mark.parametrize('string, symbol, result',
                          [('Инженер', "ж", True),
                          ("   Test    ", "T", True),
                          ("диван-кровать", '-', True),
                          ("1,2,3,4 5", '2', True),
                          ("Привет", "п", False),
                          ('', 's', False),
                          ('Test', '', True)
                          ]) 
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

# delete_symbol #
#1 вариант delete_symbol
def test_delete_symbol():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
#2 вариант delete_symbol
@pytest.mark.parametrize('string, symbol, result',
                          [('Инженер', "ж", 'Иненер'),
                          ("   Test    ", "T", "   est    "),
                          ("диван-кровать", '-', "диванкровать"),
                          ("1,2,3,4 5", '2', "1,,3,4 5"),
                          ("Привет", "я", "Привет"),
                          ('Тест', '', 'Тест'),
                          ('Test', ' ', 'Test')])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

# starts_with #
#1 вариант starts_with
def test_starts_with():
    utils = StringUtils()
    assert utils.starts_with("SkyPro", "S")
    assert not utils.starts_with("SkyPro", "P")
#2 вариант starts_with
@pytest.mark.parametrize('string, symbol, result',
                          [('Инженер', "И", True),
                          ("   Test    ", " ", True),
                          ("диван-кровать", 'д', True),
                          ("1,2,3,4 5", '2', False),
                          ("Привет", "", True),
                          (')Тест', ')', True), # фейл ')Тест', ')', True
                          ('Test', ' ', False),
                          ('Владислав Шушаков', 'в', False)])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

# end_with #
#1 вариант end_with
def test_end_with():
    utils = StringUtils()
    assert utils.end_with("SkyPro", "o")
    assert not utils.end_with("SkyPro", "y")
#2 вариант end_with
@pytest.mark.parametrize('string, symbol, result',
                          [('Инженер', "р", True),
                          ("   Test    ", " ", True),
                          ("диван-кроватI", 'I', True),
                          ("1,2,3,4 5", '5', True),
                          ("Привет", "", True),
                          ('Тест)', ')', True),
                          ('Test', '1', False),
                          ('Владислав Шушаков', 'В', False),
                          ('', '_', False)])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

# is_empty #
#1 вариант is_empty
def test_is_empty():
    utils = StringUtils()
    assert utils.is_empty("")
    assert utils.is_empty(" ")
    assert not utils.is_empty("SkyPro")
#2 вариант is_empty
@pytest.mark.parametrize('string, result',
                          [('Инженер', False),
                          ("   Test    ", False),
                          ("1,2,3,4 5", False),
                          ('(!', False),
                          ('      ', True),
                          ('', True)])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

# to_string #
#1 вариант to_string
def test_list_to_string():
    utils = StringUtils()
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
#2 вариант to_string
@pytest.mark.parametrize('lst, joiner, result',
                          [(['s','o','s'], ",", 's,o,s'),
                          ([1, 2, 3, 4, 5], None, '1, 2, 3, 4, 5'),
                          (["Первый", "Второй"], '-', "Первый-Второй"),
                          (["Первый", "Второй"], 'и', "ПервыйиВторой"),
                          (['М','В','Д'], "", "МВД"),
                          ([], None, ''),
                          ([], '.', ''),
                          ([], '', ''),])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result