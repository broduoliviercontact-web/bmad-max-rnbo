# RNBO Boundary Rules

## Objectif

Définir ce qui peut être placé dans `rnbo~` et ce qui doit rester dans Max, Max for Live ou le navigateur.

## Classification

Chaque module doit recevoir un statut :

```txt
RNBO-compatible
Max-only
M4L-only
Web-only
Unknown / needs test
```

## Règle fondamentale

Un projet Max complet ne doit jamais être supposé exportable tel quel.

## Architecture recommandée

```txt
[Max orchestration/UI] → [rnbo~ engine] → [audio out]
          ↓
      [web export]
```

## RNBO-compatible typique

- moteur DSP ;
- oscillateurs ;
- filtres ;
- enveloppes ;
- logique de contrôle simple ;
- paramètres exposés ;
- génération musicale simple ;
- états internes nécessaires au moteur.

## Max-only typique

- jweb ;
- interface Max complexe ;
- debug console ;
- outils de développement ;
- patchers de test ;
- visualisation non nécessaire au moteur ;
- logique dépendante d'objets Max non exportables.

## M4L-only typique

- live.object ;
- live.path ;
- live.dial / live.* ;
- Live API ;
- intégration transport Live ;
- automation Live spécifique.

## Web-only typique

- React ;
- CSS ;
- DOM ;
- canvas ;
- WebSocket ;
- UI navigateur ;
- loader RNBO JS.

## Checklist RNBO

- Les paramètres sont nommés clairement.
- Les ranges sont définis.
- Les valeurs par défaut sont définies.
- Le moteur audio peut fonctionner sans l'UI Max.
- Le moteur ne dépend pas de fichiers absents.
- Le niveau de sortie est sécurisé.
- Le patch exporté est testé dans un navigateur.
