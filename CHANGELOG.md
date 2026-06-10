# Changelog

Toutes les modifications importantes de BMAD-MAX-RNBO seront documentees ici.

## 1.0.0 - 2026-06-10

### Ajoute

- Structure initiale du framework BMAD-MAX-RNBO.
- Agents specialises : Max Architect, RNBO Specialist, Patch Critic, Web Export Engineer.
- Workflows de base : creation RNBO/Web, audit maxpat.
- Templates de projet : brief, PRD, architecture, matrice RNBO, parametres RNBO, plan export web, rapport d'audit.
- Checklists : patching Max, compatibilite RNBO, export web.
- Knowledge rules : retrieval local, boundary RNBO, audit patch, conventions de nommage.
- Scripts Python : scaffold de projet et audit maxpat basique.
- Documentation v1 : README, INSTALL, USAGE, PROMPTS, ROADMAP, TROUBLESHOOTING, CONTRIBUTING.

### Decisions v1

- Runtime cible : Claude et modeles Ollama Cloud.
- Documentation locale prioritaire : Cycling 74 User Guide dans docs/cycling74-userguide.
- Generation et audit maxpat via Taylor Brook MAX-MSP_CC_Framework / Patcher API quand disponible.
- Aucune reference operationnelle a Free Claude Code.

### Limites connues

- L'audit maxpat est volontairement minimal dans cette v1.
- La compatibilite RNBO doit encore etre validee dans Max/RNBO pour chaque projet reel.
- Les exemples ne sont pas encore des projets exportables complets.
