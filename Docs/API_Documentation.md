# API Documentation — STM32 USB Monitor

This document describes every GUI widget, variable, and structural section in `volt_amp_disp.py`.

---

## Module Overview

**File:** `volt_amp_disp.py`  
**Framework:** Python `tkinter` + `tkinter.ttk`  
**Entry point:** module-level code; the application runs when the file is executed directly.

---

## Window Configuration

```python
root = tk.Tk()
root.title("STM32 USB Monitor")
root.geometry("1250x760")
```

| Property | Value |
|---|---|
| Window title | `STM32 USB Monitor` |
| Default size | `1250 × 760` pixels |
| Resizable | Yes (default tkinter behaviour) |

---

## Menu Bar

The menu bar is attached to `root` via `root.config(menu=menubar)`.  
All menus use `tearoff=0`.

### File Menu (`file_menu`)

| Label | Accelerator | Description |
|---|---|---|
| New Session | Ctrl+N | Start a fresh monitoring session |
| Open Log… | Ctrl+O | Open a previously saved log file |
| Save Log… | Ctrl+S | Save the current session log |
| Export as CSV… | — | Export data to CSV format |
| Export as PDF… | — | Export data to PDF format |
| Print… | Ctrl+P | Print current view |
| Exit | Alt+F4 | Close the application |

### Connection Menu (`conn_menu`)

| Label | Accelerator | Description |
|---|---|---|
| Refresh Ports | F5 | Rescan available COM ports |
| Connect | F7 | Open the selected serial port |
| Disconnect | F8 | Close the active serial connection |
| Port Settings… | — | Advanced serial port configuration |
| Auto-Connect on Startup | — | Toggle auto-connect behaviour |

### View Menu (`view_menu`)

| Label | Type | Description |
|---|---|---|
| Show Toolbar | Checkbutton | Toggle top toolbar visibility |
| Show Status Bar | Checkbutton | Toggle bottom status bar |
| Show Raw Data Panel | Checkbutton | Toggle raw data label |
| Show Voltage Graph | Checkbutton | Toggle Voltage canvas |
| Show Current Graph | Checkbutton | Toggle Current canvas |
| Show Power Graph | Checkbutton | Toggle Power canvas |
| Zoom → Zoom In | Command | Ctrl++ |
| Zoom → Zoom Out | Command | Ctrl+- |
| Zoom → Reset Zoom | Command | Ctrl+0 |
| Light Theme | Command | Apply light colour theme |
| Dark Theme | Command | Apply dark colour theme |

### Settings Menu (`settings_menu`)

| Label | Description |
|---|---|
| COM Port Settings… | Configure port number and parameters |
| Baud Rate Settings… | Set or change baud rate |
| Display Settings… | Font size, unit display options |
| Graph Settings… | Scroll speed, Y-axis range, colours |
| Calibration Settings… | Offset/gain calibration for each channel |
| Preferences… (Ctrl+,) | General application preferences |

### Tools Menu (`tools_menu`)

| Label | Accelerator | Description |
|---|---|---|
| Data Logger | — | Start/stop continuous data logging to file |
| Serial Monitor… | — | Open a raw serial terminal window |
| Statistics & Analysis… | — | Min / Max / Average over the session |
| Clear All Data | Ctrl+Del | Wipe all in-memory readings and graphs |
| Reset Graphs | — | Clear graph canvases only |
| Run Diagnostics… | — | Check port health and data integrity |

### Help Menu (`help_menu`)

| Label | Accelerator | Description |
|---|---|---|
| Documentation | F1 | Open `Docs/User_Manual.md` |
| Keyboard Shortcuts… | — | Display all keyboard shortcuts |
| Check for Updates… | — | Query for a newer release |
| Report a Bug… | — | Open the issue tracker |
| About STM32 USB Monitor | — | Version and copyright information |

---

## Top Toolbar (`top`)

**Widget:** `ttk.Frame`, packed with `fill="x"`, padding 8 px.

| Widget | Variable / Value | Grid position | Description |
|---|---|---|---|
| `ttk.Label` | `"COM Port"` | row=0, col=0 | Label for port selector |
| `ttk.Combobox` `ports` | `["COM1"…"COM5"]`, default index 4 (`COM5`) | row=0, col=1 | Serial port selector |
| `ttk.Label` | `"Baud"` | row=0, col=2 | Label for baud selector |
| `ttk.Combobox` `baud` | `["9600","19200","57600","115200"]`, default index 3 (`115200`) | row=0, col=3 | Baud rate selector |
| `ttk.Button` | `"Refresh"` | row=0, col=4 | Trigger port rescan |
| `ttk.Button` | `"Connect"` | row=0, col=5 | Open serial connection |
| `ttk.Button` | `"Disconnect"` | row=0, col=6 | Close serial connection |
| `ttk.Label` | `textvariable=status` | row=0, col=7 | Connection state string |
| `ttk.Label` | `textvariable=runtime` | row=0, col=8 | Elapsed session time |

### StringVar references

| Variable | Initial value | Description |
|---|---|---|
| `status` | `"Disconnected"` | Reflects current connection state |
| `runtime` | `"Runtime : 00:00:00"` | HH:MM:SS elapsed time since connect |

---

## Value Cards (`cards`)

**Widget:** `ttk.Frame`, packed with padding 10 px.  
Three `tk.LabelFrame` widgets arranged in a single row (`grid row=0`).

| Index | Channel | Default text | Frame size |
|---|---|---|---|
| 0 | Voltage | `0.00 V` | 350 × 150 px |
| 1 | Current | `0.00 A` | 350 × 150 px |
| 2 | Power | `0.00 W` | 350 × 150 px |

Each card contains a centered `ttk.Label` with font `Consolas 28 bold`.  
`grid_propagate(False)` prevents the label from resizing the frame.

---

## Graph Canvases (`graphs`)

**Widget:** `ttk.Frame`, packed with padding 10 px.  
Three `tk.LabelFrame` + `tk.Canvas` pairs arranged in a single row.

| Index | Channel | Canvas size | Background |
|---|---|---|---|
| 0 | Voltage Graph | 250 × 250 px | white |
| 1 | Current Graph | 250 × 250 px | white |
| 2 | Power Graph | 250 × 250 px | white |

Each canvas has a 25 px grid drawn in `#ddd` (both horizontal and vertical lines at every 25-pixel step).

---

## Bottom Status Bar (`bottom`)

**Widget:** `ttk.Frame`, packed with `fill="x"`, `side="bottom"`, padding 8 px.

| Widget | Variable | Default value |
|---|---|---|
| `ttk.Label` | `textvariable=raw` | `"Raw Data : Waiting…"` |
| `ttk.Label` | static text | `"Device Status"` |

| Variable | Initial value | Description |
|---|---|---|
| `raw` | `"Raw Data : Waiting…"` | Last raw serial line received |

---

## Data Flow (Planned / Stub)

```
STM32 firmware
    └─► USB CDC / Virtual COM Port
            └─► Python serial.Serial (to be wired)
                    ├─► raw StringVar  (bottom bar)
                    ├─► Voltage card label
                    ├─► Current card label
                    ├─► Power card label
                    ├─► Voltage canvas (scrolling plot)
                    ├─► Current canvas (scrolling plot)
                    └─► Power canvas  (scrolling plot)
```
