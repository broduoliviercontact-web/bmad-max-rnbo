# Patch Audit Report — Split-Flap Musical Clock

## Statut

Document d'audit initial. Le patch `.maxpat` n'est pas encore généré ni validé dans Max.

## Blockers attendus à vérifier

| ID | Problème potentiel | Impact | Correction |
|---|---|---|---|
| B001 | moteur audio sans gain final | risque de sortie trop forte | ajouter `output_gain` dans RNBO + gain/mute Max |
| B002 | UI jweb placée dans boundary RNBO | export impossible | garder jweb hors `rnbo~` |
| B003 | pas de bouton panic | risque performance/génératif | ajouter `panic` côté Max et RNBO |
| B004 | messages multiples sans ordre explicite | comportement instable | utiliser `trigger` dans Max |

## Warnings attendus

| ID | Problème potentiel | Impact | Correction |
|---|---|---|---|
| W001 | send/receive non documentés | maintenance difficile | appliquer naming convention |
| W002 | tempo musical et horloge réelle mélangés | timing confus | séparer `clock_mode` |
| W003 | dépendance web/jweb trop forte | export fragile | créer API événementielle simple |
| W004 | trop de logique dans RNBO | export complexe | limiter RNBO au moteur sonore v1 |

## Checklist Max

- [ ] `p.transport_clock` créé.
- [ ] `p.visual_state_manager` créé.
- [ ] `p.music_event_generator` créé.
- [ ] `rnbo~ split_flap_engine` créé.
- [ ] `p.audio_safety` créé.
- [ ] fan-out critique vérifié.
- [ ] `trigger` utilisé quand ordre important.
- [ ] commentaires de modules ajoutés.

## Checklist RNBO

- [ ] paramètres exposés.
- [ ] `output_gain` présent.
- [ ] message `panic` présent.
- [ ] moteur testable sans UI Max.
- [ ] export `patch.export.json` généré.

## Checklist web

- [ ] AudioContext créé après clic utilisateur.
- [ ] split-flap affiché.
- [ ] patch RNBO chargé.
- [ ] paramètres mappés.
- [ ] panic fonctionne.

## Conclusion

La conception est saine si la séparation reste stricte :

```txt
UI/clock hors RNBO
moteur sonore dans RNBO
web UI séparée mais compatible avec les mêmes messages
```
