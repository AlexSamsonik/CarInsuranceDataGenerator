"""There is test for Faker Singleton."""

from src.singleton import FakerSingleton


def test_faker_singleton_instance():
    """Test that FakerSingleton always returns the same instance of Faker."""
    instance_one = FakerSingleton.get_instance()
    instance_two = FakerSingleton.get_instance()
    assert instance_one is instance_two, "FakerSingleton did not return the same instance."
