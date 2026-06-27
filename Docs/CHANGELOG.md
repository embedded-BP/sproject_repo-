# Changelog

All notable changes to **STM32 USB Monitor** are documented here.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).  
Versions follow [Semantic Versioning](https://semver.org/).

---

## [Unreleased] — develop branch

### Added
- Full menu bar with six menus: File, Connection, View, Settings, Tools, Help
- File menu: New Session, Open Log, Save Log, Export CSV/PDF, Print, Exit — with keyboard accelerators
- Connection menu: Refresh Ports (F5), Connect (F7), Disconnect (F8), Port Settings, Auto-Connect on Startup
- View menu: toggles for toolbar / status bar / raw-data panel, per-graph visibility checkbuttons, Zoom sub-menu, Light/Dark theme commands
- Settings menu: COM Port, Baud Rate, Display, Graph, Calibration, and Preferences dialogs
- Tools menu: Data Logger, Serial Monitor, Statistics & Analysis, Clear All Data, Reset Graphs, Run Diagnostics
- Help menu: Documentation (F1), Keyboard Shortcuts, Check for Updates, Report a Bug, About

### Changed
- Replaced flat menu loop with individual, fully-populated menu objects for each category
- All five `Docs/` files written with full content (were empty stubs)

---

## [1.0.1] — 2026-06-27

### Changed
- GitHub Actions workflow (`ai-docs.yml`) updated: added `permissions: contents: write` so the bot can push documentation commits back to `develop`
- `Scripts/ai_documentation.py` updated to append to `Docs/CHANGELOG.md` on every CI run
- Automated documentation update committed by CI pipeline

### Fixed
- Workflow no longer errors when `Docs/CHANGELOG.md` does not yet exist (auto-creates the file)

---

## [1.0.0] — 2026-06-26

### Added
- Initial project scaffold: `volt_amp_disp.py` as the main application file
- `Docs/` folder with placeholder files: README, API_Documentation, CHANGELOG, Release_Notes, User_Manual
- `Scripts/ai_documentation.py` — skeleton AI documentation generator
- `.github/workflows/ai-docs.yml` — CI pipeline triggered on push to `develop`
- Doxygen HTML and LaTeX output under `html/` and `latex/`
- tkinter GUI with:
  - Top toolbar: COM port selector, baud rate selector, Refresh / Connect / Disconnect buttons, status label, runtime timer
  - Three value cards: Voltage (V), Current (A), Power (W) — 350 × 150 px each, Consolas 28 bold
  - Three graph canvases: 250 × 250 px with 25 px grid lines, white background
  - Bottom status bar: raw serial data label, device status label
  - Basic menu bar stub (Connection menu only)
