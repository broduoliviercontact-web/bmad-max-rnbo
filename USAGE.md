# Usage

## Environnement cible

Ce starter est prévu pour un workflow Claude + modèles Ollama Cloud, avec Max/MSP, RNBO et export Web Audio.

## Exemple 1 — créer un projet RNBO web

```txt
Utilise workflows/create-rnbo-web-export.md.
Crée un projet appelé split-flap-musical-clock.
Sépare les couches Max-only, RNBO-compatible, Web-exportable et M4L-specific.
Remplis PROJECT_BRIEF.md, PATCH_PRD.md, PATCH_ARCHITECTURE.md et RNBO_COMPATIBILITY_MATRIX.md.
```

## Exemple 2 — auditer un patch Max

```txt
Utilise workflows/audit-maxpat.md.
Analyse patches/mon-patch.maxpat.
Produit PATCH_AUDIT_REPORT.md avec blockers, warnings et suggestions.
```

## Exemple 3 — préparer un export web

```txt
Utilise agents/rnbo-specialist.md et agents/web-export-engineer.md.
Prépare export/rnbo/patch.export.json et web/src/rnbo-loader.js.
```

## Variantes utiles

### Démarrer l'architecture d'un patch

```txt
Utilise agents/max-architect.md.
Propose l'architecture d'un patch Max/MSP pour [nom du projet].
Sépare interface, logique, audio, données et boundary RNBO.
Produit PATCH_ARCHITECTURE.md et RNBO_COMPATIBILITY_MATRIX.md.
```

### Vérifier une compatibilité RNBO

```txt
Utilise agents/rnbo-specialist.md.
Passe en revue patches/[nom].maxpat.
Classe chaque module en Max-only, RNBO-compatible, Web-exportable ou M4L-specific.
Signale les remplacements RNBO-safe.
```

### Préparer un plan d'implémentation web

```txt
Utilise agents/web-export-engineer.md.
Prépare un plan Vite ou React minimal pour charger export/rnbo/patch.export.json,
gérer AudioContext et exposer les paramètres clés dans web/src/rnbo-loader.js.
```

### Faire un audit avant export

```txt
Utilise agents/patch-critic.md.
Inspecte patches/[nom].maxpat avant export RNBO.
Vérifie fan-out, trigger, ordre d'exécution, sécurité audio, dépendances et boundary RNBO.
```
