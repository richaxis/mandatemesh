# Threat model

## Malicious leader output

A leader may return malformed or fabricated semantic data.

Mitigation: bounded parsing, deterministic semantic hashes, independent validator derivation, and rejection on material disagreement.

## Prompt injection

A submitted mandate may contain instructions aimed at the model rather than policy content.

Mitigation: the prompt treats mission and mandate text as untrusted data. Consensus compares independent derivations.

Residual risk: adversarial natural language can still be difficult to interpret. Ambiguity therefore fails closed.

## Malicious relation classification

A leader may claim two mandates are compatible when they conflict.

Mitigation: validators independently classify the pair. The top-level relationship must match, and conflicts must also match on conflict subtype.

## Model preference deciding authority

The semantic model does not choose precedence.

Mitigation: amendment lineage and numeric weights are deterministic protocol state. Equal weight deliberately produces no winner.

## Stale consumer state

A consumer may continue operating against an old policy after the charter changes.

Mitigation: `is_consistent_for` requires both current consistency and an exact current digest match.

## State growth

Pairwise links can grow quadratically.

Mitigation: each charter is bounded to 24 mandates. Revoked mandates remain historical but are excluded from the active mesh.

## Owner compromise

The charter owner controls proposals, weights, activation, revocation, and restoration.

This contract does not solve key management. Consumers should use the ownership model appropriate for their application.

## Semantic drift

A mandate's semantic record is immutable after consensus. Existing links store both semantic hashes.

This prevents a later text or semantic mutation from silently changing the meaning of an already-analyzed edge.
