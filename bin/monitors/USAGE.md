# Monitor Switching - Quick Usage Guide

## Commands Available

### Single Monitor Switching
- `m0` - Switch to **ASUS monitor** (DP-2) - 3440x1440@100Hz
- `m1` - Switch to **Iiyama monitor** (DP-4) - 3440x1440@100Hz

### Monitor Information
- `mlist` - List all available monitors with specs

### Restore/Reset
- `mreset` - Restore previous monitor configuration

## Quick Start

```bash
# To use immediately (or restart terminal)
source ~/.zshrc

# List all your monitors
mlist

# Switch to ASUS monitor
m0

# Switch to Iiyama monitor
m1

# Go back to previous setup
mreset
```

## What Each Command Does

### `m0` (ASUS Monitor)
- Enables: DP-2 (ASUS 34" UltraWide)
- Resolution: 3440x1440 at 100Hz
- Disables: All other monitors
- Backs up current config automatically

### `m1` (Iiyama Monitor)  
- Enables: DP-4 (Iiyama 34" UltraWide)
- Resolution: 3440x1440 at 100Hz
- Disables: All other monitors
- Backs up current config automatically

## How It Works

1. **Backup**: Automatically saves your current configuration
2. **Configure**: Creates proper XML configuration for GNOME
3. **Apply**: Triggers GNOME to reload display settings
4. **Feedback**: Shows exactly what's happening

## Troubleshooting

- **No immediate change**: Wait 5-10 seconds, move mouse/press key
- **Still not working**: Try logging out and back in
- **Want to go back**: Use `mreset` to restore previous config
- **Check what happened**: Look in `~/bin/monitors/configs/` for backups

## File Locations

- Scripts: `~/bin/monitors/`
- Backups: `~/bin/monitors/configs/`
- GNOME config: `~/.config/monitors.xml`
- Aliases: `~/.zshrc`