# Patch Architecture — Split-Flap Musical Clock

## Vue globale

```txt
[clock source]
      ↓
[p.transport_clock]
      ↓
[p.event_scheduler]
      ↓
[p.visual_state_manager] → [jweb / web split-flap UI]
      ↓
[p.music_event_generator]
      ↓
[rnbo~ split_flap_engine]
      ↓
[live.gain~ / gain~ / dac~]
```

## Modules

| Module | Rôle | Couche | Fichier/sous-patcher |
|---|---|---|---|
| transport_clock | source temporelle : real clock / tempo / manual | Max-only | `p.transport_clock` |
| event_scheduler | transforme le temps en ticks musicaux | Max-only puis partiel RNBO | `p.event_scheduler` |
| visual_state_manager | calcule les caractères à afficher | Max/Web | `p.visual_state_manager` |
| jweb_bridge | communication Max ↔ UI HTML/JS | Max-only/Web | `p.jweb_bridge` |
| music_event_generator | transforme ticks/chiffres en notes/triggers | RNBO-compatible si simplifié | `p.music_event_generator` ou RNBO |
| split_flap_engine | moteur audio : synthèse, enveloppes, gain | RNBO-compatible | `rnbo~ split_flap_engine` |
| audio_safety | mute, gain, limiter simple | Max/RNBO | `p.audio_safety` |

## Message flow

```txt
clock_tick
  → current_time_dict
  → visual_digits_changed
  → flap_event_list
  → musical_trigger
  → rnbo message/param
```

## Signal flow

```txt
rnbo~ out L/R
  → gain stage
  → meter
  → dac~ / plugout~ / Web Audio destination
```

## Data flow

Les états visuels peuvent être représentés par un `dict` côté Max/Web :

```json
{
  "hours": "10",
  "minutes": "42",
  "seconds": "09",
  "changed": ["seconds_ones"],
  "tick": 1234
}
```

Les événements musicaux envoyés au moteur RNBO doivent rester simples :

```txt
note 60 0.8 120
trigger 1
param density 0.5
param root_note 0
```

## Boundary RNBO

À mettre dans RNBO :

- synthèse ;
- enveloppes ;
- filtre/timbre ;
- gain final ;
- mapping simple note → son ;
- density/swing si besoin audio-accurate.

À garder hors RNBO :

- jweb ;
- HTML/CSS split-flap ;
- lecture heure système ;
- debug console ;
- Max UI avancée ;
- Live API.

## Architecture web cible

```txt
web/src/App.jsx
web/src/SplitFlapDisplay.jsx
web/src/rnbo-loader.js
web/src/clock-engine.js
web/src/style.css
export/rnbo/patch.export.json
```

## Risques

| Risque | Solution |
|---|---|
| UI trop liée au moteur audio | définir une API événementielle simple |
| RNBO non exportable | isoler seulement le DSP dans `rnbo~` |
| audio trop fort | gain final + panic/mute |
| timing instable | séparer horloge visuelle et triggers audio |
| jweb différent du navigateur final | garder le code web portable |
