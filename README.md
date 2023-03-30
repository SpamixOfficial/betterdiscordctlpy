# betterdiscordctl Python edition

A Python edition of wrapper for BetterDiscord on Linux (Python allows to add Windows and macOS support in the future).

## Roadmap
- [x] `pre-commit` with `pylint` and other useful, generic inspections added
- [x] directory with developer stuff to set up the development environment
- [x] version info
- [x] help message
- [x] verbosity control
- [ ] logic for Linux ported from the original `sh` script:
  - [ ] BetterDiscord installation
  - [ ] BetterDiscord re-installation
  - [ ] BetterDiscord removal
  - [ ] `betterdiscordpy` self-upgrade
  - [ ] `flatpak` support
  - [ ] `snap` support
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
- [ ] macOS support:
  - [ ] BetterDiscord installation
  - [ ] BetterDiscord re-installation
  - [ ] BetterDiscord removal
  - [ ] `betterdiscordpy` self-upgrade

## Development
We use the [`pre-commit` tool](https://pre-commit.com/) as our linter. Its config file is [.pre-commit-config.yaml](./.pre-commit-config.yaml)

Python requirements can be found in the [requirements-dev.txt file](dev/requirements-dev.txt)

We have a shell script (currently for POSIX) that will set up the environment. Please, run:

```shell
dev/setup.sh
```

## Credits
### Inspiration
https://github.com/bb010g/betterdiscordctl: Initial idea & Linux implementation

### Python development
- [skelly37](https://github.com/skelly37)
- [SpamixOfficial](https://github.com/SpamixOfficial)
