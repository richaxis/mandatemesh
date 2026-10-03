from pathlib import Path
import ast

ROOT = Path(__file__).parents[1]
contract = ROOT / "contracts" / "mandate_mesh.py"

checks = []
checks.append(("contract exists", contract.exists()))
source = contract.read_text(encoding="utf-8")
try:
    ast.parse(source)
    checks.append(("python syntax", True))
except SyntaxError as exc:
    checks.append((f"python syntax: {exc}", False))

required = [
    "class MandateMesh",
    "class IMandateMesh",
    "gl.vm.run_nondet_unsafe",
    "gl.nondet.exec_prompt",
    "is_consistent_for",
    "mandate_mesh_hash",
    "MAX_MANDATES_PER_CHARTER",
]
for item in required:
    checks.append((f"contains {item}", item in source))

old_names = ["RuleGraph", "RULEGRAPH", "rule_graph.py", "rulebook", "Rulebook"]
for item in old_names:
    checks.append((f"no source reference to {item}", item not in source))

failed = [name for name, ok in checks if not ok]
for name, ok in checks:
    print(("PASS " if ok else "FAIL ") + name)
if failed:
    raise SystemExit("Preflight failed: " + ", ".join(failed))
print(f"Preflight passed: {len(checks)} checks")
