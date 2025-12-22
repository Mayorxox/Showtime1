Showtime — Generative Pipeline for Human-Centered Evaluation of Autonomous Systems

Showtime is a developer-ready research repository implementing a modular generative pipeline for synthesizing study-ready video stimuli of autonomous devices operating in urban environments.
The repository mirrors the four phases described in the paper and is intended to support reproducible, controlled perception studies, rather than high-fidelity physical simulation.

Showtime focuses on social and perceptual validity—encoding environment, embodiment, and behavior constraints—rather than physics-accurate rendering.

Pipeline Overview

The repository is structured to reflect the four phases of the Chameleon pipeline:

Phase I — Input Embedding Construction
Structured representations of:

environment (urban backdrops, spatial affordances),

device embodiment (scale, morphology, sensors),

behavior (proxemic rules, motion profiles).

Phase II — Generative Prompt Composition
Compositional prompt templates that translate embeddings into:

structured JSON prompts (machine-readable),

composed natural-language prompts suitable for multimodal diffusion models.

Phase III — Video Synthesis and Refinement (Stubs)
Placeholder utilities for:

temporal consistency regularization,

trajectory smoothing,

proxemic compliance checks.

Phase IV — Instrumentation for Interaction Studies
Metadata schemas and annotation structures that prepare generated videos for:

pervasive displays,

online surveys,

controlled lab studies.

The repository is backend-agnostic and does not call proprietary APIs by default.

This repo is intentionally modular and ready to extend to real generative backends (e.g., Google Veo 3, Runway).

## Quick start
```bash
# (optional) create environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# generate example embeddings
python scripts/generate_embeddings.py

# compose structured and natural-language prompts
python scripts/prompt_composer.py \
  --input examples/example_input/embeddings.json \
  --output examples/example_output/

# simulate refinement stage (placeholder)
python scripts/simulate_refinement.py

```

## Structure
```bash
Chameleon/
├── pipeline/
│   ├── phase1_embeddings/
│   ├── phase2_prompts/
│   ├── phase3_synthesis/
│   └── phase4_instrumentation/
│
├── scripts/
│   ├── generate_embeddings.py
│   ├── prompt_composer.py
│   └── simulate_refinement.py
│
├── examples/
│   ├── example_input/
│   └── example_output/
│
├── configs/
│   ├── model_versions.yaml
│   ├── seeds.yaml
│   └── parameter_ranges.yaml
│
├── requirements.txt
└── README.md
```


## Notes
Notes on Generative Backends

This repository does not include model weights or API calls.

Integration with specific generators (e.g., Google Veo 3, Runway, DeeVid) should be performed using official SDKs and authentication.

Configuration files document model versions, parameter ranges, and random seeds used in the paper to support reproducibility.
