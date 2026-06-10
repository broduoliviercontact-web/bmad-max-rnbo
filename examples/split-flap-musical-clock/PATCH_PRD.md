# Patch PRD — Split-Flap Musical Clock

## Résumé

Le patch transforme une horloge visuelle split-flap en instrument génératif. Chaque changement d'état visuel peut produire un événement musical : note, percussion, accord, texture, modulation ou silence.

Le système doit rester modulaire : la logique d'interface et de visualisation reste côté Max/Web, tandis que le moteur audio exportable vit dans `rnbo~`.

## Fonctionnalités

| ID | Fonction | Priorité | Couche | Notes |
|---|---|---:|---|---|
| F01 | Afficher heures/minutes/secondes en split-flap | must | Max/Web | via jweb ou UI web |
| F02 | Animer chaque changement de chiffre | must | Max/Web | animation CSS/JS |
| F03 | Déclencher un événement musical à chaque tick | must | Max/RNBO | notes ou triggers |
| F04 | Générer notes selon gamme/root | must | RNBO | moteur musical minimal |
| F05 | Contrôler tempo, density, swing, gain | must | Max/RNBO/Web | paramètres exposés |
| F06 | Mode horloge réelle / mode tempo musical | should | Max | deux sources temporelles |
| F07 | Export RNBO Web Audio | should | RNBO/Web | patch.export.json |
| F08 | Mode Max for Live synchronisé au transport Live | could | M4L | phase ultérieure |

## Paramètres principaux

| Nom | Type | Range | Default | Couche | RNBO |
|---|---|---|---|---|---|
| output_gain | float | 0..1 | 0.7 | RNBO/Web | yes |
| root_note | int | 0..11 | 0 | RNBO/Web | yes |
| scale_index | int | 0..n | 0 | RNBO/Web | yes |
| density | float | 0..1 | 0.5 | RNBO/Web | yes |
| flap_speed | float | 0.05..2 | 0.25 | Max/Web | no |
| swing_amount | float | 0..0.75 | 0 | RNBO | yes |
| tone_brightness | float | 0..1 | 0.5 | RNBO | yes |
| clock_mode | enum | real/tempo/manual | real | Max/Web | no |

## États

| État | Description |
|---|---|
| idle | horloge visible, pas d'événement audio |
| running | horloge + événements musicaux actifs |
| muted | animation active, audio coupé |
| export_test | moteur RNBO contrôlé par UI minimale |
| error | erreur de chargement UI/RNBO |

## Critères d'acceptation

- [ ] Le patch affiche une horloge split-flap lisible.
- [ ] Chaque changement peut produire un événement musical.
- [ ] Le moteur audio est isolé dans `rnbo~`.
- [ ] Les paramètres RNBO principaux sont nommés et testables.
- [ ] La sortie audio possède un gain final et un mute/panic.
- [ ] L'interface visuelle ne dépend pas du moteur audio pour fonctionner.
- [ ] Le moteur audio peut être exporté et contrôlé depuis une page web.

## Hors périmètre v1

- Synchronisation Live complète.
- Presets avancés.
- Score musical complexe.
- Génération graphique 3D/Jitter.
- Export mobile optimisé.
