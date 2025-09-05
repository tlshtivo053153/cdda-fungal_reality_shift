# Dynamic EOC Implementation Plan

## 1. weighted_list_eocs の重複コード解消

### 現在の実装例 (brick_wall)
```json
{
  "type": "effect_on_condition",
  "id": "EOC_FRS_TRANSFORM_TERRAIN_FROM_BRICK_WALL",
  "effect": [
    {
      "u_location_variable": { "u_val": "transform_center" },
      "min_radius": 0,
      "max_radius": 0
    },
    {
      "weighted_list_eocs": [
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_WALL_FROM_BRICK", 1 ],
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_CONCRETE_FROM_BRICK", 1 ],
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_METAL_FROM_BRICK", 1 ],
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_FUNGUS_FROM_BRICK", 1 ],
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_PAPER_FROM_BRICK", 1 ],
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_LOG_FROM_BRICK", 1 ],
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_RESIN_FROM_BRICK", 1 ],
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_WOOD_FROM_BRICK", 1 ],
        [ "EOC_FRS_TRANSFORM_TERRAIN_TO_STRCONC_FROM_BRICK", 1 ]
      ]
    }
  ]
}
```

### 新しい実装
```json
{
  "type": "effect_on_condition",
  "id": "EOC_FRS_TRANSFORM_TERRAIN_FROM_BRICK_WALL",
  "effect": [
    {
      "u_location_variable": { "u_val": "transform_center" },
      "min_radius": 0,
      "max_radius": 0
    },
    {
      "set_string_var": "brick",
      "target_var": { "context_val": "source_material" }
    },
    {
      "set_string_var": [ "wall", "concrete", "metal", "fungus", "paper", "log", "resin", "wood", "strconc" ],
      "target_var": { "context_val": "target_material" }
    },
    {
      "set_string_var": "EOC_FRS_TRANSFORM_TERRAIN_TO_<context_val:target_material>_FROM_<context_val:source_material>",
      "target_var": { "context_val": "eoc_id" }
    },
    {
      "run_eocs": { "context_val": "eoc_id" }
    }
  ]
}
```

## 2. ter_furn_transform を呼び出す eoc の重複コード解消

### 現在の実装例 (brick_wall)
```json
{
  "type": "effect_on_condition",
  "id": "EOC_FRS_TRANSFORM_TERRAIN_TO_WALL_FROM_BRICK",
  "effect": [
    { "u_transform_radius": 20, "ter_furn_transform": "terrain_transform_frs_brick_to_wall", "target_var": { "u_val": "transform_center" } }
  ]
}
```

### 新しい実装
```json
{
  "type": "effect_on_condition",
  "id": "EOC_FRS_TRANSFORM_TERRAIN_TO_DYNAMIC_FROM_DYNAMIC",
  "effect": [
    {
      "u_transform_radius": 20,
      "ter_furn_transform": "terrain_transform_frs_<context_val:source_material>_to_<context_val:target_material>",
      "target_var": { "u_val": "transform_center" }
    }
  ]
}
```

Note: `source_material` と `target_material` は、ter_furn_transform のIDに合わせて小文字で定義されています。

## 3. 新しいEOCの定義

### ter_furn_transform を呼び出す EOC
```json
{
  "type": "effect_on_condition",
  "id": "EOC_FRS_TRANSFORM_TERRAIN_TO_DYNAMIC_FROM_DYNAMIC",
  "effect": [
    {
      "u_transform_radius": 20,
      "ter_furn_transform": "terrain_transform_frs_<context_val:source_material>_to_<context_val:target_material>",
      "target_var": { "u_val": "transform_center" }
    }
  ]
}
```

このEOCは、`source_material` と `target_material` の変数を使用して、ter_furn_transform のIDを動的に生成します。