# Release notes

<!-- do not remove -->

## 0.1.1

This is a bugfix release.

### Bugs Squashed

- NSRDB download does not account for leap years ([#1](https://github.com/SarthakJariwala/nrel_dev_api/issues/1))
  - `download_nsrdb_data` does not account for leap year.

## 0.1.0

First release of `nrel_dev_api`

Access data and analysis services that NREL (National Renewable Energy Lab) provides using a python API.

With this first release, it supports (almost) all the solar endpoints.
Future releases will expand to cover other API endpoints such as wind, utility, building, etc.
