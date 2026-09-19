"""Validate pages and local assets reachable from the public homepage."""

from collections import deque
from pathlib import Path
from urllib.parse import unquote
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
START_PAGE = ROOT / "index.html"

EXTERNAL_PREFIXES = (
    "http://",
    "https://",
    "//",
    "mailto:",
    "tel:",
    "javascript:",
    "data:",
)


def resolve_reference(page: Path, reference: str) -> Path | None:
    """Resolve a local page reference relative to its containing HTML file."""
    reference = unquote(reference.split("#", 1)[0].split("?", 1)[0])

    if not reference or reference.startswith(EXTERNAL_PREFIXES):
        return None

    target = (page.parent / reference).resolve()

    if target.is_dir() or reference.endswith("/"):
        target /= "index.html"

    try:
        target.relative_to(ROOT)
    except ValueError:
        return None

    return target


def main() -> int:
    """Validate reachable HTML pages and their referenced local assets."""
    queue = deque([START_PAGE])
    visited: set[Path] = set()
    problems: list[str] = []

    while queue:
        page = queue.popleft()

        if page in visited:
            continue

        if not page.exists():
            problems.append(f"Missing page: {page.relative_to(ROOT)}")
            continue

        visited.add(page)

        text = page.read_text(encoding="utf-8", errors="replace")
        active = re.sub(r"<!--.*?-->", "", text, flags=re.S)

        if re.search(r"<image\b", active, re.I):
            problems.append(
                f"Invalid <image> tag: {page.relative_to(ROOT)}"
            )

        for reference in re.findall(
            r'''<a\b[^>]*href=["']([^"']+)["']''',
            active,
            re.I,
        ):
            target = resolve_reference(page, reference)

            if target is None:
                continue

            if not target.exists():
                problems.append(
                    f"Broken link: {page.relative_to(ROOT)} -> {reference}"
                )
            elif target.suffix.lower() == ".html":
                queue.append(target)

        for reference in re.findall(
            r'''(?:src|href)=["']([^"']+)["']''',
            active,
            re.I,
        ):
            if "${" in reference or "{" in reference:
                continue

            target = resolve_reference(page, reference)

            if target is not None and not target.exists():
                problems.append(
                    f"Missing asset: {page.relative_to(ROOT)} -> {reference}"
                )

        for filename in re.findall(
            r'''(?:img|image)\s*:\s*["']([^"']+)["']''',
            active,
            re.I,
        ):
            candidates = (
                page.parent / filename,
                page.parent / "image" / filename,
            )

            if not any(candidate.exists() for candidate in candidates):
                problems.append(
                    f"Missing image: {page.relative_to(ROOT)} -> {filename}"
                )

        for filename in re.findall(
            r'''audio\s*:\s*["']([^"']+)["']''',
            active,
            re.I,
        ):
            candidates = (
                page.parent / filename,
                page.parent / "audio" / filename,
            )

            if not any(candidate.exists() for candidate in candidates):
                problems.append(
                    f"Missing audio: {page.relative_to(ROOT)} -> {filename}"
                )

        if "image/${n}.png" in text or "audio/${n}.mp3" in text:
            arrays = re.findall(
                r'''(?:const|let|var)\s+\w+\s*=\s*\[([^\]]+)\]''',
                text,
                re.S,
            )

            for body in arrays:
                for number in re.findall(r"\b\d+\b", body):
                    image = page.parent / "image" / f"{number}.png"
                    audio = page.parent / "audio" / f"{number}.mp3"

                    if not image.exists():
                        problems.append(
                            f"Missing image: {page.relative_to(ROOT)} "
                            f"-> image/{number}.png"
                        )

                    if not audio.exists():
                        problems.append(
                            f"Missing audio: {page.relative_to(ROOT)} "
                            f"-> audio/{number}.mp3"
                        )

    print(f"Reachable HTML pages checked: {len(visited)}")

    if problems:
        print("\nValidation failed:")
        for problem in problems:
            print(f"- {problem}")

        return 1

    print("Site validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
