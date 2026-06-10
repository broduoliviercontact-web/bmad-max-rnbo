# Troubleshooting

## Le corpus Cycling 74 n'est pas trouve

Verifier que le dossier existe :

```bash
ls -la docs/cycling74-userguide
```

Verifier aussi :

```bash
ls -la docs/cycling74-userguide/INDEX.md
ls -la docs/cycling74-userguide/manifest.json
```

Si le corpus est ailleurs, creer un symlink depuis la racine du repo :

```bash
mkdir -p docs
ln -s "../docs/cycling74-userguide" "docs/cycling74-userguide"
```

## Le symlink ne marche pas avec iCloud ou Obsidian

Copier le corpus au lieu de faire un symlink :

```bash
mkdir -p docs
cp -R "../docs/cycling74-userguide" "docs/cycling74-userguide"
```

## Le script scaffold_project.py ne se lance pas

Verifier Python :

```bash
python3 --version
```

Lancer depuis la racine du repo :

```bash
python3 scripts/scaffold_project.py test-rnbo-project
```

## Le script audit_maxpat.py ne lit pas mon patch

Verifier que le fichier existe :

```bash
ls -la patches/mon-patch.maxpat
```

Verifier que le fichier est bien un JSON Max valide :

```bash
python3 -m json.tool patches/mon-patch.maxpat > /tmp/maxpat-check.json
```

## Le patch Max s'ouvre avec des objets manquants

Actions conseillees :

- ouvrir la Max Console ;
- noter les objets manquants ;
- verifier les packages installes ;
- verifier le Search Path Max ;
- verifier que les abstractions sont dans le projet ;
- demander a Patch Critic de produire un PATCH_AUDIT_REPORT.md.

## L'export RNBO ne fonctionne pas

Verifier :

- la boundary RNBO ;
- les objets places dans rnbo ;
- les parametres exposes ;
- les fichiers externes ;
- les inlets/outlets ;
- les niveaux audio ;
- les messages d'erreur dans Max.

Ne pas supposer qu'un patch Max entier est exportable RNBO.

## Le projet web ne produit pas de son

Verifier :

- interaction utilisateur avant demarrage AudioContext ;
- chemin vers patch.export.json ;
- erreurs dans la console navigateur ;
- mapping des parametres ;
- gain final ;
- navigateur utilise.

## Regle de validation

Un agent peut preparer, generer et auditer. La validation finale audio/visuelle doit etre faite dans Max, RNBO ou le navigateur cible.
