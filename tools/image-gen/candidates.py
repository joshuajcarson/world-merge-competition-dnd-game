"""Staging area for batch generations awaiting a human pick.

When a script is run with --count N (N > 1) it saves every image here, named by
seed, instead of into assets/. Nothing in this folder is committed (it's in
.gitignore) and nothing here is published by the Jekyll build. Re-running a
batch adds more candidates rather than replacing the earlier ones, so a human
can compare across batches. `--pick SEED` then promotes one candidate into
assets/ and (for portraits) records it in the note's frontmatter.
"""
from pathlib import Path

CANDIDATES_ROOT = Path(__file__).parent / "candidates"


def candidate_dir(*parts):
    return CANDIDATES_ROOT.joinpath(*parts)


def save_candidates(directory, results):
    """results is a list of (png_bytes, seed). Returns [(seed, Path)] in order."""
    directory.mkdir(parents=True, exist_ok=True)
    saved = []
    for image_bytes, seed in results:
        path = directory / f"{seed}.png"
        path.write_bytes(image_bytes)
        saved.append((seed, path))
    return saved


def load_candidate(directory, seed):
    path = directory / f"{seed}.png"
    if not path.exists():
        available = sorted(p.stem for p in directory.glob("*.png")) if directory.exists() else []
        hint = f" Available seeds: {', '.join(available)}." if available else " No candidates saved yet."
        raise FileNotFoundError(f"No candidate with seed {seed} in {directory}.{hint}")
    return path.read_bytes()
