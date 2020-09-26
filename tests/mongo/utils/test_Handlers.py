import pytest

from spotibot.mongo.utils.Handlers import object_handler


class Sample:

    def __init__(self, val: int):
        self.attr: int = val


@pytest.fixture(
    params=[
        (Sample(2), 'attr', 2),
        ({'attr': 2}, 'attr', 2)
    ],
    scope='function'
)
def setup(request):
    obj, key, outcome = request.param
    return obj, key, outcome


def test_object_handler(setup):
    obj, key, outcome = setup
    assert object_handler(obj, key) == outcome
