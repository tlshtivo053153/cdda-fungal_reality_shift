# JSON Style Guidelines

## Overview

As with [CODE_STYLE.md](CODE_STYLE.md), the JSON styling policy should be updated when JSON is added or edited. Otherwise, it should be updated in relatively small chunks to avoid excessive disruption to development.

Since we couldn't find a suitable JSON styling tool, we created our own. It is located at `tools/format.cpp` and leverages `src/json.cpp` to parse and output JSON.
`json_formatter.cgi` is included in release builds and is already compiled. See [Format Tool](#format-tool).

## JSON Example

This example shows an overview of most styling features:

```jsonc
[
  {
    "type": "foo",
    "id": "example",
    "short_array": [ 1, 2, 3, 4, 5 ],
    "short_object": {
      "item_a": "a",
      "item_b": "b"
    },
    "long_array": [
      "a really long string to illustrate line wrapping, ",
      "which occurs if the line is longer than 120 characters"
    ],
    "nested_array": [
      [
        [ "item1", "value1" ],
        [ "item2", "value2" ],
        [ "item3", "value3" ],
        [ "item4", "value4" ],
        [ "item5", "value5" ],
        [ "item6", "value6" ]
      ]
    ]
  }
]
```

- Indentation is 2 spaces.
- All JSON delimiters except commas and colons are surrounded by whitespace (space or newline).
- Commas and colons are followed by whitespace.
- Object entries are always separated by newlines.
- Array entries are separated by newlines if the resulting array exceeds 120 characters (including indentation).
- Newlines occur after an opening brace, closing brace, or entry.

## MOD Development Best Practices

### File Structure

- It is recommended to separate MOD JSON files into different files for each feature.
  - Example: `items.json`, `monsters.json`, `professions.json`
- Each file should contain a comment at the beginning describing the content of the file.
  - Example: `// Item definitions`

### ID Naming

- It is recommended to prefix IDs with the MOD's prefix.
 - Example: `my_mod_item_01`, `my_mod_monster_01`

### Comments

- Include descriptive comments for complex logic or special settings.
- Comments use `//`.

### Inheritance

- Use the `copy-from` field when extending existing definitions.
- When using `copy-from`, clearly explain the changes in a comment.

## Format Tool

The format tool can be found as `json_formatter.exe` or `json_formatter.cgi` along with the release.
It can be built with `make style-json` or accessed at <http://dev.narc.ro/cataclysm/format.html>.
It is recommended to add the format tool location to your `PATH`.
Or place it in the Cataclysm-DDA root directory (if it doesn't already exist).

Using `make style-json` will format all files included in the JSON validation test. Or:

```sh
# Use git to filter JSON files with uncommitted changes (if there are no spaces in file or directory names).
git diff --name-only '*.json' | xargs -P 0 -L 1 json_formatter

# Use git to filter JSON files changed in the current branch.
git diff master --name-only '*.json' | xargs -P 0 -L 1 json_formatter

# Format by folder.
find path/to/desired/folder -name "*.json" -print0 | xargs -P 0 -0 -L 1 json_formatter
```

---

If you are using a Visual Studio solution, you can set up a command in Visual Studio to format all JSON in the project.

1. Build the JsonFormatter project (build the entire solution or just that project). This will create the `tools/format/json_formatter.exe` binary.
2. To automatically lint JSON, you need to define an MSBuild variable (similar to setting up ccache in the Visual Studio compile documentation).
   If set up correctly, when you try to build or run the solution, linting will be triggered, and linted files will be displayed in the `Output` and `Error List` windows (if any).
   An easy way to do this is to create a `Directory.Build.props` file in the root of the cataclysm project repository with the following content:

```xml
<Project>
  <PropertyGroup>
    <CDDA_POST_BUILD_JSON_LINT>true</CDDA_POST_BUILD_JSON_LINT>
  </PropertyGroup>
</Project>
```

3. To add an entry to manually run the JSON lint tool, go to `Tools` > `External Tools..` > `Add` and set it up as follows:
   - Title: `Lint all JSON`
   - Command: `C:\windows\system32\windowspowershell\v1.0\powershell.exe`
   - Arguments: `-file $(SolutionDir)\style-json.ps1`
   - Initial directory: `$(SolutionDir)`
   - Use Output window: *Check*

At this point, you can call the command using the menu (`Tools` > `Lint all JSON`) and check the execution results in the output window.
Furthermore, go to `Tools` > `Options` > `Environment` > `Keyboard`, search for a command containing `Tools.ExternalCommand`, select the one corresponding to the position of the command in the list (for the top item in the list, it would be `Tools.ExternalCommand1`), and assign a shortcut key.

### Visual Studio Code

If you install the recommended extensions, you will be able to access cdda-toys.cdda-json-formatter and automatically format JSON.