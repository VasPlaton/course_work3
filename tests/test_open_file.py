from src.utils import open_file


def test_open_file():
    assert open_file('data_for_test_open_file.json') == [1, 2, 3]
