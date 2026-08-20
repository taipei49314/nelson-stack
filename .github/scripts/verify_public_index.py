from __future__ import annotations

import json
import os
import re
import urllib.request
from pathlib import Path


OWNER = "taipei49314"
META_REPOSITORIES = {OWNER, "nelson-stack"}


def public_repositories() -> set[str]:
    request = urllib.request.Request(
        f"https://api.github.com/users/{OWNER}/repos?per_page=100&type=owner",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "public-index-check",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    return {repo["name"] for repo in payload if not repo["archived"]}


def main() -> int:
    public = public_repositories()
    projects = public - META_REPOSITORIES
    readme = Path("README.md").read_text(encoding="utf-8")
    linked = set(
        re.findall(rf"https://github\.com/{OWNER}/([A-Za-z0-9_.-]+)", readme)
    )
    nonpublic = sorted(linked - public)
    missing = sorted(projects - linked)
    if nonpublic or missing:
        print(json.dumps({"missing": missing, "nonpublic": nonpublic}, sort_keys=True))
        return 1
    print(json.dumps({"active_projects": len(projects), "public_repositories": len(public)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
