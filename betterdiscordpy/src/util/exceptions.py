class BaseBetterDiscordPyException(Exception):
    def __str__(self) -> str:
        return f"ERROR: {self.messages}"


class InvalidVerbosityConfigurationException(BaseBetterDiscordPyException):
    def __init__(self) -> None:
        self.messages = "Cannot be both quiet and verbose"
