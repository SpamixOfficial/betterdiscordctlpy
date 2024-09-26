#!/usr/bin/env python3

import argparse
import logging
import os
import subprocess
import sys

try:
    from betterdiscordpy.src.commands import AVAILABLE_COMMANDS
    from betterdiscordpy.src.util import exceptions
except ImportError:
    from src.commands import AVAILABLE_COMMANDS
    from src.util import exceptions

APP_NAME: str = "betterdiscordpy"
VERSION: str = "1.0.0"
TRADITIONAL_LINUX_CONFIG_DIR: str = "~/.config/"


def getVerbosityLevel(arguments: argparse.Namespace) -> int:
    if arguments.verbose:  # pylint: disable=no-else-return
        if arguments.quiet:
            raise exceptions.InvalidVerbosityConfigurationException()
        return logging.DEBUG
    elif arguments.quiet:
        return logging.WARNING
    return logging.INFO


def initLogger(verbosity_level: int, message_format: str = "%(message)s") -> None:
    logging.basicConfig(format=message_format, level=verbosity_level)


def getLinuxConfigDir(installation_type: str) -> str:
    if installation_type == "traditional":  # pylint: disable=no-else-return
        return TRADITIONAL_LINUX_CONFIG_DIR
    elif installation_type == "snap":
        snap_user_data = os.getenv("SNAP_USER_DATA")
        return os.path.join(snap_user_data, "discord", ".config")
    elif installation_type == "flatpak":
        flatpak_bin = "/usr/bin/flatpak"
        discord_app_name = "com.discordapp.Discord"

        cmd = "echo $XDG_CONFIG_HOME"
        xdg_config = subprocess.run(
            [flatpak_bin, "run", "--command=sh", discord_app_name, "-c", cmd],
            stdout=subprocess.PIPE, text=True, env=os.environ, check=True,
        ).stdout.strip()
        if xdg_config:
            return xdg_config

        default_flatpak_config = f".var/app/{discord_app_name}/config"
        return os.path.join(os.getenv("HOME"), default_flatpak_config)


def getArgumentsParser() -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(description="Manage BetterDiscord installations on Linux")
    arg_parser.add_argument(
        "-V", "--version", action="store_true",
        help="display version info and exit",
    )
    arg_parser.add_argument(
        "command", choices=["status", "install", "reinstall", "uninstall", "self-upgrade"],
        nargs="?",
    )
    arg_parser.add_argument("-v", "--verbose", action="store_true", help="increase verbosity")
    arg_parser.add_argument("-q", "--quiet", action="store_true", help="decrease verbosity")
    arg_parser.add_argument(
        "-i", "--d-install", choices=["traditional", "flatpak", "snap"],
        help="Discord's installation type",
    )
    return arg_parser


if __name__ == "__main__":
    parser = getArgumentsParser()
    args = parser.parse_args()
    initLogger(verbosity_level=getVerbosityLevel(args))

    if args.version:
        print(f"{APP_NAME} {VERSION}")
        sys.exit(0)
    elif args.command:
        AVAILABLE_COMMANDS[args.command](args)
    else:
        parser.print_help()
