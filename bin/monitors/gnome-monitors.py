#!/usr/bin/env python3
"""
GNOME Monitor Configuration Tool for Wayland
Switches between different monitor configurations
"""

import subprocess
import sys
import os
import time
from pathlib import Path

# Configuration profiles
PROFILES = {
    "single": {
        "name": "Single Monitor (Iiyama 34\")",
        "monitors": ["DP-4"],  # Only Iiyama monitor active
        "primary": "DP-4"
    },
    "dual": {
        "name": "Dual Monitors (Both 34\")",
        "monitors": ["DP-2", "DP-4"],  # ASUS and Iiyama
        "primary": "DP-4"
    },
    "triple": {
        "name": "Triple Monitors (All External)",
        "monitors": ["DP-2", "DP-3", "DP-4"],
        "primary": "DP-4"
    },
    "all": {
        "name": "All Monitors (Including Laptop)",
        "monitors": ["DP-2", "DP-3", "DP-4", "eDP-1"],
        "primary": "DP-4"
    }
}

def run_command(cmd):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running command: {e}")
        return None

def get_monitor_info():
    """Get current monitor information from GNOME"""
    cmd = "gdbus call --session --dest org.gnome.Mutter.DisplayConfig --object-path /org/gnome/Mutter/DisplayConfig --method org.gnome.Mutter.DisplayConfig.GetCurrentState"
    output = run_command(cmd)
    
    if not output:
        return None
    
    # Parse monitor information (simplified)
    monitors = {}
    lines = output.split('\n')
    
    current_monitor = None
    for line in lines:
        if "'DP-" in line or "'eDP-" in line:
            # Extract monitor connector
            parts = line.split("'")
            if len(parts) >= 2:
                connector = parts[1]
                monitors[connector] = {
                    'connector': connector,
                    'connected': True
                }
                current_monitor = connector
        elif current_monitor and "is-current" in line and "true" in line:
            monitors[current_monitor]['active'] = True
    
    return monitors

def apply_monitor_config(profile_name):
    """Apply a monitor configuration profile"""
    if profile_name not in PROFILES:
        print(f"Error: Unknown profile '{profile_name}'")
        print(f"Available profiles: {', '.join(PROFILES.keys())}")
        return False
    
    profile = PROFILES[profile_name]
    print(f"Applying profile: {profile['name']}")
    
    # For GNOME on Wayland, we need to modify the monitors.xml file
    # and trigger a reload
    monitors_xml = Path.home() / ".config" / "monitors.xml"
    
    # Backup current configuration
    backup_dir = Path.home() / "bin" / "monitors" / "configs"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    if monitors_xml.exists():
        backup_file = backup_dir / f"monitors-backup-{int(time.time())}.xml"
        subprocess.run(f"cp '{monitors_xml}' '{backup_file}'", shell=True)
        print(f"Backed up current config to: {backup_file}")
    
    # Create configuration based on profile
    if profile_name == "single":
        # Single monitor configuration
        config_xml = '''<monitors version="2">
  <configuration>
    <logicalmonitor>
      <x>0</x>
      <y>0</y>
      <scale>1</scale>
      <primary>yes</primary>
      <monitor>
        <monitorspec>
          <connector>DP-4</connector>
          <vendor>IVM</vendor>
          <product>PL3481WQ</product>
        </monitorspec>
        <mode>
          <width>3440</width>
          <height>1440</height>
          <rate>99.982</rate>
        </mode>
      </monitor>
    </logicalmonitor>
    <disabled>
      <monitorspec>
        <connector>DP-2</connector>
        <vendor>AUS</vendor>
        <product>VG34VQEL1A</product>
      </monitorspec>
    </disabled>
    <disabled>
      <monitorspec>
        <connector>DP-3</connector>
        <vendor>GSM</vendor>
        <product>LG ULTRAWIDE</product>
      </monitorspec>
    </disabled>
    <disabled>
      <monitorspec>
        <connector>eDP-1</connector>
        <vendor>CSO</vendor>
        <product>0x1319</product>
      </monitorspec>
    </disabled>
  </configuration>
</monitors>'''
    else:
        # For other profiles, we'll need more complex XML generation
        print(f"Profile '{profile_name}' configuration is being developed...")
        return False
    
    # Write the new configuration
    with open(monitors_xml, 'w') as f:
        f.write(config_xml)
    
    print("Configuration written. Applying changes...")
    
    # Try to trigger a reload
    # Toggle an unrelated setting to force GNOME to reload display config
    run_command("gsettings set org.gnome.desktop.interface enable-animations false")
    time.sleep(0.1)
    run_command("gsettings set org.gnome.desktop.interface enable-animations true")
    
    print("Monitor configuration applied!")
    print("\nNote: If changes don't apply immediately, you may need to:")
    print("- Log out and log back in")
    print("- Or wait a few seconds for GNOME to detect the change")
    
    return True

def list_monitors():
    """List all connected monitors"""
    monitors = get_monitor_info()
    
    if not monitors:
        print("Error: Could not get monitor information")
        return
    
    print("Connected monitors:")
    for connector, info in monitors.items():
        status = "Active" if info.get('active', False) else "Inactive"
        print(f"  {connector}: {status}")
    
    print("\nAvailable profiles:")
    for key, profile in PROFILES.items():
        print(f"  {key}: {profile['name']}")

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: gnome-monitors.py <command>")
        print("Commands:")
        print("  list    - List all monitors and profiles")
        print("  single  - Switch to single monitor")
        print("  dual    - Switch to dual monitors")
        print("  triple  - Switch to triple monitors")
        print("  all     - Enable all monitors")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        list_monitors()
    elif command in PROFILES:
        apply_monitor_config(command)
    else:
        print(f"Unknown command: {command}")
        print("Run without arguments to see usage")
        sys.exit(1)

if __name__ == "__main__":
    main()