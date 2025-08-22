# Testing Procedure Guidelines

## Overview

When making changes that require contributions or other testing, please ensure that the changes work as expected. Our tests already cover many issues, but non-trivial changes require in-game testing. Typo fixes usually do not need to be tested.

## Style

[Manual of Style](MANUAL_OF_STYLE.md) applies to all proposed changes, so please read it first.

For JSON changes, please read [JSON/JSON_STYLE.md](JSON/JSON_STYLE.md).

All release builds include a pre-compiled `json_formatter.cgi`, which is a handy tool that automatically formats JSON files to the project's standards.

## Applying Changes Locally

For JSON-only changes (which make up the majority of contributions), a very simple method is to place the Cataclysm executable in the git repository.
This will automatically use the modified paths to load resources.
In more advanced situations, there are command-line parameters like `--datadir`, which can be specified to the git repository.
See `--help` for details.

Make sure to use the latest version of Cataclysm and ensure that the git revision matches the version of the Cataclysm executable to avoid conflicts with other people's JSON processing code changes.

When you return to the main menu and reload the save, most JSON files will be reloaded. After changes, you can choose to either restart Cataclysm or reload the save, whichever is more convenient.

## Using the Debug Menu

**Tip: If you name your character "Debug" (or something that starts with Debug), the game will automatically disable achievements and will no longer display the message "The debug menu does not help you play the game well."**

The debug menu is a powerful and useful tool. If you debug frequently, consider binding it globally to a key like F12.
Different tests are needed depending on the situation, so tests that tweak EOCs will require different tests than those that add item qualities.

### Items

You can summon any item with *Spawning > Spawn item*.
This menu is very intuitive. If an item name ends with a yellow `(S)`, it means the item's description is variable and is manipulated by snippets (hence the `(S)`). You can choose which snippet to apply.
Gray `(V)` has a similar meaning, but this is a variant that changes not only the description but also other things. Currently, these cannot be selected from the debug menu and are randomized.

### Map Generation

Many options in the `Map` part of the debug menu are self-explanatory.

However, *Map editor* and *Overmap editor* are particularly interesting, but may not be as intuitive as other options.

*Map editor* allows you to modify small amounts of terrain or apply different overmap terrain without touching the ID.

*Overmap editor* is useful mainly for spawning buildings and other special things.
To spawn buildings or other things that occupy multiple overmap tiles, type `s` to spawn a special.
Spawning individual overmap terrain is usually not used and is not very useful in that sense.

When spawning overmap specials, make sure to spawn them only in non-highlighted areas. Otherwise, they will not be applied.

### Monsters

You can spawn individual monsters or swarms of monsters with *Spawning > Spawn monster*.
This is very useful for testing monster factions, combat behavior, and more.
Unfortunately, there is currently no way to spawn monster groups (`mongroup`).

For more advanced playtesting, use the loadouts from the Standard Combat Testing Mod (included in the Misc category of built-in MODs) and document the results in the PR's testing section.

Important testing tips:
 - Spawned and saved monsters will always remain the same even if you modify the underlying monster definition. Always use newly spawned monsters!
 - Evolution, growth, and breeding occur when monsters are loaded, so the test procedure is as follows: Spawn monster -> Teleport to unload -> Teleport to load and start timer -> Teleport to unload -> Advance time in debug menu -> Teleport back.
 - If you enable the debug mode monster filter, you can examine monsters with `x` and get additional information with `e`.

## Automated Testing and CI/CD

### Unit Tests

- Please include unit tests for new features or modified features whenever possible.
- Unit tests are placed in the `tests/` directory and written using the [Catch2](https://github.com/catchorg/Catch2) framework.
- Tests can be run by executing the `tests/cata_test` executable.

### Continuous Integration (CI)

- All pull requests are automatically tested by the CI system.
- CI tests include code style checks, compilation tests, and unit tests.
- It is recommended to run tests equivalent to CI tests locally before submitting a pull request.

### Test Best Practices

- Tests should focus on specific features or bug fixes.
- Tests should be as independent as possible (one test should not depend on the results of another test).
- Test preconditions should be clearly documented, and comments should be added as needed.
- If a test fails, make sure the reason is clear.