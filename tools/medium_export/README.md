# Hugo → Medium preparation

The Hugo English page is the canonical source.  This tool produces a separate
import payload and audit manifest; it does not alter the Hugo article and it
never publishes a Medium story.

```sh
python3 tools/medium_export/translate_article.py \
  content/plasma-physics/magnetic-mirror-reflection-force/index.md
python3 tools/medium_export/check_article.py \
  content/plasma-physics/magnetic-mirror-reflection-force/index.md \
  content/plasma-physics/magnetic-mirror-reflection-force/index.en.md
python3 tools/medium_export/prepare_medium.py \
  content/plasma-physics/magnetic-mirror-reflection-force/index.en.md
```

The last command writes `.medium-export/magnetic-mirror-reflection-force.medium.md`
and a JSON manifest.  It removes Hugo's `math-display` wrappers and converts
page-bundle image links to absolute GitHub Pages URLs so that Medium's current
`/p/import` flow can fetch the images after the site is deployed.

The payload intentionally keeps `$...$`, `$$...$$`, and `aligned` source.  A
successful import is not evidence that Medium rendered those formulas.  The
Medium editor has to be checked in the live Draft.  If it does not preserve the
math, the safe fallback is to generate equation images and upload them as
images; the canonical Hugo page is never replaced by that compatibility copy.

Authentication data, cookies, tokens, and browser profiles must remain outside
the repository.
