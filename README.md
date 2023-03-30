# betterdiscordpy

A Python wrapper for [BetterDiscord](https://betterdiscord.app/) on Linux (Windows and macOS support planned in the future).

## TODO
### Roadmap
- [x] `pre-commit` with `pylint` and other useful, generic inspections added
- [x] directory with developer stuff to set up the development environment
- [x] version info
- [x] help message
- [x] verbosity control
- [ ] logic for Linux ported from [the original `sh` script](https://github.com/bb010g/betterdiscordctl/blob/master/betterdiscordctl):
  - [ ] BetterDiscord installation
  - [ ] BetterDiscord re-installation
  - [ ] BetterDiscord removal
  - [ ] `betterdiscordpy` self-upgrade
  - [ ] `flatpak` support
  - [ ] `snap` support
  - [ ] [`betterdiscordctl`](./betterdiscordctl) removed from the repository
  - [ ] Binary release ([`pyinstaller`](https://github.com/pyinstaller/pyinstaller) or something)
- [ ] flavors, remotes and other optional flags
- [ ] documentation update with options, example usage, installation, etc...
- [ ] good enough set of tests
- [ ] CI on GitHub Actions
- [ ] Pull Request, issues etc. templates
- [ ] Windows support:
  - [ ] BetterDiscord installation
  - [ ] BetterDiscord re-installation
  - [ ] BetterDiscord removal
  - [ ] `betterdiscordpy` self-upgrade
  - [ ] Binary release ([`pyinstaller`](https://github.com/pyinstaller/pyinstaller) or something)
- [ ] macOS support:
  - [ ] BetterDiscord installation
  - [ ] BetterDiscord re-installation
  - [ ] BetterDiscord removal
  - [ ] `betterdiscordpy` self-upgrade
  - [ ] Binary release ([`pyinstaller`](https://github.com/pyinstaller/pyinstaller) or something)

## Technical debt
- [ ] `try-except` workaround in imports is handled in a less dirty way

## Development
### Conventions and setting up the development environment
We use the [`pre-commit` tool](https://pre-commit.com/) as our linter. Its config file is [.pre-commit-config.yaml](./.pre-commit-config.yaml)

Python requirements can be found in the [requirements-dev.txt file](dev/requirements-dev.txt)

We have a shell script (currently for POSIX) that will set up the environment. Please, run:

```shell
dev/setup.sh
```

### Testing
Tests work in assumption that the working directory is the repository's root. To run all tests use [run_all_tests.sh](dev/run_all_tests.sh):

```shell
dev/run_all_tests.sh
```

## Credits
### Inspiration
https://github.com/bb010g/betterdiscordctl: Initial idea & Linux implementation

### Python development
- [skelly37](https://github.com/skelly37)
- [SpamixOfficial](https://github.com/SpamixOfficial)
