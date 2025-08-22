# Git Workflow and Branching Strategy

## Overview

This document provides guidelines for the project's Git workflow and branching strategy.

## Branching Strategy

- The `main` branch holds code that is ready for release.
- The `develop` branch holds code that is under development.
- Feature development should be done in feature branches prefixed with `feature/`.
- Release preparation should be done in release branches prefixed with `release/`.
- Hotfixes should be done in hotfix branches prefixed with `hotfix/`.

## Commit Messages

- Commit messages should follow the Conventional Commits format.
- Commit messages should be written in English.
- One commit should represent one logical change unit.

## Pull Requests

- When feature development is complete, create a pull request.
- Pull requests should be merged after review by at least one other developer.
- The title and description of pull requests should clearly describe the changes.