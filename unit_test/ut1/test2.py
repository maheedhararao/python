import pytest


@pytest.mark.file_2
def test_1():
    print 'testing the changes done to source dir'
    print 'testing first test from test_2 file in ut1'


@pytest.mark.file_1
def test_2():
    print 'testing the changes done to source dir'
    print 'testing second test from test_2 file in ut1'
