# Documentation Style Guidelines for Effect Usage

## Overview

This document provides style guidelines for documenting the usage of effect definitions in project documentation.

## Effect Usage Documentation

### `effect_on_conditions` vs `consumption_effect_on_conditions`

- Explain the difference between `effect_on_conditions` and `consumption_effect_on_conditions`.
- `effect_on_conditions` is used for general item usage effects.
- `consumption_effect_on_conditions` is specifically for effects that occur when comestible items are consumed.

### Usage Examples

- Provide clear examples of how to use `effect_on_conditions` and `consumption_effect_on_conditions`.
- Include code snippets and explanations for each example.

### Best Practices

- Always use `consumption_effect_on_conditions` for comestible items.
- Ensure that all effect definitions referenced in `consumption_effect_on_conditions` exist.
- Document the purpose and behavior of each effect clearly.
- Refer to bundled MODs like Magiclysm and MindOverMatter for examples of how to use `consumption_effect_on_conditions` effectively.

## Document Structure

1. **Title**: Give the document a title that clearly indicates its purpose.
2. **Overview**: Briefly explain the purpose and scope of the document.
3. **Table of Contents**: Provide a table of contents for long documents.
4. **Body**: Organize information logically and describe it clearly.
5. **Conclusion**: Summarize the key points of the document.

## Style Guide

### Language and Style

- Use clear and concise words.
- Define technical terms appropriately.
- Maintain a consistent style.
- It is recommended to keep paragraphs short for easy understanding by readers.
- Lines should not exceed 120 characters. If a line exceeds 120 characters, it should be wrapped to the next line.

### Headings

- Structure headings hierarchically.
- Give each section an appropriate heading.
- Heading levels are specified as `#` (H1), `##` (H2), `###` (H3)...

### Code and Examples

- Format code blocks and examples appropriately when provided.
- Enable syntax highlighting by specifying the language for code blocks (e.g., ```cpp).
- Examples help illustrate actual usage.

### Links

- Provide links to relevant documents or external resources.
- Link text should indicate the content of the destination.

### Lists

- Use bulleted lists or numbered lists to organize information.
- Keep list items concise and use a consistent format.

### Commit Messages

Follow Conventional Commits format:

#### Format
`type: subject`

#### Types
- `feat`: Adding a new feature
- `fix`: Bug fix
- `docs`: Documentation only changes
- `style`: Code formatting changes (no functional changes)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Changes to build process or auxiliary tools

#### Commit Rules
- Commit messages must be in English.
- One commit = one logical change unit
- When ready to commit, provide copy-pasteable commands:
  ```sh
  git add .
  git commit -m "feat: add user registration API endpoint"
  ```

## Document Maintenance

- Review documents regularly and update them as needed.
- Update related documents when changes occur.
- Remove or correct outdated or incorrect information.

## Review and Approval

- Documents should be reviewed by other team members.
- Reviews are important to verify the accuracy, clarity, and consistency of the content.