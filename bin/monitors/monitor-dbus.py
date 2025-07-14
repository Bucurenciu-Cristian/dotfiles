#!/usr/bin/env python3
"""
Direct D-Bus Monitor Control for GNOME/Wayland
Working monitor switching with immediate feedback
"""

import subprocess
import sys
import json
import time
from pathlib import Path

# Known monitor configurations from your system
MONITORS = {
    'DP-2': {
        'vendor': 'AUS',
        'product': 'VG34VQEL1A',
        'serial': 'NBLMDW006540',
        'name': 'ASUS 34" UltraWide',
        'preferred_mode': ('3440x1440@100.006', 3440, 1440, 100.00563049316406, 1.0)
    },
    'DP-3': {
        'vendor': 'GSM',
        'product': 'LG ULTRAWIDE',
        'serial': '0x00080df4',
        'name': 'LG 29" UltraWide',
        'preferred_mode': ('2560x1080@60.000', 2560, 1080, 59.999534606933594, 1.0)
    },
    'DP-4': {
        'vendor': 'IVM',
        'product': 'PL3481WQ',
        'serial': '1242542701807',
        'name': 'Iiyama 34" UltraWide',
        'preferred_mode': ('3440x1440@99.982', 3440, 1440, 99.981605529785156, 1.0)
    },
    'eDP-1': {
        'vendor': 'CSO',
        'product': '0x1319',
        'serial': '0x00000000',
        'name': 'Built-in Laptop Display',
        'preferred_mode': ('2880x1920@60.000', 2880, 1920, 60.000129699707031, 2.0)
    }
}

def run_command(cmd, show_output=False):
    """Run a command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if show_output:
            print(f"Command: {cmd}")
            print(f"Return code: {result.returncode}")
            if result.stdout:
                print(f"Output: {result.stdout}")
            if result.stderr:
                print(f"Error: {result.stderr}")
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        print(f"Error running command: {e}")
        return False, "", str(e)

def get_current_state():
    """Get current monitor state from GNOME"""
    cmd = 'gdbus call --session --dest org.gnome.Mutter.DisplayConfig --object-path /org/gnome/Mutter/DisplayConfig --method org.gnome.Mutter.DisplayConfig.GetCurrentState'
    success, output, error = run_command(cmd)
    if not success:
        print(f"Failed to get monitor state: {error}")
        return None
    return output

def backup_config():
    """Backup current monitor configuration"""
    backup_dir = Path.home() / "bin" / "monitors" / "configs"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # Backup monitors.xml if it exists
    monitors_xml = Path.home() / ".config" / "monitors.xml"
    if monitors_xml.exists():
        backup_file = backup_dir / f"monitors-backup-{int(time.time())}.xml"
        success, _, _ = run_command(f'cp "{monitors_xml}" "{backup_file}"')
        if success:
            print(f"✓ Configuration backed up to: {backup_file}")
        else:
            print("⚠ Warning: Could not backup configuration")

def create_single_monitor_xml(monitor_id):
    """Create XML configuration for single monitor"""
    if monitor_id not in MONITORS:
        print(f"❌ Unknown monitor: {monitor_id}")
        return None
    
    monitor = MONITORS[monitor_id]
    mode_name, width, height, refresh_rate, scale = monitor['preferred_mode']
    
    # Create XML for single monitor setup
    xml_content = f'''<monitors version="2">
  <configuration>
    <logicalmonitor>
      <x>0</x>
      <y>0</y>
      <scale>{scale}</scale>
      <primary>yes</primary>
      <monitor>
        <monitorspec>
          <connector>{monitor_id}</connector>
          <vendor>{monitor['vendor']}</vendor>
          <product>{monitor['product']}</product>
          <serial>{monitor['serial']}</serial>
        </monitorspec>
        <mode>
          <width>{width}</width>
          <height>{height}</height>
          <rate>{refresh_rate}</rate>
        </mode>
      </monitor>
    </logicalmonitor>'''
    
    # Disable all other monitors
    for other_id, other_monitor in MONITORS.items():
        if other_id != monitor_id:
            xml_content += f'''
    <disabled>
      <monitorspec>
        <connector>{other_id}</connector>
        <vendor>{other_monitor['vendor']}</vendor>
        <product>{other_monitor['product']}</product>
        <serial>{other_monitor['serial']}</serial>
      </monitorspec>
    </disabled>'''
    
    xml_content += '''
  </configuration>
</monitors>'''
    
    return xml_content

def apply_monitor_config(monitor_id, verbose=True):
    """Apply single monitor configuration"""
    if monitor_id not in MONITORS:
        print(f"❌ Unknown monitor: {monitor_id}")
        return False
    
    monitor = MONITORS[monitor_id]
    
    if verbose:
        print(f"🔄 Switching to: {monitor['name']} ({monitor_id})")
        print(f"   Resolution: {monitor['preferred_mode'][1]}x{monitor['preferred_mode'][2]}")
        print(f"   Refresh Rate: {monitor['preferred_mode'][3]:.1f}Hz")
    
    # Backup current configuration
    backup_config()
    
    # Create new configuration
    xml_content = create_single_monitor_xml(monitor_id)
    if not xml_content:
        return False
    
    # Write configuration
    monitors_xml = Path.home() / ".config" / "monitors.xml"
    try:
        with open(monitors_xml, 'w') as f:
            f.write(xml_content)
        if verbose:
            print("✓ Configuration written")
    except Exception as e:
        print(f"❌ Failed to write configuration: {e}")
        return False
    
    # Try to trigger reload using multiple methods
    if verbose:
        print("🔄 Applying configuration...")
    
    # Method 1: Toggle display settings
    run_command("gsettings set org.gnome.desktop.interface enable-animations false")
    time.sleep(0.1)
    run_command("gsettings set org.gnome.desktop.interface enable-animations true")
    
    # Method 2: Toggle screen lock setting (forces display refresh)
    run_command("gsettings set org.gnome.desktop.screensaver lock-enabled false")
    time.sleep(0.1)
    run_command("gsettings set org.gnome.desktop.screensaver lock-enabled true")
    
    # Method 3: Try to force display reconfiguration
    run_command("busctl --user call org.gnome.Mutter.DisplayConfig /org/gnome/Mutter/DisplayConfig org.gnome.Mutter.DisplayConfig GetCurrentState >/dev/null 2>&1")
    
    if verbose:
        print("✓ Configuration applied!")
        print("\n💡 Note: If the display doesn't change immediately:")
        print("   - Wait 5-10 seconds for GNOME to detect the change")
        print("   - Try moving your mouse or pressing a key")
        print("   - If still not working, try logging out and back in")
    
    return True

def list_monitors():
    """List all available monitors"""
    print("Available monitors:")
    print("=" * 50)
    
    for monitor_id, monitor in MONITORS.items():
        mode_name, width, height, refresh_rate, scale = monitor['preferred_mode']
        print(f"📺 {monitor_id}: {monitor['name']}")
        print(f"   Resolution: {width}x{height} @ {refresh_rate:.1f}Hz")
        print(f"   Scale: {scale}x")
        print(f"   Vendor: {monitor['vendor']}, Product: {monitor['product']}")
        print()

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("GNOME Monitor Switcher - D-Bus Edition")
        print("=" * 40)
        print("Usage: monitor-dbus.py <command>")
        print("\nCommands:")
        print("  list        - List all available monitors")
        print("  DP-2        - Switch to ASUS monitor only")
        print("  DP-3        - Switch to LG monitor only")
        print("  DP-4        - Switch to Iiyama monitor only")
        print("  eDP-1       - Switch to laptop display only")
        print("\nExamples:")
        print("  monitor-dbus.py DP-2    # Switch to ASUS monitor")
        print("  monitor-dbus.py list    # Show all monitors")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        list_monitors()
    elif command in MONITORS:
        success = apply_monitor_config(command)
        if success:
            monitor = MONITORS[command]
            print(f"\n🎉 Successfully switched to {monitor['name']}!")
        else:
            print(f"\n❌ Failed to switch to {command}")
            sys.exit(1)
    else:
        print(f"❌ Unknown command: {command}")
        print("Run without arguments to see available commands")
        sys.exit(1)

if __name__ == "__main__":
    main()