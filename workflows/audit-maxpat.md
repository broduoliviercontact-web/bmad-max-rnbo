# Workflow — Audit Maxpat

## But

Auditer un fichier `.maxpat`.

## Entrées

```txt
path/to/project.maxpat
```

## Sorties

```txt
PATCH_AUDIT_REPORT.md
PATCH_FIX_PLAN.md
```

## Étapes

1. Parser le JSON `.maxpat`.
2. Lister les objets.
3. Lister les patchlines.
4. Détecter les objets inconnus.
5. Détecter fan-out.
6. Vérifier les objets audio.
7. Vérifier `trigger` quand l'ordre est critique.
8. Vérifier boundary RNBO.
9. Vérifier dépendances.
10. Produire blockers/warnings/suggestions.
