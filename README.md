# BMAD-MAX-RNBO

Méthode agentique pour concevoir, auditer, documenter et exporter des projets Max/MSP, RNBO, Max for Live, Gen, Jitter et Web Audio.

## Objectif

Transformer une idée musicale ou interactive en projet structuré :

```txt
idée → brief → PRD → architecture Max → boundary RNBO → implémentation → audit → export web → documentation
```

## Principe

BMAD-MAX-RNBO ne remplace pas Max/MSP.  
Il organise le travail des agents autour de règles claires :

- utiliser la documentation locale Cycling '74 avant de proposer une solution ;
- séparer les couches Max-only, RNBO-compatible, M4L-specific et Web-exportable ;
- générer ou modifier les `.maxpat` avec une API de patching quand c'est possible ;
- auditer les patches avec des règles Max/RNBO ;
- produire une documentation lisible pour humain et agent.

## Structure

```txt
agents/       rôles spécialisés
workflows/    procédures de travail
templates/    modèles de documents projet
checklists/   listes de contrôle
knowledge/    règles de retrieval, RNBO, audit, naming
scripts/      scripts Python de scaffold/audit
examples/     exemples de projets
docs/         corpus local Cycling '74 User Guide
```

## Runtime recommandé

- Claude comme agent principal.
- Modèles Ollama Cloud pour le raisonnement et le code.
- Max 9 + RNBO pour validation audio/visuelle.
- Taylor Brook MAX-MSP_CC_Framework / Patcher API quand disponible.
- React/Vite pour les exports web.

## Démarrage rapide

1. Copier le corpus Cycling '74 dans :

```txt
docs/cycling74-userguide/
```

2. Copier `BMAD_MAX_AGENT_BRIEF.md` à la racine du projet.

3. Lancer un workflow :

```txt
workflows/create-rnbo-web-export.md
```

4. Produire les documents projet :

```txt
templates/PROJECT_BRIEF.md
templates/PATCH_PRD.md
templates/PATCH_ARCHITECTURE.md
templates/RNBO_COMPATIBILITY_MATRIX.md
```

## Règle fondamentale

Avant de générer un patch, l'agent doit dire dans quelle couche chaque partie vit :

```txt
Max-only
RNBO-compatible
Max for Live-specific
Web-exportable
```
