# Monitor Configuration Switcher for GNOME/Wayland

A simple command-line tool to switch between different monitor configurations on Fedora with GNOME running on Wayland.

## Installation

The scripts are already installed in `~/bin/monitors/`. The aliases have been added to your `.zshrc` file.

To use the aliases immediately without restarting your terminal:
```bash
source ~/.zshrc
```

## Usage

### Available Commands

- `mlist` - List all connected monitors and available profiles
- `m1` - Switch to single monitor mode (Iiyama 34" only)
- `m2` - Switch to dual monitor mode (both 34" monitors)
- `m3` - Switch to triple monitor mode (all external monitors)
- `mall` - Enable all monitors (including laptop screen)
- `mreset` - Restore the last working configuration

### Examples

```bash
# See what monitors are connected
mlist

# Switch to single monitor
m1

# Go back to previous configuration
mreset
```

## How It Works

1. The tool modifies the GNOME display configuration file (`~/.config/monitors.xml`)
2. It creates backups before making any changes
3. Changes are applied by triggering a GNOME settings reload

## Important Notes

- **Wayland Limitation**: Unlike X11, Wayland doesn't allow real-time monitor switching via xrandr
- **Apply Changes**: Changes might take a few seconds to apply, or you may need to log out/in
- **Backups**: All configuration changes are backed up in `~/bin/monitors/configs/`
- **Safety**: You can always restore the previous configuration with `mreset`

## Monitor Information

Your setup:
- **DP-2**: ASUSTek 34" monitor (3440x1440)
- **DP-3**: LG UltraWide 29" monitor (2560x1080)
- **DP-4**: Iiyama 34" monitor (3440x1440) - Primary
- **eDP-1**: Built-in laptop display (2880x1920)

## Troubleshooting

If changes don't apply:
1. Try logging out and back in
2. Use `mreset` to restore previous configuration
3. Check the backup files in `~/bin/monitors/configs/`

## Future Improvements

- Add custom positioning for multi-monitor setups
- Support for portrait/landscape orientation switching
- More robust configuration parsing
- GUI interface option