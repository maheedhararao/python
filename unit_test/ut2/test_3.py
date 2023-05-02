import pytest


@pytest.mark.file_3
def test_1():
    print 'testing the changes done to source dir'
    print 'testing first test from test_3 file in ut2'


@pytest.mark.file_3
def test_2():
    print 'testing the changes done to source dir'
    print 'testing second test from test_3 file in ut2'
