"""There is test for Faker Singleton."""

from src.singleton import FakerSingleton


def test_faker_singleton_instance():
    """Test that FakerSingleton always returns the same instance of Faker."""
    instance1 = FakerSingleton.get_instance()
    instance2 = FakerSingleton.get_instance()
    assert instance1 is instance2, "FakerSingleton did not return the same instance."
