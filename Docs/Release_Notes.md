# Release Notes — STM32 USB Monitor

---

## v1.0.1 — 2026-06-27

**Type:** Patch release  
**Branch:** develop → main

### What's New

This patch fixes the GitHub Actions CI pipeline so it can write documentation updates back to the repository automatically.

#### CI Fix — Documentation Workflow
- Added `permissions: contents: write` to `ai-docs.yml` so `github-actions` bot has push rights.
- `Scripts/ai_documentation.py` now creates `Docs/CHANGELOG.md` if the file is absent before appending to it, preventing a `FileNotFoundError` on a fresh clone.

### Upgrade Notes

No user-facing changes. Pull the latest `develop` branch to pick up the workflow fix.

---

## v1.0.0 — 2026-06-26

**Type:** Initial release  
**Branch:** main

### What's New

First working release of **STM32 USB Monitor** — a Python desktop application for real-time display of Voltage, Current, and Power measurements from an STM32 microcontroller via USB.

#### GUI Application (`volt_amp_disp.py`)

| Section | Description |
|---|---|
| **Top Toolbar** | COM port selector (COM1–COM5), baud rate selector (9600–115200), Refresh / Connect / Disconnect buttons, live status label, runtime timer |
| **Value Cards** | Three large `LabelFrame` cards — Voltage, Current, Power — showing the live reading in Consolas 28 bold font |
| **Graph Area** | Three 250 × 250 px canvases with a 25 px grey grid, one per measurement channel |
| **Status Bar** | Raw serial data line and device status at the bottom of the window |

#### Infrastructure
- GitHub Actions workflow (`ai-docs.yml`) triggers on every push to `develop` and runs the documentation generator script.
- Doxygen HTML and LaTeX documentation stubs generated under `html/` and `latex/`.

### Known Limitations (v1.0.0)

- Serial port is **not yet connected** — the GUI displays placeholder values (`0.00 V`, `0.00 A`, `0.00 W`). Live data reading via `pyserial` is planned for v1.1.
- Menu items have no `command=` handlers wired up. All menu actions are visual stubs only.
- Graphs do not scroll or update — static grid canvases only.
- COM port list is hardcoded (`COM1`–`COM5`); dynamic port discovery is planned.
- Theme switching (Light / Dark) is not yet implemented.

### System Requirements

| Item | Requirement |
|---|---|
| OS | Windows 10 / 11 (primary), Linux/macOS untested |
| Python | 3.10 or newer |
| tkinter | Bundled with CPython — no separate install needed |
| Hardware | STM32 board with USB CDC firmware (for live data) |

---

## Roadmap

| Version | Target Features |
|---|---|
| v1.1 | Live serial read via `pyserial`, real-time graph scrolling, dynamic COM port discovery |
| v1.2 | CSV / PDF log export, session save/load |
| v1.3 | Dark theme, calibration dialog, statistics panel |
| v2.0 | Multi-device support, plugin architecture |
