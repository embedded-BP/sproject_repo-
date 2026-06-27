# User Manual — STM32 USB Monitor

**Version:** 1.0.1  
**Application:** STM32 USB Monitor  
**Platform:** Windows 10 / 11

---

## Table of Contents

1. [Overview](#1-overview)
2. [Installation](#2-installation)
3. [Starting the Application](#3-starting-the-application)
4. [Application Layout](#4-application-layout)
5. [Connecting to the STM32 Device](#5-connecting-to-the-stm32-device)
6. [Reading Live Measurements](#6-reading-live-measurements)
7. [Menu Reference](#7-menu-reference)
8. [Keyboard Shortcuts](#8-keyboard-shortcuts)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. Overview

**STM32 USB Monitor** displays live **Voltage**, **Current**, and **Power** data sent by an STM32 microcontroller over a USB serial (CDC) connection. The application shows numerical values in large cards and plots them on scrolling graphs so you can see trends at a glance.

---

## 2. Installation

### Requirements

- **Python 3.10 or newer** — download from [python.org](https://www.python.org)
- `tkinter` — included with the standard CPython installer (no extra install needed)

### Steps

1. Clone or download the repository to your PC.
2. Open a terminal in the project folder.
3. Run:
   ```
   python volt_amp_disp.py
   ```

No `pip install` is required for the GUI itself.

---

## 3. Starting the Application

Double-click `volt_amp_disp.py` in File Explorer, or run it from a terminal:

```
python volt_amp_disp.py
```

The main window opens at 1250 × 760 pixels. All value cards start at `0.00` and the status shows **Disconnected** until you connect.

---

## 4. Application Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│  File  Connection  View  Settings  Tools  Help          (menu bar)  │
├──────┬──────┬─────────┬──────────┬──────────┬───────────────────────┤
│ COM  │ Baud │ Refresh │ Connect  │Disconnect│ Status   │  Runtime   │
│ Port │      │         │          │          │          │            │
├──────┴──────┴─────────┴──────────┴──────────┴──────────┴────────────┤
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐               │
│  │  Voltage    │   │  Current    │   │   Power     │  (cards)      │
│  │  0.00 V     │   │  0.00 A     │   │  0.00 W     │               │
│  └─────────────┘   └─────────────┘   └─────────────┘               │
├──────────────────────────────────────────────────────────────────────┤
│  [Voltage Graph]     [Current Graph]     [Power Graph]  (graphs)    │
├──────────────────────────────────────────────────────────────────────┤
│  Raw Data : Waiting…                                                 │
│  Device Status                                   (status bar)       │
└──────────────────────────────────────────────────────────────────────┘
```

### Sections

| Section | Description |
|---|---|
| **Menu bar** | Access all functions via File, Connection, View, Settings, Tools, Help |
| **Toolbar** | Quick controls for port, baud, connect/disconnect and live status |
| **Value cards** | Large live readout for Voltage (V), Current (A), Power (W) |
| **Graphs** | Scrolling time-series plot for each channel |
| **Status bar** | Last raw serial line received; device connection state |

---

## 5. Connecting to the STM32 Device

1. Plug the STM32 board into a USB port on your PC.
2. Open **Device Manager** (Win + X → Device Manager) and expand **Ports (COM & LPT)** to find the COMx number assigned to the board.
3. In the application toolbar, click the **COM Port** dropdown and select the matching port.
4. Set the **Baud** dropdown to the rate configured in the STM32 firmware (typically `115200`).
5. Click **Refresh** to re-scan if the port is not listed.
6. Click **Connect**.

The status label changes to **Connected** and the runtime timer starts counting up (`Runtime : 00:00:00`).

To disconnect, click **Disconnect** or use **Connection → Disconnect (F8)**.

---

## 6. Reading Live Measurements

Once connected, the three value cards update automatically:

| Card | Unit | Description |
|---|---|---|
| Voltage | V | DC bus or output voltage |
| Current | A | Load current |
| Power | W | Calculated power (V × I) |

The **Graphs** below each card plot the value over time. The horizontal axis is time; the vertical axis scales to the data range.

The **Raw Data** label at the bottom shows the last unparsed line received from the device — useful for verifying the serial stream is active.

---

## 7. Menu Reference

### File

| Item | Shortcut | Action |
|---|---|---|
| New Session | Ctrl+N | Clear current data and start fresh |
| Open Log… | Ctrl+O | Load a previously saved `.log` file |
| Save Log… | Ctrl+S | Save the current session to a file |
| Export as CSV… | — | Write all readings to a `.csv` file |
| Export as PDF… | — | Save a formatted PDF report |
| Print… | Ctrl+P | Print the current view |
| Exit | Alt+F4 | Close the application |

### Connection

| Item | Shortcut | Action |
|---|---|---|
| Refresh Ports | F5 | Rescan and update the COM port list |
| Connect | F7 | Open the selected port |
| Disconnect | F8 | Close the active port |
| Port Settings… | — | Set stop bits, parity, flow control |
| Auto-Connect on Startup | — | Toggle: connect automatically when the app opens |

### View

| Item | Action |
|---|---|
| Show Toolbar | Toggle the top toolbar on/off |
| Show Status Bar | Toggle the bottom bar on/off |
| Show Raw Data Panel | Toggle the raw data label |
| Show Voltage / Current / Power Graph | Show or hide individual graphs |
| Zoom In / Out / Reset | Scale graph time axis |
| Light Theme / Dark Theme | Switch the colour scheme |

### Settings

| Item | Action |
|---|---|
| COM Port Settings… | Advanced port parameters (stop bits, parity, flow control) |
| Baud Rate Settings… | Set a custom baud rate not in the dropdown |
| Display Settings… | Decimal places, font size, unit labels |
| Graph Settings… | Y-axis range, scroll speed, line colour |
| Calibration Settings… | Per-channel gain and offset correction |
| Preferences… (Ctrl+,) | General application preferences |

### Tools

| Item | Shortcut | Action |
|---|---|---|
| Data Logger | — | Start writing all readings to a timestamped file |
| Serial Monitor… | — | Open a raw serial terminal for two-way communication |
| Statistics & Analysis… | — | Show min / max / average for the current session |
| Clear All Data | Ctrl+Del | Erase all in-memory data and reset graphs |
| Reset Graphs | — | Clear graph lines without erasing stored data |
| Run Diagnostics… | — | Check port health and verify data framing |

### Help

| Item | Shortcut | Action |
|---|---|---|
| Documentation | F1 | Open this User Manual |
| Keyboard Shortcuts… | — | List all shortcuts |
| Check for Updates… | — | Check for a newer release online |
| Report a Bug… | — | Open the issue tracker |
| About STM32 USB Monitor | — | Version number and copyright |

---

## 8. Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| Ctrl+N | New Session |
| Ctrl+O | Open Log |
| Ctrl+S | Save Log |
| Ctrl+P | Print |
| Alt+F4 | Exit |
| F5 | Refresh Ports |
| F7 | Connect |
| F8 | Disconnect |
| F1 | Open Documentation |
| Ctrl++ | Zoom In |
| Ctrl+- | Zoom Out |
| Ctrl+0 | Reset Zoom |
| Ctrl+Del | Clear All Data |
| Ctrl+, | Preferences |

---

## 9. Troubleshooting

### The COM port I need is not in the list
- Click **Refresh** (F5) or use **Connection → Refresh Ports**.
- Check Device Manager to confirm the device is enumerated.
- Try unplugging and re-plugging the USB cable.
- Ensure the STM32 USB CDC firmware is loaded correctly.

### Status shows "Connected" but values stay at 0.00
- Verify the baud rate matches the firmware setting.
- Check the raw data bar at the bottom — if it shows data, the parser may need updating to match the firmware message format.
- Use **Tools → Serial Monitor** to see the raw stream.

### Application window does not open
- Make sure Python 3.10+ is installed: `python --version`
- Make sure tkinter is available: `python -m tkinter` (a small test window should appear)
- Run from a terminal to see any error messages.

### Graphs are not updating
- Live graph scrolling requires an active serial connection with valid data packets.
- In the current version (v1.0.x) graphs are static placeholders; live updates are planned for v1.1.
