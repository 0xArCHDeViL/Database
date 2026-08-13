# Gateway Tracker

Gateway Tracker is a private, local-first daily operating ledger for two parallel commitments: a Tom Holland-inspired bodyweight workout routine and Japanese study toward JLPT N3. The interface follows the **Swiss Training Ledger** direction: warm paper, charcoal ink, signal red, asymmetric sections, and small metadata labels that make the dashboard feel like a field notebook rather than a generic admin panel.

## What is included

The daily log supports either or both workout toggles. The ladder records round count and minutes, while Cindy records AMRAP rounds and minutes. Japanese study supports two deliberate paths: a **batch session** for up to 1,000 deduplicated Kotoba, Kanji, or Bunpou items pasted in one operation, and optional manual detail when a reading, example sentence, or grammar note is genuinely useful. Free minutes and one practical note complete the daily checkpoint.

The Rhythm section includes a 12-week contribution heatmap, current and longest streaks, a 14-day line chart, range-aware summary cards, and a category breakdown across Kotoba, Kanji, Bunpou, and Workout. The Export section produces a formatted XLSX workbook with `Summary`, `Daily Log`, `Japanese Detail`, `Japanese Batches`, and `Workout Log` sheets, including frozen headers and readable widths.

## Daily pilot, reminders, and batch formats

The daily pilot turns historic logs into one next action. It favours the least-represented Japanese category over the previous 14 days, starts from the configurable Japanese baseline, raises the target slightly only when rhythm is stable, and applies a bounded **re-entry discount** after missed days rather than creating a punishing backlog. The user sees the target rationale in the interface.

The local focus alarm runs a countdown, visual completion state, optional sound, and browser notification permission flow. A configurable daily nudge is evaluated while Gateway is open or installed. Because this is a static GitHub Pages app, it **cannot guarantee an alarm after the browser/app has been fully closed**; the UI states this explicitly instead of implying a background service.

For batch capture, paste one item per line, or separate items with commas or semicolons. Numbered/bulleted prefixes are removed and duplicates are discarded. The batch worksheet exports one session per row, with a newline-preserved item list, so 500 items stay portable without creating 500 manual input fields.

## Storage model

The browser is the local source of truth. The app writes a versioned `gateway-tracker-v1` payload to both the available `window.storage` adapter and `localStorage` as a fallback. A blank Japanese row is not counted as progress until its content is filled. The data model is intentionally append-friendly and includes an `updatedAt` timestamp on each daily log.

## GitHub backup model

GitHub sync is explicit and runs from the browser. It creates or reuses a dedicated branch, appends an immutable JSON snapshot under `data/journal/<timestamp>.json`, updates `data/gateway-tracker-latest.json`, and optionally creates or reuses an open pull request. The app serializes the two file writes and fetches the current SHA before replacing the latest pointer, so a sync does not silently erase prior snapshots.

The sync dialog expects a **fine-grained personal access token** with access limited to the private data repository. Use `Contents: Read and write`; add `Pull requests: Read and write` only if pull-request mode is enabled. The token is held in component state and is not written to local storage or committed to the repository. For higher security, use a dedicated private data repository and revoke the token when finished.

This architecture intentionally does not place a token in GitHub Actions secrets for browser access. GitHub Pages is a static site; a token embedded in a public build would be extractable. The browser-to-GitHub flow is suitable for one personal user who explicitly supplies a narrowly scoped token. A multi-user or fully unattended flow should use a backend or GitHub App instead.

## GitHub Pages deployment

1. Create a repository and place this project on its `main` branch.
2. In **Settings → Pages**, choose **GitHub Actions** as the source.
3. Push to `main` or run **Deploy Gateway Tracker to GitHub Pages** manually.
4. The workflow installs Node 22 and pnpm, builds `dist/public`, uploads the Pages artifact, and deploys it with the required `pages: write` and `id-token: write` permissions.

The Vite base path automatically becomes `/<repository-name>/` inside GitHub Actions and remains `/` in the local preview. The visual identity is rendered with CSS and inline SVG, so no preview-only asset path is required for GitHub Pages deployment.

## Source delivery policy

For this personal tracker, verified changes are committed and pushed **directly to `main`**; pull requests are not part of the default delivery path. Before each direct push, run the unit suite, type-check, and production build. If a prepared branch has diverged from current `main`, preserve remote history by cherry-picking only the verified commits onto an up-to-date local `main`, then push normally. Never force-push or overwrite unrelated repository content.

## Performance and WASM decision

The tracker keeps aggregation bounded by the selected date range and journal size, caps date-range expansion at 3,660 days, sanitizes malformed values before save, and lazy-loads SheetJS only when an XLSX export is requested. In the current production build, moving SheetJS out of the initial path reduced the main JavaScript chunk from **928.11 kB** to **643.31 kB** before compression; XLSX now lives in a separate **429.49 kB** chunk downloaded only at export time. The tracker unit suite completes in roughly **0.3 seconds** in the project environment, and the core dashboard does not run a compute-heavy algorithm. Adding a Rust/WASM payload would increase download, initialization, and debugging cost without improving the user-visible hot path, so it is intentionally omitted. Reconsider WASM only if a future feature introduces large-scale offline analysis or cryptographic work that has been profiled as a real bottleneck.

## Local development

```bash
pnpm install
pnpm dev
pnpm check
pnpm build
pnpm exec vitest run
```

The app is intentionally frontend-only. `server/` remains the template compatibility placeholder and is not used for persistence or GitHub credentials.

## Reference notes

The workout labels and structure are based on the user-provided [Man of Many article](https://manofmany.com/culture/fitness/tom-holland-spider-man-workout-diet-plan). That article describes the 1,500-rep ladder as 1–10 and back down using pull-ups, dips, press-ups, sit-ups, and air squats, and Cindy as a 20-minute AMRAP of 5 pull-ups, 10 press-ups, and 15 squats. The tracker is a logging tool, not medical advice; scale movements and stop when appropriate.

The deployment workflow follows the official [GitHub Pages custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), and the backup implementation follows the official [repository Contents API documentation](https://docs.github.com/en/rest/repos/contents) for Base64 content, commit messages, branches, and SHA-aware file updates.
