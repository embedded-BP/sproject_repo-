# STM32 USB Monitor

A desktop application for real-time monitoring of **Voltage**, **Current**, and **Power** data streamed from an STM32 microcontroller over a USB/Serial connection.

---

## Features

- Live display of Voltage (V), Current (A), and Power (W) in large, easy-to-read value cards
- Real-time scrolling graphs for each measurement channel
- Serial port selection (COM1–COM5) with configurable baud rate (9600 / 19200 / 57600 / 115200)
- Session runtime timer
- Raw data panel at the bottom for raw serial output inspection
- Full menu bar: File, Connection, View, Settings, Tools, Help
- Log export to CSV and PDF (planned)
- Light and Dark theme support (planned)

---

## Requirements

| Dependency | Version |
|---|---|
| Python | 3.10+ |
| tkinter | bundled with CPython |

No third-party packages are required to run the GUI. The GitHub Actions workflow additionally uses `openai` and `GitPython` for automated documentation.

---

## Project Structure

```
sproject_repo-/
├── volt_amp_disp.py          # Main application entry point
├── Docs/
│   ├── README.md             # This file
│   ├── API_Documentation.md  # Code-level reference
│   ├── CHANGELOG.md          # Version history
│   ├── Release_Notes.md      # User-facing release notes
│   └── User_Manual.md        # End-user operating guide
├── Scripts/
│   └── ai_documentation.py   # GitHub Actions doc-generator script
├── html/                     # Doxygen HTML output
├── latex/                    # Doxygen LaTeX output
└── .github/
    └── workflows/
        └── ai-docs.yml       # CI workflow for automated doc updates
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd sproject_repo-
```

### 2. Run the application

```bash
python volt_amp_disp.py
```

The window opens at **1250 × 760 px**. Connect your STM32 device before pressing **Connect**.

---

## Connecting to the STM32 Device

1. Plug the STM32 board into a USB port.
2. Select the correct **COM Port** from the dropdown (use Device Manager to find it).
3. Set **Baud** to match the firmware configuration (default: `115200`).
4. Click **Refresh** to rescan available ports, then click **Connect**.
5. The status label changes from `Disconnected` to `Connected` and the runtime timer starts.

---

## CI / Automated Documentation

Pushing to the `develop` branch triggers `.github/workflows/ai-docs.yml`, which:

1. Checks out the repository.
2. Runs `Scripts/ai_documentation.py` (requires `OPENAI_API_KEY` secret).
3. Commits any updated files under `Docs/` back to the branch automatically.

---

## Branch Strategy

| Branch | Purpose |
|---|---|
| `main` | Stable releases |
| `develop` | Active development, CI triggers here |

---

## License

See repository root for license information.
