# Gateway Tracker Upgrade Checklist

- [x] Restore the static Vite build after the unnecessary full-stack upgrade.
- [x] Keep GitHub Pages deployment as the target; do not require OAuth credentials, a database, or an always-on server.
- [x] Audit the current local-first tracker, sync flow, and Pages workflow for portability risks.
- [x] Rework the mobile shell around bottom navigation and a one-handed daily check-in flow.
- [x] Add accessible labels, focus states, reduced-motion handling, and touch target validation.
- [x] Memoize derived stats, avoid unnecessary cloning/renders, and add defensive validation for daily logs.
- [x] Add offline/retry states, safer unsynced-change indicators, and recoverable sync error handling without accounts.
- [x] Make generated visual assets portable for GitHub Pages rather than dependent on preview-specific paths.
- [x] Evaluate Rust/WASM against bundle and latency cost; document the decision and omit it unless it wins a measured hot path.
- [x] Add tests for streaks, date ranges, category totals, export shape, and sync conflict handling.
- [x] Verify desktop/mobile screens, build, type-check, and GitHub Pages artifact output.
- [x] Save an upgrade checkpoint and document deployment prerequisites.
- [x] Diagnose the supplied GitHub Actions job log and identify the exact failing step.
- [x] Apply the minimal GitHub Pages workflow or build configuration fix.
- [x] Re-run the equivalent static CI checks and update the existing pull request.
- [x] Record direct-to-main as the default GitHub delivery policy for this tracker.
- [x] Cherry-pick the remaining verified workflow fix directly onto main after branch divergence, without a pull request.
