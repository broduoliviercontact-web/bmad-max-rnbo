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

## Documents

```txt
PROJECT_BRIEF.md
PATCH_PRD.md
PATCH_ARCHITECTURE.md
RNBO_COMPATIBILITY_MATRIX.md
WEB_EXPORT_PLAN.md
```

## Architecture courte

```txt
[clock source]
      ↓
[split-flap state manager] → [jweb / web UI]
      ↓
[musical event generator]
      ↓
[rnbo~ audio engine]
      ↓
[audio out / web audio]
```

## Intention

Ce projet sert de démonstration pour montrer comment BMAD-MAX-RNBO transforme une idée visuelle et musicale en projet propre : brief, PRD, architecture, séparation RNBO, export web et audit.
