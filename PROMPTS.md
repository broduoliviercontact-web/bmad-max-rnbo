# Prompts

## Max Architect

```txt
Utilise agents/max-architect.md.
Conçois l'architecture globale de ce projet Max/MSP.
Sépare UI, logique, audio, données et boundary RNBO.
Appuie-toi sur le corpus local Cycling '74 dans docs/cycling74-userguide.
Produis :
- une vue globale ;
- la liste des modules ;
- les flux de données ;
- les flux audio ;
- la boundary RNBO ;
- les fichiers à créer ;
- les risques.
```

## RNBO Specialist

```txt
Utilise agents/rnbo-specialist.md.
Analyse ce patch ou ce plan de patch.
Détermine ce qui peut entrer dans rnbo~, quels paramètres exposer et ce qui doit rester hors RNBO.
Appuie-toi sur le corpus local Cycling '74 dans docs/cycling74-userguide.
Produis :
- RNBO_COMPATIBILITY_MATRIX.md ;
- RNBO_PARAMETERS.md ;
- WEB_EXPORT_PLAN.md.
```

## Patch Critic

```txt
Utilise agents/patch-critic.md.
Audite ce patch Max/MSP avant validation.
Détecte blockers, warnings, problèmes d'ordre d'exécution, fan-out sans trigger, dépendances fragiles, risques audio et problèmes de boundary RNBO.
Appuie-toi sur le corpus local Cycling '74 dans docs/cycling74-userguide.
Produis :
- PATCH_AUDIT_REPORT.md ;
- PATCH_FIX_PLAN.md.
```

## Web Export Engineer

```txt
Utilise agents/web-export-engineer.md.
Prépare l'intégration Web Audio d'un export RNBO.
Crée le plan de chargement de export/rnbo/patch.export.json, la gestion de AudioContext et le mapping des paramètres.
Appuie-toi sur le corpus local Cycling '74 dans docs/cycling74-userguide.
Produis :
- WEB_EXPORT_PLAN.md ;
- web/src/rnbo-loader.js ;
- web/src/App.jsx ;
- README web.
```

## Documentation Agent

```txt
Agis comme un Documentation Agent pour ce repo Max/RNBO.
Lis README.md, BMAD_MAX_AGENT_BRIEF.md, agents/, workflows/, templates/ et les docs du projet.
Synthétise ce qui manque, clarifie les étapes d'usage et rédige une documentation concise orientée production.
Le runtime cible est Claude avec modèles Ollama Cloud.
Référence le corpus local Cycling '74 situé dans docs/cycling74-userguide sans le modifier.
Produis ou mets à jour :
- README.md ;
- INSTALL.md ;
- USAGE.md ;
- TROUBLESHOOTING.md si nécessaire.
```
