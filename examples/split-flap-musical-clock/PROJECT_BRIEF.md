# Project Brief — Split-Flap Musical Clock

## Nom du projet

Split-Flap Musical Clock

## Résumé

Créer une horloge musicale visuelle inspirée des panneaux split-flap. Chaque changement de caractère, chiffre ou état peut déclencher un événement musical : note, accord, percussion, texture ou modulation.

Le projet doit fonctionner d'abord dans Max/MSP, puis isoler le moteur musical/audio dans `rnbo~` pour préparer un export Web Audio.

## Intention musicale

Transformer le temps en matière musicale : secondes, minutes, heures et changements visuels deviennent des déclencheurs rythmiques, mélodiques et texturaux.

## Usage cible

- Installation interactive.
- Performance audiovisuelle.
- Horloge générative dans Max.
- Démo pédagogique RNBO/Web Audio.
- Prototype pour Max for Live.

## Entrées

| Entrée | Description | Couche |
|---|---|---|
| heure système | source temporelle principale | Max-only |
| tempo manuel | contrôle musical | Max/RNBO |
| Ableton Link / transport | optionnel | Max/M4L |
| UI split-flap | interaction visuelle | Max/Web |
| presets | choix de comportements | Max/Web/RNBO |

## Sorties

| Sortie | Description | Couche |
|---|---|---|
| animation split-flap | affichage visuel | jweb/Web |
| notes/events | événements musicaux | Max/RNBO |
| audio stéréo | moteur sonore | RNBO |
| paramètres web | contrôle navigateur | Web/RNBO |

## Contraintes

- Le moteur RNBO doit pouvoir fonctionner sans l'interface Max.
- L'interface split-flap ne doit pas être placée dans `rnbo~`.
- Le projet doit éviter le clipping audio.
- Les paramètres doivent être nommés clairement.
- L'export web doit être pensé dès l'architecture.

## Critères de réussite

- [ ] L'horloge affiche un état lisible.
- [ ] Chaque changement peut déclencher un événement musical.
- [ ] Le moteur audio est isolé dans une couche RNBO-compatible.
- [ ] Les paramètres principaux sont exposés.
- [ ] Un plan d'export web existe.
- [ ] Les limites Max-only/RNBO/Web sont documentées.
