#!/usr/bin/env python3
"""check_public.py - refuse to let real client material reach a public repo.

This site is PUBLIC: the free org plan serves GitHub Pages only from a public repo, so
anything committed here is readable by anyone with the URL. Run this before every commit.

    python3 check_public.py

The name list is not a guess. It comes from the example filenames in the private marketplace
repo (plugins/*/skills/*/examples/), which is how sdworx and mortgage-ops were found after six
names had been assumed to be the whole set. Add to it, never trim it.
"""
import os, re, sys

FORBIDDEN = ["Helvetia", "helvetia", "Allianz", "allianz", "Carrefour", "carrefour",
             "Ethias", "ethias", "DLH", "sdworx", "SD Worx", "SDWorx",
             "mortgage-ops", "anon-ops",
             "Strictly Confidential"]
WORD = ["ALZ", "dlh", "alz"]
SKIP_DIRS = {".git", ".github", "node_modules"}
TEXT = (".html", ".md", ".json", ".js", ".css", ".txt", ".py", ".svg")


def hits(text):
    found = []
    for n in FORBIDDEN:
        c = text.count(n)
        if c:
            found.append("%s x%d" % (n, c))
    for n in WORD:
        c = len(re.findall(r"\b%s\b" % re.escape(n), text))
        if c:
            found.append("%s x%d" % (n, c))
    return found


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    me = os.path.basename(__file__)
    checked, bad = 0, []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in sorted(filenames):
            if not f.endswith(TEXT):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), root)
            if rel == me:
                continue
            try:
                text = open(os.path.join(dirpath, f), encoding="utf-8").read()
            except UnicodeDecodeError:
                continue
            checked += 1
            h = hits(text)
            print("  %-6s %s%s" % ("LEAK" if h else "ok", rel, ("   " + ", ".join(h)) if h else ""))
            if h:
                bad.append(rel)
    print("")
    print("%d files checked, %d carrying something that must not be public" % (checked, len(bad)))
    if bad:
        print("DO NOT COMMIT. Fix these first:")
        for b in bad:
            print("   " + b)
        return 1
    print("clean - safe to commit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
