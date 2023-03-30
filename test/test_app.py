import os
import subprocess
import unittest

from betterdiscordpy import betterdiscord


class TestApp(unittest.TestCase):
    def testVersion(self) -> None:
        print(os.getcwd())
        output = subprocess.run(
            ["python3", "betterdiscordpy/betterdiscord.py", "-V"], stdout=subprocess.PIPE, text=True,
            env=os.environ, check=True, ).stdout.strip()
        self.assertEqual(f"{betterdiscord.APP_NAME} {betterdiscord.VERSION}", output)

    # TODO test other commands


if __name__ == '__main__':
    unittest.main()
