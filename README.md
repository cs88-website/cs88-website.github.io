# c88c.org

| File | Role |
|---|---|
| `CNAME` | the custom domain (mirrors the repo's Pages settings) |
| `index.html` | `c88c.org` → client-side redirect to the current semester |
| `404.html` | any unknown path: assignment links (`/hw/...`) redirect into the current semester; anything else shows a 404. Past semesters are served directly at `c88c.org/<sem>/` by their own repos, so they never reach this file |

## Each semester

Update the semester in `index.html` (two places) and `CURRENT` in `404.html`.
A new semester repo named `<sem>` is served at `c88c.org/<sem>/`
automatically, but check **Enforce HTTPS** in its Pages settings — the
setting is per repo, and without it `http://c88c.org/<sem>/...` serves
plain HTTP instead of redirecting to https.
