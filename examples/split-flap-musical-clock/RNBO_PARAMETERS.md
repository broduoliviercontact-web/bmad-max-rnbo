# RNBO Parameters — Split-Flap Musical Clock

## Paramètres audio/musique

| Param | Type | Range | Default | Unit | Automation | Description |
|---|---|---|---|---|---|---|
| output_gain | float | 0..1 | 0.7 | linear | yes | gain final sécurisé |
| root_note | int | 0..11 | 0 | semitone | yes | fondamentale de la gamme |
| scale_index | int | 0..7 | 0 | index | yes | choix de gamme interne |
| density | float | 0..1 | 0.5 | probability | yes | probabilité de déclenchement |
| swing_amount | float | 0..0.75 | 0 | ratio | yes | décalage rythmique optionnel |
| tone_brightness | float | 0..1 | 0.5 | normalized | yes | contrôle filtre/timbre |
| decay_time | float | 0.02..4 | 0.35 | seconds | yes | durée d'enveloppe |
| reverb_mix | float | 0..1 | 0.15 | normalized | yes | ambiance si disponible |

## Messages événementiels

| Message | Arguments | Description |
|---|---|---|
| `note` | `pitch velocity duration_ms` | déclenche une note |
| `tick` | `index intensity` | déclenche un tick musical |
| `panic` | none | coupe les sons |
| `set_scale` | `scale_index` | change la gamme |

## Exemple de messages Max → RNBO

```txt
note 60 0.8 120
tick 42 0.5
panic
```

## Mapping proposé chiffre → musique

| Source visuelle | Mapping musical |
|---|---|
| seconde unités | note courte |
| seconde dizaines | percussion douce |
| minute unités | note plus longue |
| minute dizaines | accord ou basse |
| heure | changement de texture |

## Presets v1

| Preset | Description |
|---|---|
| minimal_clock | ticks doux, faible densité |
| melodic_clock | notes pentatoniques, density moyenne |
| percussive_clock | ticks courts et rythmiques |
| ambient_clock | decay long, brightness faible |
