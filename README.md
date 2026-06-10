# BMAD-MAX-RNBO

**Version : v1.0.0**

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

## Runtime recommandé

- Claude comme agent principal.
- Modèles Ollama Cloud pour le raisonnement et le code.
- Max 9 + RNBO pour validation audio/visuelle.
- Taylor Brook MAX-MSP_CC_Framework / Patcher API quand disponible.
- React/Vite pour les exports web.

Aucune hypothèse Free Claude Code.

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

## Documentation v1

- [Installation](INSTALL.md)
- [Usage](USAGE.md)
- [Prompts prêts à copier](PROMPTS.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Contribution](CONTRIBUTING.md)

## Démarrage rapide

1. Cloner le repo :

```bash
git clone https://github.com/broduoliviercontact-web/bmad-max-rnbo.git
cd bmad-max-rnbo
```

2. Relier ou copier le corpus Cycling '74 dans :

```txt
docs/cycling74-userguide/
```

3. Créer un projet :

```bash
python3 scripts/scaffold_project.py split-flap-musical-clock
```

4. Lancer le workflow :

```txt
workflows/create-rnbo-web-export.md
```

5. Produire les documents projet :

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

## Statut v1

Cette v1 pose le cadre de travail : agents, workflows, templates, checklists, scripts de base et documentation d'usage. Les futures versions pourront ajouter un audit `.maxpat` plus profond, une base de compatibilité RNBO enrichie et des exemples complets exportables.
