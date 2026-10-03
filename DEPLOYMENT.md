# Deployment

This repository does not claim a live deployment. Record deployment details only after they are returned by the GenLayer CLI.

## 1. Install

Use the GenLayer CLI version required by your current Studio environment.

```bash
npm install -g genlayer
genlayer --version
```

Install the repository's development requirements:

```bash
python -m pip install -r requirements-dev.txt
```

## 2. Select the network

For a StudioNet submission, configure the network using the current CLI command:

```bash
genlayer network set studionet
genlayer config get network
genlayer account show
```

Do not commit private keys.

## 3. Preflight

```bash
python scripts/preflight.py
```

## 4. Local tests

```bash
gltest tests/test_mandate_mesh.py -v -s
```

## 5. Deploy

```bash
genlayer deploy --contract contracts/mandate_mesh.py
```

Save the real finalized contract address and transaction hash in a deployment record.

## 6. Smoke test

Run this lifecycle:

```text
create_charter
    |
propose clear mandate
    |
ACTIVE
    |
propose equal-weight conflicting mandate
    |
BLOCKED
    |
set_blocked_mandate_weight
    |
existing link becomes deterministically resolved
    |
activate_blocked_mandate
    |
ACTIVE + new mandate_mesh_hash
```

Then verify:

```text
current_mandate_mesh_hash
is_consistent
is_consistent_for
link_between
```

## Important

Do not copy deployment addresses, transaction hashes, or explorer URLs from another contract. The deployment section should contain only evidence produced by the deployment being submitted.
