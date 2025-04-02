"""There is module for Singleton pattern."""

from faker import Faker


class FakerSingleton:
    """Singleton class for creating and reusing a single instance of Faker."""

    __instance = None

    @staticmethod
    def get_instance() -> Faker:
        """Get the singleton instance of Faker.

        :return: A single instance of Faker.
        """
        if FakerSingleton.__instance is None:
            # Create a new instance of Faker if it doesn't exist
            FakerSingleton.__instance = Faker()
        return FakerSingleton.__instance
