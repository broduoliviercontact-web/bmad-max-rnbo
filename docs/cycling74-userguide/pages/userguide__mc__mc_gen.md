---
title: "MC and Gen"
source: https://docs.cycling74.com/userguide/mc/mc_gen/
source_path: /userguide/mc/mc_gen/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# MC and Gen

Source: https://docs.cycling74.com/userguide/mc/mc_gen/

## Extracted Text

# MC and Gen
Gen and MC combine in the following objects:
-
mc.gen~ contains individual instances of gen~ via the MC Wrapper , so it can take advantage of all the features available to any wrapped object.
-
mcs.gen~ , like other mcs.* objects, combines the separate Gen inputs and outputs defined by`inX`and`outX`operators into a multi-channels input and output.
-
mc.gen contains multiple instances of the event-based gen object. It has an additional outlet that informs Max of the voice number associated with any outgoing message.
## See Also
-
Using mc.gen With the MC Wrapper
-
MC Gen Instances
-
Gen Features for MC
-
MC Gen Operators
