import pytest

from ciphers.caesar import CeaserCipher

cipher = CeaserCipher()


@pytest.mark.parametrize('txt, key, expected', [
    ('Sonia', 3, 'Vrqld'),
    ('Abc', 2, 'Cde'),
    ('Mom', 5, 'Rtr')
])
def test_encrypt_on_text(txt, key, expected):
    actual = cipher.encrypt(txt, key)
    assert actual == expected


def test_encrypt_on_empty_should_return_empty_str():
    expected = ''
    actual = cipher.encrypt('', 2)
    assert expected == actual


@pytest.mark.parametrize('txt, key, expected', [
    ('Random string- 123', 7, 'Yhukvt zaypun- 123'),
    ('Abc12-3', 3, 'Def12-3'),
    ('Mom__', 1, 'Npn__')
])
def test_encrypt_on_numbers_and_symbols_should_return_without_change(txt, key, expected):
    actual = cipher.encrypt(txt, key)
    assert expected == actual


@pytest.mark.parametrize('txt, expected', [
    ('', ''),
    ('Abc12-3', 'Abc12-3'),
    ('Mom', 'Mom')
])
def test_encrypt_with_key_equal_0_should_return_string_without_change(txt, expected):
    actual = cipher.encrypt(txt, 0)
    assert expected == actual


@pytest.mark.parametrize('expected, key, txt', [
    ('Random string- 123', -7, 'Yhukvt zaypun- 123'),
    ('Abc12-3', -3, 'Def12-3'),
    ('Mom__', -1, 'Npn__')
])
def test_encrypt_negative_key(txt, key, expected):
    actual = cipher.encrypt(txt, key)
    assert expected == actual


@pytest.mark.parametrize('txt, key', [
    ('Random string- 123', 'a'),
    ('Abc12-3', 0.75),
    ('Mom__', 'klucz')
])
def test_encrypt_invalid_key_should_raise_TypeError(txt, key):
    with pytest.raises(TypeError):
        cipher.encrypt(txt, key)


@pytest.mark.parametrize('expected, key, txt', [
    ('Sonia', 3, 'Vrqld'),
    ('Abc', 2, 'Cde'),
    ('Mom', 5, 'Rtr')
])
def test_decrypt_on_text(txt, key, expected):
    actual = cipher.decrypt(txt, key)
    assert expected == actual


def test_decrypt_on_empty_should_return_empty_string():
    expected = ''
    actual = cipher.decrypt('', 2)
    assert expected == actual


@pytest.mark.parametrize('expected, key, txt', [
    ('Random string- 123', 7, 'Yhukvt zaypun- 123'),
    ('Abc12-3', 3, 'Def12-3'),
    ('Mom__', 1, 'Npn__')
])
def test_decrypt_on_numbers_and_symbols_should_return_without_change(txt, key, expected):
    actual = cipher.decrypt(txt, key)
    assert expected == actual


@pytest.mark.parametrize('txt, expected', [
    ('', ''),
    ('Abc12-3', 'Abc12-3'),
    ('Mom', 'Mom')
])
def test_decrypt_with_key_equal_0_should_return_string_without_change(txt, expected):
    actual = cipher.decrypt(txt, 0)
    assert expected == actual


@pytest.mark.parametrize('txt, key, expected', [
    ('Random string- 123', -7, 'Yhukvt zaypun- 123'),
    ('Abc12-3', -3, 'Def12-3'),
    ('Mom__', -1, 'Npn__')
])
def test_decrypt_negative_key(txt, key, expected):
    actual = cipher.decrypt(txt, key)
    assert expected == actual


@pytest.mark.parametrize('txt, key', [
    ('Random string- 123', 'a'),
    ('Abc12-3', 0.75),
    ('Mom__', 'klucz')
])
def test_decrypt_invalid_key_should_raise_TypeError(txt, key):
    with pytest.raises(TypeError):
        cipher.decrypt(txt, key)
