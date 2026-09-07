#!/usr/bin/env python3
"""Install this checkout's complete skill folders into Codex, without overwrites."""
from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tempfile


SOURCE = Path(__file__).resolve().parents[1] / "skills"


def default_destination() -> Path:
    codex_root = os.environ.get("CODEX_HOME")
    return (Path(codex_root).expanduser() if codex_root else Path.home() / ".codex") / "skills"


def manifest(folder: Path) -> dict[str, str | None]:
    """Compare every resource, including empty directories; reject linked content."""
    result = {}
    if folder.is_symlink() or getattr(folder.lstat(), "st_file_attributes", 0) & 0x400:
        raise ValueError(f"Linked skill folders are not supported: {folder}")
    for item in sorted(folder.rglob("*")):
        # st_file_attributes catches Windows junctions on Python 3.10/3.11 too.
        if item.is_symlink() or getattr(item.lstat(), "st_file_attributes", 0) & 0x400:
            raise ValueError(f"Linked resources are not supported: {item}")
        key = item.relative_to(folder).as_posix()
        if item.is_file():
            result[key] = hashlib.sha256(item.read_bytes()).hexdigest()
        elif item.is_dir():
            result[key] = None
        else:
            raise ValueError(f"Unsupported resource: {item}")
    return result


def install(destination: Path) -> None:
    destination = destination.expanduser().resolve()
    source = SOURCE.resolve()
    if destination == source or source in destination.parents or destination in source.parents:
        raise ValueError("The destination must not overlap the source skills directory.")
    skills = sorted(p for p in source.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not skills:
        raise ValueError(f"No skill folders found in {source}")

    pending = []
    # Preflight the entire set before installing any skill.
    for skill in skills:
        if not (skill / "SKILL.md").is_file():
            raise ValueError(f"Missing entrypoint: {skill / 'SKILL.md'}")
        expected = manifest(skill)
        target = destination / skill.name
        if os.path.lexists(target):
            if target.is_dir() and manifest(target) == expected:
                print(f"Already installed: {target}")
                continue
            raise ValueError(
                f"Destination exists and differs: {target}\n"
                "Back up and move that skill folder outside the skills directory, then retry."
            )
        pending.append((skill, target, expected))

    if pending:
        destination.mkdir(parents=True, exist_ok=True)
        # Stage outside the discovery directory. A failed copy never exposes a partial skill.
        with tempfile.TemporaryDirectory(prefix="agent-toolkit-install-", dir=destination.parent) as staging:
            for skill, target, expected in pending:
                staged = Path(staging) / skill.name
                shutil.copytree(skill, staged)
                if manifest(staged) != expected:
                    raise ValueError(f"Copy verification failed for {skill.name}")
            for skill, target, expected in pending:
                if os.path.lexists(target):
                    raise ValueError(f"Destination appeared during installation: {target}")
                (Path(staging) / skill.name).rename(target)
                if manifest(target) != expected:
                    raise ValueError(f"Installed content differs: {target}")
                print(f"Installed: {target}")
    print(f"Verified {len(skills)} skills. They will be available on your next Codex turn.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest", type=Path, default=default_destination(),
        help="Skills directory (default: $CODEX_HOME/skills or ~/.codex/skills).",
    )
    args = parser.parse_args(argv)
    try:
        install(args.dest)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
