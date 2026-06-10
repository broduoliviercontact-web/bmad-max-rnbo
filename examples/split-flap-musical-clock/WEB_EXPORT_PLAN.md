# Web Export Plan — Split-Flap Musical Clock

## Objectif

Créer une version web qui affiche l'horloge split-flap et contrôle le moteur RNBO exporté en Web Audio.

## Stack recommandée

```txt
React
Vite
RNBO JS API
Web Audio API
CSS animation split-flap
```

## Arborescence cible

```txt
examples/split-flap-musical-clock/
  export/rnbo/patch.export.json
  web/
    package.json
    src/
      App.jsx
      SplitFlapDisplay.jsx
      rnbo-loader.js
      clock-engine.js
      style.css
```

## Flux web

```txt
user click Start Audio
      ↓
create AudioContext
      ↓
load patch.export.json
      ↓
create RNBO device
      ↓
connect device to destination
      ↓
start clock loop
      ↓
update split-flap UI + send note/tick messages to RNBO
```

## API UI → RNBO

| UI | RNBO | Notes |
|---|---|---|
| Start Audio | create AudioContext | obligatoire navigateur |
| Gain | `output_gain` | 0..1 |
| Density | `density` | 0..1 |
| Root | `root_note` | 0..11 |
| Scale | `scale_index` | index |
| Brightness | `tone_brightness` | timbre |
| Panic | `panic` message | coupe audio |

## Pseudo-code RNBO loader

```js
import { createDevice } from '@rnbo/js';

export async function loadRnboDevice(audioContext) {
  const raw = await fetch('/patch.export.json');
  const patcher = await raw.json();
  const device = await createDevice({ context: audioContext, patcher });
  device.node.connect(audioContext.destination);
  return device;
}
```

## Pseudo-code clock engine

```js
function onSecondChanged(state, rnboDevice) {
  const pitch = 60 + (state.seconds % 12);
  rnboDevice.scheduleEvent(new RNBO.MessageEvent(RNBO.TimeNow, 'note', [pitch, 0.7, 120]));
}
```

## Tests

- [ ] Le navigateur demande une interaction avant l'audio.
- [ ] `patch.export.json` charge sans erreur.
- [ ] L'horloge s'affiche sans audio.
- [ ] Le bouton Start active l'audio.
- [ ] Les changements de seconde déclenchent des sons.
- [ ] Le bouton Panic coupe les sons.
- [ ] Les sliders modifient les paramètres RNBO.

## Limites v1

- Pas de synchronisation Ableton Live dans le web.
- Pas de stockage de presets avancé.
- Pas de rendu 3D.
- Le patch RNBO doit être exporté manuellement depuis Max/RNBO.
