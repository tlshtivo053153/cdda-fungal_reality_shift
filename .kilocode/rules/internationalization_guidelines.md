# Internationalization (i18n) and Translation Guidelines

## Overview

This document provides guidelines for translation procedures and language file management.

## Language File Structure

- Place language files in the `lang/` directory.
- Each language has its own directory (e.g., `lang/en/`, `lang/ja/`).
- Language files should be written in JSON format.

## Translation Key Naming Convention

- Use snake_case for translation keys.
- Translation keys should be descriptive and clear in meaning.

## Translation Procedure

1. Use the English files in the `lang/en/` directory as a reference to create files for other languages.
2. When new translation keys are added to the English files, add them to the other language files as well.
3. It is recommended that native speakers perform translation work.

## Translation Review

- Translations should be merged after review by at least one other native speaker.
- It is recommended to conduct regular reviews to maintain translation quality.