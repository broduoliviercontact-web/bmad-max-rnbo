# Patch Audit Rules

## Catégories

```txt
blocker   empêche le patch de fonctionner ou peut produire un danger audio
warning   problème sérieux mais contournable
info      remarque utile
suggestion amélioration de lisibilité ou maintenance
```

## Blockers fréquents

- audio sans contrôle de gain ;
- absence de mute/panic dans un patch génératif ;
- objets manquants ;
- dépendances absentes ;
- patchline vers un objet supprimé ;
- objets non compatibles dans une zone RNBO ;
- boucle de messages infinie ;
- fan-out critique sans trigger quand l'ordre est important.

## Warnings fréquents

- send/receive non documentés ;
- objets sans scripting name ;
- sous-patchers trop gros ;
- UI illisible ;
- absence de valeurs par défaut ;
- absence de commentaires ;
- dépendance à un chemin absolu ;
- paramètres non exposés clairement.

## Audit structurel

Vérifier :

- nombre d'objets ;
- nombre de patchlines ;
- objets inconnus ;
- fan-out ;
- objets audio ;
- objets UI ;
- objets RNBO ;
- objets M4L ;
- dépendances fichier ;
- sous-patchers ;
- nommage.

## Audit RNBO

Vérifier :

- frontière RNBO claire ;
- paramètres ;
- inlets/outlets ;
- niveaux audio ;
- dépendances ;
- export web.
