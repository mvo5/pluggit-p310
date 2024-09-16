import unittest
import unittest.mock

from . pluggit_p310 import (
    set_time,
)


class TestSetTime(unittest.TestCase):

    def test_setTime(self, all=1):
        mockModBus = unittest.mock.MagicMock()
        setTime(mockModBus)
        mockModBus.write_registers.assert_called()


if __name__ == '__main__':
    unittest.main()
