import argparse
import logging
import os
import unittest

from betterdiscordpy import betterdiscord
from betterdiscordpy.src.util import exceptions


class TestMainFunctions(unittest.TestCase):
    def testVerbosityLevelGetter(self) -> None:
        self.assertRaises(
            exceptions.InvalidVerbosityConfigurationException, betterdiscord.getVerbosityLevel,
            argparse.Namespace(quiet=True, verbose=True),
        )
        self.assertEqual(
            logging.WARNING,
            betterdiscord.getVerbosityLevel(argparse.Namespace(quiet=True, verbose=False)),
        )
        self.assertEqual(
            logging.DEBUG,
            betterdiscord.getVerbosityLevel(argparse.Namespace(quiet=False, verbose=True)),
        )
        self.assertEqual(
            logging.INFO,
            betterdiscord.getVerbosityLevel(argparse.Namespace(quiet=False, verbose=False)),
        )

    def testConfigDirGetter(self) -> None:
        self.assertRaises(
            exceptions.InvalidInstallTypeException, betterdiscord.getLinuxConfigDir,
            "I don't exist",
        )
        self.assertEqual(
            betterdiscord.TRADITIONAL_LINUX_CONFIG_DIR,
            betterdiscord.getLinuxConfigDir("traditional"),
        )

        os.environ["SNAP_USER_DATA"] = "dummy"
        self.assertEqual(
            os.path.join("dummy", "discord", ".config"),
            betterdiscord.getLinuxConfigDir("snap"),
        )
        os.environ["SNAP_USER_DATA"] = ""

        # TODO test flatpak one


if __name__ == '__main__':
    unittest.main()
