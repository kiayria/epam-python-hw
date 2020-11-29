from counter.counter import instances_counter


@instances_counter
class Dummy:
    """This is a dummy class for testing."""

    pass


def test_counter_methods_added():
    d = Dummy()
    assert hasattr(d, "get_created_instances")
    assert hasattr(d, "reset_instances_counter")


def test_counter_amount_of_instances():
    Dummy.reset_instances_counter()
    d, _, _, _ = Dummy(), Dummy(), Dummy(), Dummy()
    assert d.get_created_instances() == 4


def test_counter_reset_return():
    Dummy.reset_instances_counter()
    d, _, _, _ = Dummy(), Dummy(), Dummy(), Dummy()
    assert d.get_created_instances() == 4
    assert d.reset_instances_counter() == 4


def test_counter_amount_after_resetting():
    Dummy.reset_instances_counter()
    d, _, _, _ = Dummy(), Dummy(), Dummy(), Dummy()
    assert d.reset_instances_counter() == 4
    assert d.get_created_instances() == 0
