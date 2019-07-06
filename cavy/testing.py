import logging
import os
import unittest


class EnvironmentMixin(unittest.TestCase):
    """Adds safe environment variable manipulation.

    Use this instead of manipulating :data:`os.environ` or calling
    :meth:`os.setenv` directly.  Failing to do so may cause strange
    test failures when environment variables leak between test
    cases.

    """

    def setUp(self):
        super().setUp()
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__saved_vars = {}

    def tearDown(self):
        """Automatically reset the environment during test clenaup."""
        super().tearDown()
        self.reset_environment()

    def reset_environment(self):
        """Undo changes to the environment."""
        for name, value in self.__saved_vars.items():
            os.environ.pop(name, None)
            if value is not None:
                os.environ[name] = value
        self.__saved_vars.clear()

    def setenv(self, name, value):
        """Set an environment variable.

        :param str name: names the environment variable to set
        :param str value: value to store in the environment

        """
        self.__logger.getChild('setenv').info('setting %s=%s', name, value)
        self.__saved_vars.setdefault(name, os.environ.get(name))
        os.environ[name] = value

    def unsetenv(self, name):
        """Clear an environment variable.

        :param str name: names the environment variable to clear

        """
        self.__logger.getChild('unsetenv').info('clearing %s', name)
        self.__saved_vars.setdefault(name, os.environ.get(name))
        os.environ.pop(name, None)
