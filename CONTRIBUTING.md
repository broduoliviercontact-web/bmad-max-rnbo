# Contributing

Merci de contribuer a BMAD-MAX-RNBO.

## Philosophie

Ce repo doit rester utile pour des projets reels Max/MSP, RNBO, Max for Live et export Web Audio.

Les contributions doivent respecter quatre principes :

1. clarte ;
2. separation des couches ;
3. documentation locale d'abord ;
4. validation honnete.

## Separation des couches

Toute contribution technique doit indiquer ce qui appartient a :

```txt
Max-only
RNBO-compatible
Max for Live-specific
Web-exportable
```

## Documentation locale

Avant d'ajouter une regle Max, RNBO, M4L, Gen ou Jitter, verifier le corpus local :

```txt
docs/cycling74-userguide/
```

Ne pas coller de longs extraits de documentation officielle. Resumer en decisions de patching.

## Ajouter un agent

Creer un fichier dans :

```txt
agents/
```

Structure recommandee :

```md
# Agent - Nom

## Mission
## Sources locales
## Responsabilites
## Livrables
## Format de reponse
```

## Ajouter un workflow

Creer un fichier dans :

```txt
workflows/
```

Un workflow doit contenir :

- but ;
- entrees ;
- sorties ;
- etapes ;
- fichiers produits ;
- criteres de validation.

## Ajouter une checklist

Creer un fichier dans :

```txt
checklists/
```

Une checklist doit etre actionnable, courte et orientee production.

## Ajouter un script

Creer un fichier dans :

```txt
scripts/
```

Regles :

- Python 3 standard quand possible ;
- pas de dependance lourde sans justification ;
- commentaires simples ;
- sortie lisible en Markdown si possible.

## Commits

Format recommande :

```txt
Add RNBO export checklist
Update patch audit rules
Fix scaffold script
Document split-flap workflow
```

## Validation

Ne pas ecrire qu'un patch est valide audio/visuel si Max, RNBO ou le navigateur cible n'a pas ete ouvert et teste.
