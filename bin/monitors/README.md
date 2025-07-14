# Instant Monitor Switching for GNOME/Wayland ⚡

A powerful command-line solution for instant monitor switching on Fedora with GNOME/Wayland. Features safety validation, environment detection, and sub-second switching using GNOME's official `gdctl` utility.

## ✨ Features

- **Instant Switching**: Sub-second monitor configuration changes
- **Safety Validation**: Prevents switching to disconnected monitors
- **Environment Detection**: Automatically detects home/laptop/partial setups
- **Custom Layouts**: Optimized triple monitor configuration with maximum refresh rates
- **Automatic Backups**: Safe configuration management with rollback capability
- **Smart Aliases**: Simple commands for daily use

## 🚀 Quick Start

### Essential Commands
```bash
m0          # Switch to ASUS monitor (3440x1440@100Hz)
m1          # Switch to Iiyama monitor (3440x1440@180Hz) 
m3          # Custom triple monitor layout (all monitors)
mavailable  # Show only connected monitors
```

### Monitor Layout (Triple Mode)
- **LG (DP-3)**: Portrait left, 2560x1080@60Hz
- **Iiyama (DP-4)**: Primary top-right, 3440x1440@180Hz
- **ASUS (DP-2)**: Secondary bottom-right, 3440x1440@100Hz

## 📖 Usage

### Basic Commands
```bash
# Switch to specific monitors
gdctl-instant.py DP-2      # ASUS monitor
gdctl-instant.py DP-4      # Iiyama monitor  
gdctl-instant.py eDP-1     # Laptop display
gdctl-instant.py triple    # Custom triple layout

# Information commands
gdctl-instant.py show      # Current configuration
gdctl-instant.py available # Connected monitors only
gdctl-instant.py list      # All available monitors
```

### Environment Detection
The script automatically detects your current setup:
- **🏠 Full home setup**: All 3 external monitors connected
- **💻 Laptop mode**: Only built-in display available
- **⚡ Partial setup**: Some external monitors connected

## 🛡️ Safety Features

### Monitor Presence Validation
```bash
# When away from home setup
m0  # ❌ Monitor DP-2 (ASUS) is not connected!
    # ℹ️  You appear to be on laptop-only mode (away from home setup)
```

### Smart Error Messages
- Clear feedback about missing monitors
- Suggestions for available alternatives
- Environment context awareness

## 🔧 Technical Details

### Requirements
- Fedora Linux with GNOME on Wayland
- `gdctl` utility (included with GNOME)
- Python 3 (for the script)

### Monitor Configuration
- **ASUS (DP-2)**: VG34VQEL1A, 3440x1440@100Hz
- **Iiyama (DP-4)**: PL3481WQ, 3440x1440@180Hz  
- **LG (DP-3)**: LG ULTRAWIDE, 2560x1080@60Hz
- **Laptop (eDP-1)**: Built-in display, 2880x1920@60Hz

### Automatic Backups
- Configuration backed up before each change
- Stored in `~/bin/monitors/configs/`
- Timestamped for easy restoration

## 📂 Installation

Already installed and configured! Aliases are available in your shell:
```bash
source ~/.zshrc  # Reload aliases if needed
```

## 🎯 Perfect for

- **Daily workflow**: Quick switching between monitor setups
- **Remote work**: Safe operation when away from home setup  
- **Gaming/productivity**: Instant layout changes
- **Multi-monitor optimization**: Maximum refresh rates automatically

---

**Powered by GNOME's gdctl** | **Instant switching** | **Production ready**