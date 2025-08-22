# MOD Development Guidelines

## Overview

Game features can be modified without rebuilding the game from source code. This includes professions, monsters, NPCs, and more. You can see the changes by simply modifying the relevant files and running the game.

Most MOD creation is done by editing JSON files. A detailed review of all JSON files and their appropriate fields is available in [JSON/JSON_INFO.md](JSON/JSON_INFO.md).

## Basics

### Creating a Barebones MOD

A MOD is created by creating a folder within the `data/mods` directory of Cataclysm. The properties of the MOD are set by the `modinfo.json` file that exists within that folder. For Cataclysm to recognize the folder as a MOD, the `modinfo.json` file **must** exist within that folder.

### Modinfo.json

The modinfo.json file is a file that contains metadata for the MOD. Every MOD needs a `modinfo.json` file for Cataclysm to find it.
A barebones `modinfo.json` file looks like this:
```jsonc
[
  {
    "type": "MOD_INFO",
    "id": "Mod_ID",
    "name": "Mod's Display Name"
  }
]
```

This is the absolute minimum, but it is recommended to add `authors` (you!), `description`, and `category`. See below for possibilities.

### All MOD_INFO Fields

The following is a complete list of values supported by MOD_INFO:
```jsonc
[
  {
    "type": "MOD_INFO",                             // Required, you are making this!
    "id": "Mod_ID",                                 // Required, a unique ID for the MOD. Do not use the same ID as another MOD. Cannot contain the '#' character. The MOD ID must also be a valid folder path to support compatibility with other MODs.
    "name": "Mod's Display Name",                   // Required.
    "authors": [ "Me", "A really cool friend" ],    // Optional, but it is recommended to put your name. Multiple entries can be added.
    "description": "The best mod ever!",            // Optional
    "category": "graphical",                        // Optional, see the complete list of selectable values below.
                                                    // Categories are for informational purposes only, so don't worry if your MOD fits into multiple categories.
    "dependencies": [ "dda" ],                      // Optional. What other MODs are required for this MOD to function? If a MOD depends on another MOD to function correctly, by adding that MOD's `id` attribute to the array, Cataclysm will force that MOD to load before yours.
    "loading_images": [ "cool.png", "cool2.png" ], // Optional. File names of loading screen images that the MOD might have. Loading screens only exist in the graphical/"tiles" version. Only .png files are supported. The actual loading screen image is randomly selected from all MOD loading screens, including those with other loading screen MODs.
    "version": "1.3.bacon",                         // Optional. For informational purposes only. No version management system is provided, so what you write here is up to you. You can even name it after ice cream. However, it is recommended to use the `v1.0.0` format for version numbers. Version numbers consist of three parts: major, minor, and patch. Increment the major version when making incompatible changes. Increment the minor version when adding or modifying features. Increment the patch version when fixing bugs.
    "core": false,                                  // Optional, default is false. Core MODs are loaded before all others. Not supported for use in DDA.
    "obsolete": false,                              // Optional, default is false. Obsolete MODs are loaded for legacy saves, but cannot be used when starting a new world.
    "path": "my_mod_files/"                         // Optional, a relative directory from the location of modinfo.json. This directory is considered the actual directory of the MOD. For example, if modinfo.json is at C:\CDDA\my_mod\modinfo.json, the MOD files are considered to be at C:\CDDA\my_mod\my_mod_files\. Files such as C:\CDDA\my_mod\some_other_file.json are ignored because they are not within the specified directory.
  }
]
```

The `category` attribute indicates where the MOD will appear in the MOD selection menu. These are selectable categories, and examples selected from MODs that existed at the time this document was written. When writing a modinfo file, select the one that best suits your MOD.
 - `content` - A MOD that adds many things. Usually reserved for large MODs (e.g., core game files, Aftershock).
 - `total_conversion` - A MOD that fundamentally changes the game. Specifically, it is based on the premise that players should not use two total conversion MODs simultaneously. Therefore, they are not tested together. However, nothing prevents you from using more than two if the player wishes. (e.g., Dark Skies Above)
 - `items` - A MOD that adds new items or recipes to the game (e.g., More survival tools)
 - `creatures` - A MOD that adds new creatures or NPCs to the game (e.g., Modular turrets)
 - `misc_additions` - Other content additions to the game (e.g., Alternative map key, Crazy cataclysm)
 - `buildings` - New overmap locations and structures (e.g., National Guard Camp). This is also an available category if you want to blacklist buildings from spawning (e.g., No rail stations).
 - `vehicles` - New vehicles or vehicle parts (e.g., Tanks and other vehicles)
 - `rebalance` - A MOD designed to rebalance the game in some way (e.g., Safe autodocs).
 - `magical` - A MOD that adds something magic-related to the game (e.g., Necromancy)
 - `item_exclude` - A MOD that stops item spawning in the world (e.g., No survivor armor, No drugs)
 - `monster_exclude` - A MOD that stops spawning of specific monster species in the world (e.g., No fungal monsters, No monsters)
 - `graphical` - A MOD that adjusts game graphics in some way (e.g., Graphical overmap)

## Actually Adding Things to a MOD

Once you've created a basic MOD, you're ready to actually add something!

### File Structure

It is recommended to put additions for different categories into different JSON files. All JSON files that exist in the MOD folder or its subfolders will be detected and loaded by Cataclysm, but otherwise there are no restrictions on where to put what.

### JSON_INFO.md

It is worth reading [JSON/JSON_INFO.md](JSON/JSON_INFO.md) to get a comprehensive list of what you can do with these MODs. The rest of this document contains some examples that can be copy-pasted, but it is by no means comprehensive. Since the base game data is also defined in the same way as any MOD you write, looking at the game's JSON files (found in `data/json`) can also teach you a lot. If there is a problem with JSON syntax when attempting to load a game world, the game will spit out an error message and will not be able to load that game until the problem is fixed.

### Adding Scenarios

Scenarios are what the game uses to determine the general situation when creating a character. It determines where and when the character spawns in the world, and which professions can be used. It is also used to determine whether those professions have mutations at the start. The following is the JSON definition of the game's built-in `Large Building` scenario.
```jsonc
[
  {
    "type": "scenario",
    "id": "largebuilding",
    "name": "Large Building",
    "points": -2,
    "description": "Whether due to stubbornness, ignorance, or just plain bad luck, you missed the evacuation, and are stuck in a large building full of the risen dead.",
    "allowed_locs": [
      "mall_a_12",
      "mall_a_30",
      "apartments_con_tower_114",
      "apartments_con_tower_014",
      "apartments_con_tower_104",
      "apartments_con_tower_004",
      "hospital_1",
      "hospital_2",
      "hospital_3",
      "hospital_4",
      "hospital_5",
      "hospital_6",
      "hospital_7",
      "hospital_8",
      "hospital_9"
    ],
    "start_name": "In Large Building",
    "surround_groups": [ [ "GROUP_BLACK_ROAD", 70.0 ] ],
    "flags": [ "CITY_START", "LONE_START" ]
  }
]
```

### Adding Professions

Professions are character classes that can be selected at the start of the game. Professions can have traits, skills, items, and even pets! The following is the definition of a police officer profession:
```jsonc
[
  {
    "type": "profession",
    "id": "cop",
    "name": "Police Officer",
    "description": "Just a small-town deputy when you got the call, you were still ready to come to the rescue. Except that soon it was you who needed rescuing - you were lucky to escape with your life. Who's going to respect your authority when the government this badge represents might not even exist anymore?",
    "points": 2,
    "skills": [ { "level": 3, "name": "gun" }, { "level": 3, "name": "pistol" } ],
    "traits": [ "PROF_POLICE" ],
    "items": {
      "both": {
        "items": [ "pants_army", "socks", "badge_deputy", "police_belt", "boots", "whistle", "wristwatch" ],
        "entries": [
          { "group": "charged_cell_phone" },
          { "group": "charged_two_way_radio" },
          { "item": "postman_shirt", "variant": "sheriff" },
          { "item": "ear_plugs", "custom-flags": [ "no_auto_equip" ] },
          { "item": "usp_45", "ammo-item": "45_acp", "charges": 12, "container-item": "holster" },
          { "item": "legpouch_large", "contents-group": "army_mags_usp45" }
        ]
      },
      "male": [ "boxer_shorts" ],
      "female": [ "bra", "boy_shorts" ]
    }
  }
]
```

### Adding Items

For items, there is a lot you can do, and it varies slightly depending on the item category, so it is highly recommended to read the [JSON/JSON_INFO.md](JSON/JSON_INFO.md) file.
<!--The one I chose is the most basic item I found. Everything else does something.-->
```jsonc
[
  {
    "id": "family_photo",
    "type": "GENERIC",
    "//": "Unique mission item for the CITY_COP.",
    "category": "other",
    "name": "family photo",
    "description": "A photo of a smiling family on a camping trip.  One of the parents looks like a cleaner, happier version of the person you know.",
    "weight": "1 g",
    "volume": 0,
    "price": "8 USD",
    "material": [ "paper" ],
    "symbol": "*",
    "color": "light_gray"
  }
]
```

### Preventing Monster Spawning

This type of MOD is relatively simple but very useful. If you don't want to deal with a specific type of monster in the world, this is how you do it. You can create blacklists and whitelists to define allowed monsters individually, by species, or by category. To create these, you need the relevant identifiers. A monster's `id`, `species`, and `categories` can be found in the JSON definitions in `data/json/monsters/` of the core game.

The following is an excerpt from the `Mythos` MOD, showing how to blacklist monsters individually and by species. This prevents the spawning of all zombies, cyborgs, and robots, except for those specified by the `id` of fungal zombies.
```jsonc
[
  {
    "type": "MONSTER_BLACKLIST",
    "monsters": [
      "mon_zombie_fungus",
      "mon_boomer_fungus",
      "mon_zombie_child_fungus",
      "mon_zombie_gasbag_fungus",
      "mon_zombie_smoker_fungus",
      "mon_skeleton_fungus",
      "mon_skeleton_brute_fungus",
      "mon_skeleton_hulk_fungus",
      "mon_chud"
    ]
  },
  {
    "type": "MONSTER_BLACKLIST",
    "species": [ "ZOMBIE", "ROBOT", "CYBORG" ]
  }
]
```
The following is an example of how to blacklist monsters by category. In this case, all classic zombie types are removed from the game.
```jsonc
[
  {
    "type": "MONSTER_BLACKLIST",
    "categories": [ "CLASSIC" ]
  }
]
```
You can also define exclusions by combining blacklists and whitelists. Extending the previous example, this removes all classic zombie types but excludes zombie horses.
```jsonc
[
  {
    "type": "MONSTER_BLACKLIST",
    "categories": [ "CLASSIC" ]
  },
  {
    "type": "MONSTER_WHITELIST",
    "monsters": [
      "mon_zombie_horse"
    ]
  }
]
```
Alternatively, if you only want specific monsters or species to appear, you can define an exclusive whitelist. Note that this overrides the defined blacklist. The following example is from the `No Monsters` MOD, which prevents all monsters but excludes wildlife.
```jsonc
[
  {
    "type": "MONSTER_WHITELIST",
    "mode": "EXCLUSIVE",
    "categories": [ "WILDLIFE" ]
  }
]
```
You can also define a non-exclusive whitelist by itself, but these will only have a notable effect when combined with a blacklist or exclusive whitelist as above. This is still useful because these lists are combined across all active MODs, so you can include a list that guarantees the existence of a specific monster type, and even if other MODs try to disable them, it will still allow their spawning. For example, `Crazy Cataclysm` uses the following list to enable some monsters that the core game blacklists by default, and even if other MODs try to disable them, it will still allow their spawning.
```jsonc
[
  {
    "type": "MONSTER_WHITELIST",
    "monsters": [
      "mon_zombie_dancer",
      "mon_zombie_jackson",
      "mon_shia",
      "mon_bear_smoky",
      "mon_zombie_skeltal",
      "mon_zombie_skeltal_minion"
    ]
  }
]
```

### Preventing Location Spawning

<!--I'm not very satisfied with this section. Blacklisting things on the map varies depending on the type of thing you're blacklisting. Overmap specials are different from overmap extras, city buildings, and building groups.-->
Preventing the spawning of specific types of locations in the game becomes a bit more difficult depending on the type of thing you're targeting. Overmap buildings are either standard buildings or overmap specials. If you want to block things with specific flags from spawning, you can blacklist them in a very similar way to monsters. The following example is also from the `No Fungal Monsters` MOD, which stops the spawning of all fungal regions.
```jsonc
[
  {
    "type": "region_overlay",
    "regions": [ "all" ],
    "overmap_feature_flag_settings": { "blacklist": [ "FUNGAL" ] }
  }
]
```

If you want to blacklist overmap specials, you need to copy from their definition and manually set the `occurrences` attribute to `[ 0, 0 ]`.

Finally, if you are trying to blacklist things that spawn in cities, you can do so with a region overlay. The following example is used in the `No rail stations` MOD, which stops the spawning of railroad stations in cities. However, it does not stop the spawning of railroad station overmap specials.
```jsonc
[
  {
    "type": "region_overlay",
    "regions": [ "all" ],
    "city": { "houses": { "railroad_city": 0 } }
  }
]
```

### Disabling Specific Scenarios

`SCENARIO_BLACKLIST` is either a blacklist or a whitelist.
If it's a whitelist, it blacklists all scenarios except those specified.
Only one blacklist can be specified at a time - this applies to all JSON loaded in a specific game (all MODs + core game). It is not specific to your particular MOD.
The format is as follows:
```jsonc
[
  {
    "type": "SCENARIO_BLACKLIST",
    "subtype": "whitelist",
    "scenarios": [ "largebuilding" ]
  }
]
```
Valid values for `subtype` are `whitelist` and `blacklist`.
`scenarios` is an array of scenario IDs to blacklist or whitelist.

### Disabling Specific Professions or Hobbies

`profession_blacklist` is either a blacklist or a whitelist.
If it's a whitelist, only the specified professions/hobbies can be selected.
Only one blacklist can be specified at a time - this applies to all JSON loaded in a specific game (all MODs + core game). It is not specific to your particular MOD.
The format is as follows:
```jsonc
[
  {
    "type": "profession_blacklist",
    "subtype": "blacklist",
    "professions": [ "caffiend", "unemployed" ]
  }
]
```
Valid values for `subtype` are `whitelist` and `blacklist`.
`professions` is an array of profession/hobby IDs to blacklist or whitelist.

### Adding Dialog to Existing NPCs

Existing dialog cannot be edited, but you can add new responses to start new dialog and missions. The following is a practical example from DinoMod:

```jsonc
  {
    "type": "talk_topic",
    "id": "TALK_REFUGEE_BEGGAR_2_WEARING",
    "responses": [
      {
        "text": "Yes.  I ask because I noticed there are dinosaurs around.  Do you know anything about that?",
        "topic": "TALK_REFUGEE_BEGGAR_2_DINO2"
      }
    ]
  }
```
## Monster Status Adjustment

Monster status can be adjusted using the `monster_adjustment` JSON element.
```jsonc
  {
    "type": "monster_adjustment",
    "species": "ZOMBIE",
    "flag": { "name": "REVIVES", "value": false },
	  "stat": { "name": "speed", "modifier": 0.9 }
  }
```
Using this syntax, you can modify the following:
**stat**: `speed` and `hp` are supported. Modifier is a multiplier of the base speed or HP stat.
**flag**: Add or remove monster flags.
**special**: Currently only supports `nightvision`, giving the specified monster species equal night vision to day vision.

Currently, separate `monster_adjustment` entries are required to adjust multiple stats or flags.

## External Options

External options control global settings that are not suitable for region settings. `SHOW_MUTATION_SELECTOR` allows you to select mutations to acquire when mutating, and `ETERNAL_WEATHER` allows you to select always active weather types.
All available external options are located in `/core/external_options.json`, with comments explaining their purpose and DDA's values.
To change values in a MOD, you only need to define the same object as DDA's and change the values.

You can also override any source-defined option with an external option of the same name in the same way (e.g., if a player sets `AUTO_FEATURES` to false, but you create an external option that sets `AUTO_FEATURES` to true, when the player loads the MOD, the value will change to true).
**However, since this currently overrides the user's settings at save time, do not use it unless it is necessary for the MOD to function.**

## Important Notes on JSON Files

The following characters: `[ { , } ] : "` are *very* important when adding or modifying JSON files. If you want to include these characters in what you are working on (e.g., if you want to put quotes in an item description), you can "escape" them by placing a backslash before the relevant character. For example, if you want to include quotes in an item description, you can do the following:
```jsonc
...
"description": "This is a shirt that says \"I wanna kill ALL the zombies\" on the front.",
...
```

In the game, it will be displayed as:
`This is a shirt that says "I wanna kill ALL the zombies" on the front.`

Many editors have a feature to track `{ [` and `] }` to check if they are balanced (i.e., if there is a matching opposite), and these editors properly respect escaped characters. [Notepad++](https://notepad-plus-plus.org/) is a popular free editor on Windows that includes this feature. On Linux, there are many options, and you probably already have a preferred one🙂

### Things That Cannot Be MODded

Almost everything in this game can be MODded. Almost. This section is intended to show areas where MODding is not supported, in order to save time and headaches.

The Names folder and its contents (EN, etc.) were checked on 5/23/20.
Construction recipes. As of 7/4/22, a workaround has been confirmed to add requirements, and they can be MODded.