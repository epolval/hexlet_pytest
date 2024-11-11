import pytest
@pytest.fixture()
def sqrt():
    x = [1,2,3,4,5]
    for i in x:
        yield i * i
         #return i * i



y = sqrt()
print(y)
print(list(y))