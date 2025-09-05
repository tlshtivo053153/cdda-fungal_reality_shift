# set_string_var parse_tags Setting

## Overview

When using `set_string_var` to set a variable, if the variable contains tags such as `<context_val:...>`, you must set `"parse_tags": true`.

## Rule

- When using `set_string_var` with tags such as `<context_val:...>`, you must always set `"parse_tags": true`.
- If you forget to set `parse_tags`, the variable expansion will not be performed correctly, and unintended behavior may occur.

## Example

```json
{
  "set_string_var": [ "brick", "concrete", "metal", "fungus", "paper", "log", "resin", "wood", "strconc", "wall" ],
  "target_var": { "context_val": "source_material" },
  "parse_tags": true
}
```

## Related Task

- [Conduct a detailed review of the task implementation process and results, perform an objective and honest self-evaluation, and based on that evaluation, propose new rules to be added to .kilocode/rules or improvements to existing rules with concrete examples. The proposed rule ideas should contribute to quality improvement, efficiency, and risk avoidance in future similar tasks.](#)