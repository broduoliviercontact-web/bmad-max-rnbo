# Split-Flap Musical Clock

Exemple v1 pour **BMAD-MAX-RNBO**.

Objectif : créer une horloge musicale avec affichage **split-flap** animé, contrôlable dans Max/MSP, avec un moteur musical/audio isolé dans `rnbo~` pour préparer un export Web Audio.

## Principe

Le projet est volontairement séparé en couches :

```txt
Max-only            → orchestration, tests, jweb, debug, interaction locale
RNBO-compatible     → moteur musical/audio exportable
Web-exportable      → interface HTML/CSS/JS ou React/Vite
M4L-specific        → optionnel : synchro Ableton Live, automation, device Live
```

## Documents de l'exemple

```txt
PROJECT_BRIEF.md
PATCH_PRD.md
PATCH_ARCHITECTURE.md
RNBO_COMPATIBILITY_MATRIX.md
RNBO_PARAMETERS.md
WEB_EXPORT_PLAN.md
PATCH_AUDIT_REPORT.md
```

## Architecture courte

```txt
[clock source]
      ↓
[p.transport_clock]
      ↓
[p.event_scheduler]
      ↓
[p.visual_state_manager] → [jweb / web UI split-flap]
      ↓
[p.music_event_generator]
      ↓
[rnbo~ split_flap_engine]
      ↓
[audio out / web audio]
```

## Intention

Ce projet sert de démonstration pour montrer comment BMAD-MAX-RNBO transforme une idée visuelle et musicale en projet propre : brief, PRD, architecture, séparation RNBO, paramètres, export web et audit.

## Prochaine étape technique

Créer un premier patch minimal :

```txt
split-flap-musical-clock.maxpat
split-flap-engine.rnbopat ou rnbo~ dans le patch principal
```

Le patch minimal doit seulement faire :

1. afficher un tick de seconde ;
2. envoyer un événement `tick` ;
3. déclencher une note dans RNBO ;
4. contrôler `output_gain`, `density`, `root_note` ;
5. offrir un bouton `panic`.
