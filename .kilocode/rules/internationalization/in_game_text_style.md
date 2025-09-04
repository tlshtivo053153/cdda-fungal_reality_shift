# In-Game Text Style Guidelines

## Overview

When adding or editing in-game text, please follow the rules below. These rules apply to default American English. For translations, follow the guidelines for the target language (if described in [/lang/notes/](../lang/notes)). These guidelines may differ from those described here.

## Style Rules

1. Use American English spelling.
   - Exception: Some character dialogues may use dialects other than American English. For example, Exodii/Rubik uses a combination of [Cockney dialect](https://en.wikipedia.org/wiki/Cockney) and [Early Modern English](https://en.wikipedia.org/wiki/Early_Modern_English).

2. Use double sentence spacing after sentences. This means placing two spaces after the period that ends a sentence. If the sentence is the last sentence in a text block, do not place a space after it.

3. Use second person perspective (e.g., "you").

4. Names of stats, traits/mutations, scenarios, professions, backgrounds, proficiencies, martial arts, and compact bionic modules (CBMs) should be written in title case. This means capitalizing every word except articles, prepositions, and conjunctions.

5. Names of items and entities that are proper nouns should also be written in title case.
   - This includes: Cataclysm, Discontinuity (an Aftershock event), Exodii, Marloss, Mycus, Autodoc, Kevlar, Nomex.
   - Custom currencies like "merch" should be written in lowercase unless the name contains a proper noun. For example, "Hubcoin" contains a proper noun, so it should be capitalized.

6. All other item and entity names should be written in all lowercase.

7. Use the serial comma (Oxford comma).

8. Use the ellipsis (…) instead of three dots (...). Instances of three periods should be replaced with the Unicode character dedicated to ellipses (U+2026). Details on usage:
   - Do not place a space before it, and place one space after it.
   - Since this character does not end a sentence, if you end a sentence with an ellipsis, place a period after the ellipsis (....).

9. There is no need to avoid brand names. They are within the scope of fair use. However, since CDDA-Earth is a parallel universe, non-existent brands can also be used.

10. Do not avoid using Unicode characters (including proper nouns, alphabets, and symbols such as ® and ™).

11. All descriptive text should follow sentence case. This means it should start with a capital letter and end with a period. This applies even for testing purposes (to prevent incorrect display in the debug menu).

## NPC Dialogue Condition Checking

When specifying condition checks in NPC dialogues:

1. When specifying stats, use the abbreviated form. Example: `[PER 10] I can see something weird.`. Example to avoid: `[PER 10+]` or `[PERCEPTION 10]`.

2. When specifying skills, use normal sentence case. Example: `[Tailoring 2] I can patch it up for you!`

3. When specifying traits, write them in all uppercase. Example: `[SWEET TOOTH] Do you have something more sugary than fruit?`

4. When specifying that an item is used (not consumed), write it as in the example: `[Use Stethoscope] Let's see if this one is still alive.`

5. When specifying an action without dialogue, write it as in the example: `[Push the button.]`