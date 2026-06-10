# Web Export Plan

## Export RNBO

```txt
export/rnbo/patch.export.json
```

## Web stack

```txt
React
Vite
RNBO JS API
Web Audio API
```

## Fichiers

```txt
web/package.json
web/src/App.jsx
web/src/rnbo-loader.js
web/src/style.css
```

## Param mapping

| UI | RNBO Param | Range | Notes |
|---|---|---|---|
| gain slider | output_gain | 0..1 |  |

## Tests navigateur

- [ ] AudioContext démarre après interaction utilisateur.
- [ ] patch.export.json chargé.
- [ ] paramètres modifiables.
- [ ] pas de clipping.
- [ ] fonctionne dans Chrome.
- [ ] fonctionne dans Safari si cible macOS/iOS.
