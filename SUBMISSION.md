# MandateMesh submission

## Category

Standalone GenLayer Intelligent Contract.

## Purpose

MandateMesh is a reusable policy primitive for autonomous systems that need natural-language operating mandates to become durable, consensus-backed state.

A charter stores immutable mandates and a complete pairwise semantic link graph. Other contracts can inspect that graph or pin its current digest before performing policy-sensitive actions.

## Consensus logic

There are two semantic consensus boundaries.

First, validators independently derive the meaning of each proposed mandate and reject material disagreement.

Second, validators independently classify the relationship between the new mandate and existing mandates. Conflict subtypes are consensus checked as well.

The protocol then applies deterministic precedence. Consensus does not decide which mandate wins.

## Why it is more than a thin model wrapper

The contract maintains:

- immutable semantic records
- pairwise link history
- deterministic precedence
- amendment lineage
- blocked proposals
- lifecycle states
- charter revisions
- versioned active state
- a canonical charter digest
- a reusable read interface for downstream contracts

The semantic result therefore compounds into persistent state instead of producing a one-off AI answer.

## Suggested reviewer sequence

1. Create a fail-closed treasury charter.
2. Add a prohibition at weight 100.
3. Add an emergency permission at weight 100.
4. Observe the second mandate remain blocked because the conflict is unresolved.
5. Raise its weight to 200.
6. Observe the existing conflict link change deterministically.
7. Activate the blocked mandate without another semantic analysis.
8. Read the new charter digest.
9. Call `is_consistent_for` with that digest.
10. Submit an amendment and inspect the preserved lineage.

## Verification

The repository contains Direct Mode tests for:

- charter initialization
- owner authorization
- clear semantic activation
- ambiguous mandate blocking
- compatible mandates
- equal-weight conflicts
- deterministic weight precedence
- blocked mandate reweighting
- immutable active weights
- amendment lineage
- invalid amendment relationships
- digest consistency

No deployment address is claimed in this repository until an actual deployment is performed.
