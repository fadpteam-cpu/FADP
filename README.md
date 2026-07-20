# FADP Architecture — website

Static HTML/CSS/JS website for Fa Design Partners Limited, trading as FADP Architecture.

**Live at:** `https://<your-username>.github.io/<repo-name>/`

## What this is

46 static pages, no build system needed to view. The HTML is regenerated
from Python scripts (`build_pages.py`, `build_services.py`,
`build_subservices.py`, `build_blog.py`); the output files are already
committed and served directly.

## Deploying to GitHub Pages

This repo is set up for GitHub Pages hosting only.

### First-time setup

1. Push this folder to a new GitHub repo (name it whatever you like,
   e.g. `fadp-website`).
2. In GitHub: **Settings → Pages → Source: GitHub Actions**.
3. Every push to `main` will now auto-deploy. The included workflow
   (`.github/workflows/deploy.yml`) handles it.

### Regular deploys

```bash
git add -A
git commit -m "Update copy"
git push
```

The GitHub Action takes 30–60 seconds, then your changes are live.

### Custom domain (optional, later)

If you want `www.fadp.co.uk` pointing at GitHub Pages instead of
GitHub's default URL:

1. In your DNS provider, add a CNAME record for `www` pointing to
   `<your-username>.github.io`.
2. In GitHub → Settings → Pages → Custom domain, enter `www.fadp.co.uk`
   and click Save. GitHub provisions HTTPS automatically.
3. Add a file named `CNAME` at the repo root containing just
   `www.fadp.co.uk` (one line, no trailing content) so the setting
   survives future deploys.

## Editing content

**Small text tweaks:** edit the generated HTML files directly. Commit,
push, done.

**Broader changes (structure, adding a page):** edit the Python build
scripts, run them locally with `python3 build_pages.py && python3
build_services.py && python3 build_subservices.py && python3
build_blog.py`, then commit the regenerated `.html` files.

## Firm details baked into the site

- **Legal name:** Fa Design Partners Limited
- **Trading as:** FADP Architecture
- **Companies House number:** 17331773
- **Registered office:** 66 Paul Street, London EC2A 4NA
- **Email:** design@fadp.co.uk
- **Directors:** Aun Naeem, Fatima Shakeel

## Known items to resolve before public promotion

- **"Architect" is a protected UK title.** The Architects Registration
  Board (arb.org.uk) enforces this. Only individuals on the ARB
  register can call themselves architects. If neither director is
  currently on the register, all instances of "architect(s)" should be
  changed site-wide to "architectural designer(s)". A find-and-replace
  in the Python build scripts will do it in one commit.
- **Placeholder testimonials** (Priya N., Sarah W., Daniel R.). Replace
  with real Google reviews before promotion.
- **Placeholder Google review count** (5.0 from 42) in the reviews
  section label.
- **Stock photography** is currently in every image slot. Real project
  photography, when shot, replaces the URLs in `IMG` at the top of
  `build_pages.py`.
- **Councils strip** (Camden · Islington · Hackney · etc.) — verify
  these are all real prior approvals or trim.
