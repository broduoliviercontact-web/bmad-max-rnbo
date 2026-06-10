# Workflow — Create RNBO Web Export

## But

Créer un projet Max/RNBO exportable vers Web Audio avec interface web.

## Étapes

### 1. Brief

Remplir :

```txt
templates/PROJECT_BRIEF.md
```

### 2. PRD

Remplir :

```txt
templates/PATCH_PRD.md
```

### 3. Architecture

Créer :

```txt
templates/PATCH_ARCHITECTURE.md
```

Séparer :

```txt
Max-only
RNBO-compatible
Web-exportable
M4L-specific
```

### 4. Boundary RNBO

Créer :

```txt
templates/RNBO_COMPATIBILITY_MATRIX.md
```

### 5. Paramètres

Créer :

```txt
templates/RNBO_PARAMETERS.md
```

### 6. Patch

Créer ou modifier :

```txt
patches/project.maxpat
patches/project.rnbo.maxpat
```

### 7. Export

Exporter depuis Max/RNBO :

```txt
export/rnbo/patch.export.json
```

### 8. Web

Créer :

```txt
web/package.json
web/src/App.jsx
web/src/rnbo-loader.js
web/src/style.css
```

### 9. Audit

Remplir :

```txt
templates/PATCH_AUDIT_REPORT.md
```

### 10. Documentation

Créer :

```txt
README.md
TROUBLESHOOTING.md
```
