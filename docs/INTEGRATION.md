# Integration

MandateMesh can act as a policy primitive for another Intelligent Contract.

## Pin a charter

A consumer should read:

```python
expected = mandate_mesh.current_mandate_mesh_hash(charter_id)
```

and persist the value if the application wants to bind execution to that exact charter revision.

Before a sensitive operation:

```python
if not mandate_mesh.is_consistent_for(charter_id, expected):
    raise gl.vm.UserError("charter changed or is not consistent")
```

This creates a simple policy gate:

`consumer state -> pinned charter digest -> consistency check -> action`

## Inspecting a mandate

Use:

```python
mandate_mesh.get_mandate(mandate_id)
```

to obtain the original text, semantic record, status, weight, and amendment lineage.

## Inspecting a pair

Use:

```python
mandate_mesh.link_between(left_id, right_id)
```

to determine whether two mandates are compatible, redundant, specialized, conflicting, or ambiguous.

## Recommended consumer behavior

A consumer should:

1. create or reference a charter;
2. require a known charter digest for policy-sensitive execution;
3. check `is_consistent_for` before executing;
4. treat `BLOCKED` mandates as non-authoritative;
5. treat unresolved conflicts as non-authoritative;
6. store the mandate IDs that justify a sensitive action where useful.

The consumer should not reproduce the semantic prompts. MandateMesh is intended to centralize the consensus-backed policy primitive.
