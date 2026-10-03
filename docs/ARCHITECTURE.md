# Architecture

## Primitive

MandateMesh treats a charter as a versioned collection of natural-language mandates plus the semantic links between them.

The important distinction is between **semantic work** and **protocol work**.

Semantic work uses GenLayer non-deterministic execution and validator agreement. Protocol work is deterministic once the semantic result is stored.

## State model

### Charter

A charter stores:

- owner
- name
- mission
- fail-closed setting
- revision
- mandate mesh version
- mandate IDs
- link IDs
- active and blocked counts
- resolved and unresolved conflict counts
- ambiguous-link count
- consistency flag
- current mandate mesh hash

### Mandate

A mandate stores:

- original text and text hash
- consensus-derived directive
- actor, action, object
- condition, exception, scope
- semantic state and ambiguity reason
- semantic hash
- weight
- lifecycle status
- creation and activation versions
- amendment lineage
- associated link IDs

### Link

A link stores:

- two mandate IDs
- relationship kind
- conflict subtype
- bounded overlap note
- stable reason code
- deterministic precedence result
- timestamp
- both semantic hashes

The semantic hashes bind a link to the mandate meanings that were actually analyzed.

## Lifecycle

`PROPOSED -> ACTIVE` when:

1. semantic consensus accepts the mandate;
2. all required links are available;
3. the mandate is not ambiguous;
4. any conflict is deterministically resolved;
5. any declared amendment target has a valid semantic relationship.

Otherwise the mandate remains `BLOCKED`.

A blocked mandate can be reweighted and then activated without repeating semantic analysis because the stored links are reused.

An active mandate can be revoked. An active mandate can also be superseded by a new mandate whose semantic relationship is validated as a meaningful refinement.

## Versioning

`mandate_mesh_version` changes when the active charter changes.

`mandate_mesh_hash` is a canonical digest of active mandates and active-to-active links. Consumers can pin the digest to make the charter state explicit.

The hash is not a replacement for consensus. It is a commitment to already-consensus-accepted state.

## Bound

Each charter is limited to 24 mandates. Pairwise analysis is therefore bounded at 276 unordered pairs in the largest charter.
