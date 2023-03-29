import logging
import os
import subprocess
import unittest

import betterdiscordpy


class AppTest(unittest.TestCase):
    def setUp(self) -> None:
        if os.getcwd().endswith("test"):
            os.chdir("../")

    def tearDown(self) -> None:
        if not os.getcwd().endswith("test"):
            os.chdir("test")

    def testVersion(self) -> None:
        output = subprocess.run(
            ["python3", "betterdiscordpy.py", "-V"], stdout=subprocess.PIPE, text=True,
            env=os.environ, check=True, ).stdout.strip()
        self.assertEqual(f"{betterdiscordpy.APP_NAME} {betterdiscordpy.VERSION}", output)

    # TODO test other commands


if __name__ == '__main__':
    unittest.main()
