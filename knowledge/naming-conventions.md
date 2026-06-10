# Naming Conventions

## Modules

Format :

```txt
p.module_name
```

Exemples :

```txt
p.transport
p.event_scheduler
p.rnbo_engine
p.ui_state
p.midi_input
p.web_bridge
```

## Send / Receive

Format :

```txt
s project.domain.event
r project.domain.event
```

Exemples :

```txt
s splitflap.clock.tick
r splitflap.clock.tick
s atlas.scale.selected
r atlas.scale.selected
```

## Parameters

Format :

```txt
snake_case
```

Exemples :

```txt
root_note
scale_index
swing_amount
flap_speed
output_gain
```

## Files

Format :

```txt
project-name.module.ext
```

Exemples :

```txt
split-flap-clock.maxpat
split-flap-clock.rnbo.maxpat
split-flap-clock.web.md
```

## Comments

Chaque module doit avoir un commentaire d'en-tête :

```txt
MODULE: transport
ROLE: global clock and timing source
INPUTS: start, stop, tempo
OUTPUTS: tick, bar, beat
RNBO: no
```
