from backend.utils import (
    type_count, gen_alphabet, gen_alphanumeric, gen_real_numbers, gen_integers
)


def test_gen_alphabet():
    s = gen_alphabet()
    assert s.isalpha() is True


def test_gen_integers():
    s = gen_integers()
    assert s.isnumeric() is True


def test_gen_alphanumeric():
    s = gen_alphanumeric()
    assert s.isalnum() is True


def test_gen_real_numbers():
    s = str(gen_real_numbers())
    flag = False
    if not s.isalnum():
        flag = True
    assert flag is True


def test_typecount():
    s = "hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, lizierdjfklaasf, " \
        "123192u3kjwekhf, 89181811238, 122, nmarcysfa900jkifh, 3.781, 2.11"

    count = type_count(s)
    assert count == {
        "report": {
            "alpha_count": 2,
            "alpha_num_count": 3,
            "num_count": 3,
            "real_num_count": 2,
        }
    }
