# Changelog for `fungal reality shift`

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),

## Unreleased

## 1.3.0 - 2025-09-15

### Added
- Add tileset generation tool and source images
- Add tileset generation with dependency check to build script
- Add removal of existing ZIP file before building
- Add 'looks_like' property to fungal spore and liquid fuel items

### Changed
- Add python dependencies installation to release workflow
- Add execute permissions to tool scripts

## 1.2.0 - 2025-09-09

### Added
- Portal material support to wall terrain transformations
- Internationalization (i18n) support and build tools
- Terrain transformation reference check script
- Portal wall and monster summoning feature
- Mutual transformation between gold wall and chocolate wall
- Transformation support for gold and chocolate walls
- New EOC ID naming convention compliance

### Fixed
- Missing reverse terrain transformation definitions and JSON syntax errors
- Invalid ter_furn_transform ID errors
- Terrain transformation target for strconc to concrete wall
- Portal wall terrain ID reference in portal_wall_check.json
- Missing terrain_transform_frs_strconc_to_concrete ID

### Changed
- Clarified inconsistent reference messages in check_terrain_transform_references.py
- Renamed portal wall terrain ID from t_portal_wall to t_wall_portal
- Updated liquid terrain names to be more descriptive
- Restructured terrain files and integrated portal wall definition
- Increased veggy_tainted requirement for fungal spore creation
- Simplified portal wall monster spawn logic and changed to fungaloid
- Resolved code duplication caused by terrain transformation EOCs
- Classified files in terrain_transformation directory into liquid and wall
- Separated ter_furn_transform and EOC definitions into dedicated directories

### Documentation
- Added CHANGELOG.md and removed changelog section from README.md
- Added rules for bulk file editing and terrain transformation templates
- Improved efficient tool selection guidelines
- Added rules for set_string_var parse_tags and ter_furn_transform variable call
- Added new rules for task execution improvement

### Chore
- Added timeout-minutes to release workflow
- Added GitHub release workflow
- Updated .gitignore to exclude zip archives
- Removed obsolete dynamic EOC implementation plan
- Updated mod author information

## 1.1.0 - 2025-09-05

### Added
- Chocolate-themed items
- Updated file structure

## 1.0.0 - 2025-08-24

### Added
- Initial release