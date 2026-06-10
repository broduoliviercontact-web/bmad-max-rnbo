# Retrieval Rules

## Principe

Avant toute décision technique Max/MSP, RNBO, M4L, Gen, Jitter ou Web Audio, l'agent doit chercher dans le corpus local Cycling '74.

## Sources prioritaires

```txt
docs/cycling74-userguide/INDEX.md
docs/cycling74-userguide/manifest.json
docs/cycling74-userguide/pages/
```

## Mapping rapide

| Sujet | Pages à consulter |
|---|---|
| RNBO | rnbo, param_connect, parameter_mode, snapshots |
| Gen | gen overview, gen expr, gen~ operators |
| Patching | patching, patching_mechanics, patch_cords, objects |
| Timing | scheduler, transport, time_value_syntax, sample_accurate_messages |
| M4L | m4l overview, live_api, live_parameters, live_timing |
| UI | styles, color_palette, dynamic_colors, bpatchers |
| Web/jweb | web_browser, javascript, jweb |
| Debug | debugging_and_probing, error_messages, max_console |
| MIDI/OSC | midi, OSC, mapping |
| Jitter | jitter graphics_processing, matrix, textures, video |

## Règles

- Ne pas copier longuement la doc.
- Résumer en décisions de patching.
- Citer le fichier ou l'URL source si un rapport est produit.
- Croiser les détails objets avec la base Taylor Brook si disponible.
- En cas de doute, marquer `needs manual Max validation`.
