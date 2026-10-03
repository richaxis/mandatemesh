# MandateMesh

MandateMesh is a standalone GenLayer Intelligent Contract for turning natural language operating mandates into consensus-backed, reusable on-chain state.

It is designed for autonomous agents, treasuries, DAOs, protocol operators, and other systems that need a durable charter whose natural-language directives can be compared without trusting a single model response.

## What it provides

A charter contains immutable mandate records and a complete pairwise compatibility graph.

For each proposed mandate, GenLayer consensus is used twice:

1. **Semantic extraction** derives a bounded representation: directive, actor, action, object, condition, exception, and scope.
2. **Pairwise analysis** determines how the new mandate relates to every earlier non-revoked mandate: unrelated, compatible, redundant, specializes, conflict, or ambiguous.

The contract then applies deterministic protocol rules. Consensus does not decide which mandate has authority.

Conflict precedence is resolved from stored state:

- explicit amendment lineage wins;
- otherwise higher mandate weight wins;
- equal weight remains unresolved.

A fail-closed charter does not activate a mandate while its semantic meaning is ambiguous or an applicable conflict remains unresolved.

## Why this is a reusable primitive

A downstream contract can pin the current `mandate_mesh_hash` and require the charter to remain consistent before accepting an action.

Useful consumers include:

- autonomous agent operating charters
- treasury execution policies
- DAO operating mandates
- protocol emergency authorities
- multi-agent coordination agreements
- governance policy registries

The contract is intentionally standalone. There is no frontend, database, or off-chain state required for the primitive.

## Core interface

Writes:

- `create_charter(name, mission, fail_closed)`
- `propose_mandate(charter_id, text, weight, supersedes_mandate_id)`
- `set_blocked_mandate_weight(mandate_id, weight)`
- `activate_blocked_mandate(mandate_id)`
- `revoke_mandate(mandate_id)`
- `restore_superseded_mandate(mandate_id)`

Views:

- `get_charter(charter_id)`
- `get_mandate(mandate_id)`
- `get_link(link_id)`
- `link_between(left_mandate_id, right_mandate_id)`
- `get_mandate_mesh(charter_id)`
- `get_mandate_mesh_links(charter_id)`
- `mandate_mesh_status(charter_id)`
- `is_consistent(charter_id)`
- `is_consistent_for(charter_id, expected_mandate_mesh_hash)`
- `current_mandate_mesh_hash(charter_id)`

## Bounded state

A charter accepts at most 24 mandates. A new mandate is compared against existing non-revoked mandates, giving bounded quadratic consensus work while retaining complete historical links.

## Repository

```text
contracts/mandate_mesh.py     Intelligent Contract
tests/test_mandate_mesh.py    Direct Mode tests
docs/ARCHITECTURE.md          state model and lifecycle
docs/CONSENSUS.md             consensus boundaries and validation
docs/INTEGRATION.md           downstream contract integration
docs/THREAT_MODEL.md          failure and adversarial cases
scripts/preflight.py          offline repository checks
DEPLOYMENT.md                 deployment and verification procedure
SUBMISSION.md                 submission-ready explanation
```

## Quick start

Install the GenLayer CLI and development dependencies for your environment, then run:

```bash
python scripts/preflight.py
gltest tests/test_mandate_mesh.py -v -s
```

Deploy with:

```bash
genlayer deploy --contract contracts/mandate_mesh.py
```

Do not put private keys or credentials in the repository.

## License

MIT. See `LICENSE`.
