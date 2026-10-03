# Consensus

MandateMesh has two independent semantic consensus boundaries.

## 1. Mandate meaning

The leader derives a structured representation from the charter mission and submitted mandate.

The representation contains:

- directive: require, permit, or prohibit
- actor
- action
- object
- condition
- exception
- scope
- ambiguity status

The validator independently derives the same representation from the immutable submitted text.

The validator rejects malformed records, invalid hashes, mismatched directive or ambiguity state, mismatched condition/exception presence, and semantic disagreement. For clear mandates, a comparison prompt is used to decide whether harmless wording differences still describe the same material meaning.

The leader never gets to persist an arbitrary semantic object merely because validators can parse it.

## 2. Pairwise relationship

The leader classifies the candidate against an existing mandate.

Possible outcomes:

- `UNRELATED`
- `COMPATIBLE`
- `REDUNDANT`
- `SPECIALIZES`
- `CONFLICT`
- `AMBIGUOUS`

For conflicts, validators also independently derive the conflict subtype and must agree on it.

The stored overlap text and reason code are explanatory metadata. The relationship kind and conflict subtype are the protocol-relevant consensus facts.

## What consensus does not decide

Consensus does not select a winner in a conflict.

That is deterministic protocol state:

1. a valid explicit amendment takes precedence;
2. otherwise the higher stored weight prevails;
3. equal weights remain unresolved.

This prevents model output from silently becoming authority.

## Fail-closed behavior

Ambiguous semantic extraction is blocked.

Ambiguous pairwise analysis is blocked for fail-closed charters.

An equal-weight conflict remains unresolved and therefore cannot activate in a fail-closed charter.

## Prompt injection

Mission and mandate text are wrapped as untrusted data in the prompts. The semantic instructions explicitly tell the model not to follow instructions embedded in user-supplied text.

This is a mitigation, not a claim that arbitrary text is harmless. Consensus still acts as the second boundary.
