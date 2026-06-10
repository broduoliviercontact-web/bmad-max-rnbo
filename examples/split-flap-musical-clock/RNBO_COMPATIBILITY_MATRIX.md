# RNBO Compatibility Matrix — Split-Flap Musical Clock

## Classification des modules

| Module | Statut | Pourquoi | Décision v1 | Validation |
|---|---|---|---|---|
| transport_clock | Max-only | accès heure système, transport, UI | rester hors RNBO | manual Max test |
| event_scheduler | Unknown / partial | peut être simple mais dépend de la source temporelle | garder dans Max v1, migrer partiellement plus tard | needs test |
| visual_state_manager | Max/Web-only | manipule caractères, UI, état visuel | hors RNBO | manual UI test |
| jweb_bridge | Max-only/Web-only | communication avec navigateur embarqué | hors RNBO | jweb test |
| music_event_generator | RNBO-compatible / partial | peut devenir note/trigger logic simple | prototype Max puis port RNBO si stable | RNBO test |
| split_flap_engine | RNBO-compatible | moteur audio autonome | dans `rnbo~` | export test |
| audio_safety | RNBO-compatible + Max | gain final dans RNBO, meter/mute dans Max | doublon sécurité Max + RNBO | audio test |
| m4l_transport_sync | M4L-only | Live API / transport Live | phase ultérieure | M4L test |

## Objets/approches à garder hors RNBO

| Élément | Raison |
|---|---|
| `jweb` | UI navigateur embarquée Max, pas moteur audio |
| HTML/CSS/DOM | Web-only |
| lecture date/heure système complexe | mieux côté Max ou JS navigateur |
| `live.object`, `live.path` | M4L-only |
| debug console / print avancé | Max-only |

## Candidats RNBO

| Élément | Notes |
|---|---|
| synthèse simple | oscillateur + enveloppe + filtre |
| note trigger | message simple `note pitch velocity duration` |
| density | contrôle probabilité/triggers |
| root_note / scale_index | mapping musical simplifié |
| output_gain | paramètre obligatoire |
| tone_brightness | timbre exportable |

## Paramètres RNBO v1

| Param | Type | Range | Default | Notes |
|---|---|---|---|---|
| output_gain | float | 0..1 | 0.7 | gain final |
| root_note | int | 0..11 | 0 | C=0 |
| scale_index | int | 0..7 | 0 | gamme interne simple |
| density | float | 0..1 | 0.5 | densité musicale |
| swing_amount | float | 0..0.75 | 0 | optionnel v1 |
| tone_brightness | float | 0..1 | 0.5 | filtre/timbre |

## Règle v1

Le premier export RNBO doit être petit : un moteur sonore autonome et contrôlable, pas toute l'horloge.

```txt
Max/Web clock + split-flap UI
        ↓
messages simples
        ↓
RNBO sound engine
```
