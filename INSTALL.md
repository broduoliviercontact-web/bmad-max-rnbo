# Installation

## Objectif

Ce repo fournit une base de travail agentique pour Max/MSP, RNBO et export Web Audio, à utiliser avec Claude et des modèles Ollama Cloud.

## Emplacement installé

```txt
/Users/zub/Library/Mobile Documents/iCloud~md~obsidian/Documents/MetaVault/02 - Projets/Max - Workspace/bmad-max-rnbo
```

## Étapes d'installation

1. Décompresser `bmad-max-rnbo-starter.zip`.
2. Copier le contenu dans `bmad-max-rnbo/`.
3. Vérifier la présence des dossiers racine :

```txt
README.md
BMAD_MAX_AGENT_BRIEF.md
agents/
workflows/
templates/
checklists/
knowledge/
scripts/
examples/
docs/
```

4. Intégrer le corpus local Cycling '74 User Guide dans :

```txt
docs/cycling74-userguide
```

5. Vérifier le scaffold Python :

```bash
python3 scripts/scaffold_project.py test-rnbo-project
```

6. Initialiser Git :

```bash
git init
git add .
git commit -m "Initial BMAD-MAX-RNBO starter kit"
```

## Structure du repo

```txt
agents/        briefs spécialisés par rôle
workflows/     procédures guidées par tâche
templates/     documents à remplir pour cadrer un projet
checklists/    contrôles qualité Max, RNBO et export web
knowledge/     règles de travail et conventions
scripts/       utilitaires Python
examples/      exemples de projets et de cas d'usage
docs/          documentation locale, dont le corpus Cycling '74
```

## Créer un nouveau projet

Créer un squelette de projet :

```bash
python3 scripts/scaffold_project.py mon-projet-rnbo
```

Le dossier généré contient notamment :

```txt
patches/
docs/
export/rnbo/
web/src/
tests/
```

Ensuite, utiliser :

```txt
templates/PROJECT_BRIEF.md
templates/PATCH_PRD.md
templates/PATCH_ARCHITECTURE.md
templates/RNBO_COMPATIBILITY_MATRIX.md
```

## Utiliser le corpus Cycling '74

Le corpus local est disponible dans :

```txt
docs/cycling74-userguide/
```

Réflexes conseillés :

- commencer par `docs/cycling74-userguide/INDEX.md` ;
- consulter `pages/` pour les sujets détaillés ;
- référencer explicitement les sections `rnbo`, `patching`, `patching_mechanics`, `javascript`, `web_browser`, `m4l` selon le besoin ;
- ne jamais modifier le corpus source original hors du repo.

## Utiliser les agents

Agents disponibles :

- `agents/max-architect.md`
- `agents/rnbo-specialist.md`
- `agents/patch-critic.md`
- `agents/web-export-engineer.md`

Flux recommandé :

1. `max-architect` définit la structure du patch.
2. `rnbo-specialist` identifie la boundary RNBO et les paramètres.
3. `web-export-engineer` prépare l'export Web Audio.
4. `patch-critic` audite le patch ou le plan avant validation.

## Lancer un audit `.maxpat`

Audit brut en ligne de commande :

```bash
python3 scripts/audit_maxpat.py patches/mon-patch.maxpat > PATCH_AUDIT_REPORT.md
```

Audit guidé côté agent :

```txt
Utilise workflows/audit-maxpat.md.
Analyse patches/mon-patch.maxpat.
Produit PATCH_AUDIT_REPORT.md avec blockers, warnings et suggestions.
```
