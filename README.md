# FADP Architecture — Website

Marketing site for FADP Architecture. Static HTML/CSS/JS, no build step, no framework.

## Structure

```
index.html          Page markup
css/styles.css      All styles (design tokens at the top in :root)
js/main.js          Form handlers + fee-proposal wizard
assets/img/         Partner logos + brand logo SVGs
favicon.svg / .png  Site icon
```

## Run locally

Open `index.html` in a browser, or serve it:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

## Deploy — GitHub Pages

1. Push this repo to GitHub
2. Repo **Settings → Pages → Source: Deploy from a branch → main / (root)**
3. Site goes live at `https://<user>.github.io/<repo>/` (add a custom domain in the same settings screen)

Also works as-is on Netlify (drag the folder onto app.netlify.com/drop) or Vercel (`npx vercel`).

## Before launch — placeholder checklist

Search and replace in `index.html`:

- [ ] `020 0000 0000` / `+442000000000` — phone (header, contact, footer)
- [ ] `studio@fadp.com` — email (also in `js/main.js` form handlers)
- [ ] `Address line one / two / Postcode` — studio address (contact + footer)
- [ ] `No. 00000000` — Companies House number (footer)
- [ ] `5.0` / `42 reviews` — real Google review figures (hero + footer badge)
- [ ] Project names, areas, years in the work grid
- [ ] All `images.unsplash.com` URLs — replace with real project photography (put files in `assets/img/`)
- [ ] Testimonial quotes and names — real reviews, used with permission
- [ ] `/blog` nav link — point somewhere real or remove
- [ ] Social links in the footer (`href="#"`)

## Connect the forms

Both forms (consultation + fee-proposal wizard) currently open the visitor's mail
client with answers pre-filled — fine for testing, not for production.

To capture submissions: create a free endpoint at [Formspree](https://formspree.io)
(or use Netlify Forms), then in `js/main.js` replace the two
`window.location.href = "mailto:..."` lines with a `fetch()` POST to the endpoint.
Both handlers are marked with comments.

## Compliance (read before publishing)

- **"Architect" is a protected title in the UK.** Only use it if the relevant people
  are on the ARB register; otherwise change the wording to "architectural designers".
- Only display partner logos (RICS, Houzz, Planning Portal) the practice genuinely
  holds or uses, per each organisation's rules.
- Review figures and testimonials must be real and verifiable.
- Get written consent before using photography of clients' homes.

## Design system

| Token | Value |
|---|---|
| Brand | PANTONE 20-0146 TPM "Magnetic Blue" · `#05308C` |
| Text | `#141414` |
| Muted | `#6E6E6A` |
| Background | `#FBFBFA` / `#F2F2EF` |
| Hairline | `#E2E1DC` |
| Type | Manrope 300/400/500/700 → Inter → system UI |

House style: no em dashes anywhere — middle dots ( · ) for label pairs,
"to" for ranges. Full rules in the FADP brand guidelines (separate package).
