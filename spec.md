# 🚀 New Machine Setup Specification

**Comprehensive guide for setting up a professional development environment on Fedora + GNOME, optimized based on real-world usage patterns and identified blindspots.**

---

## 📋 Executive Summary

This specification addresses the complete setup process for replicating a proven development environment on new machines, with focus on:

- **Critical Day-1 functionality**: Git SSH, essential dev tools, GNOME productivity extensions
- **Identified blindspots**: Bootstrap dependencies, untested flows, missing automations
- **Optimization opportunities**: 1Password SSH workflow, repository management, validation testing

**Target Platform**: Fedora Linux + GNOME Shell (no cross-platform requirements)

---

## 🎯 Critical Components (Must Work Day 1)

### **1. Git SSH Configuration with 1Password**
- **Priority**: HIGHEST - "Biggest pain point" 
- **Current State**: Uses 1Password SSH agent with frequent auth prompts
- **Requirements**:
  - Personal GitHub SSH key via 1Password
  - Work GitHub SSH key via 1Password  
  - GPG signing configuration
  - Seamless authentication flow

### **2. Essential Development Tools**
- **Bun**: JavaScript/TypeScript package manager (critical for projects)
- **UV**: Python package manager (critical for Python development)
- **Git**: With proper SSH and GPG configuration

### **3. GNOME Extensions (All 16 Required)**
**Daily Usage Extensions** (highest priority):
- `forge@jmmaranan.com` - Tiling window manager
- `advanced-alt-tab@G-dH.github.com` - Enhanced Alt-Tab
- `space-bar@luchrioh` - Workspace indicator  
- `clipboard-indicator@tudmotu.com` - Clipboard history
- `Vitals@CoreCoding.com` - System monitoring

**Complete Extensions List** (all contribute to workflow):
- `extension-list@tu.berry`
- `impatience@gfxmonk.net`
- `just-perfection-desktop@just-perfection`
- `smart-auto-move@khimaros.com`
- `weatherornot@somepaulo.github.io`
- `blur-my-shell@aunetx`
- `BingWallpaper@ineffable-gmail.com`
- `burn-my-windows@schneegans.github.com`
- `apps-menu@gnome-shell-extensions.gcampax.github.com`
- `places-menu@gnome-shell-extensions.gcampax.github.com`
- `window-list@gnome-shell-extensions.gcampax.github.com`
- `appindicatorsupport@rgcjonas.gmail.com`

### **4. Custom System Configuration**
- **Keybinding**: Super+Alt+H to hide windows (not captured in current dotfiles)
- **GNOME settings**: Restored via dconf files
- **Shell environment**: Zsh + Oh-My-Zsh + Powerlevel10k (aesthetic priority)

---

## ⚠️ Identified Blindspots & Solutions

### **1. CRITICAL: Untested Restoration Flow**
- **Problem**: yadm dotfiles setup never tested end-to-end
- **Risk**: Setup may fail when desperately needed
- **Solution**: Create comprehensive testing protocol

### **2. Bootstrap Dependency Chain**
- **Problem**: Chicken-and-egg setup sequence unclear
- **Current Understanding**: 1Password → SSH Keys → yadm clone
- **Solution**: Document exact bootstrap sequence with fallback options

### **3. Missing Repository Automation**
- **Problem**: No automated way to clone essential repos to ~/dev
- **Impact**: Manual setup time and potential forgotten repositories
- **Solution**: Create repository cloning script/checklist

### **4. 1Password SSH Agent Friction**
- **Problem**: "Very annoying when requesting access to pull"
- **Impact**: Workflow interruption and frustration
- **Solution**: Research SSH agent optimization and caching options

### **5. Custom Keybindings Not Captured**
- **Problem**: Super+Alt+H keybinding not in dotfiles
- **Risk**: Lost productivity shortcuts
- **Solution**: Audit and document all custom keybindings

### **6. System Dependency Assumptions**
- **Problem**: ONBOARDING.md assumes packages exist
- **Risk**: Setup failure on fresh systems
- **Solution**: Add pre-flight dependency checks

---

## 🔄 Optimal Bootstrap Sequence

### **Phase 1: System Foundation (5 minutes)**
```bash
# 1. Update system
sudo dnf update -y

# 2. Install core dependencies
sudo dnf install -y git curl zsh util-linux-user gnome-shell-extensions gnome-tweaks yadm

# 3. Verify installations
git --version && zsh --version && yadm --version
```

### **Phase 2: Authentication Setup (10 minutes)**
```bash
# 1. Install 1Password (manual download)
# Download from: https://1password.com/downloads/linux/

# 2. Configure 1Password SSH agent
# Enable SSH agent in 1Password settings

# 3. Test SSH access
ssh -T git@github.com  # Should authenticate via 1Password
```

### **Phase 3: Dotfiles Restoration (5 minutes)**
```bash
# 1. Clone dotfiles repository
yadm clone https://github.com/Bucurenciu-Cristian/dotfiles

# 2. Verify critical files restored
ls -la ~/.zshrc ~/.p10k.zsh ~/.gitconfig ~/.claude/

# 3. Test yadm status
yadm status  # Should show clean working tree
```

### **Phase 4: Shell Environment (10 minutes)**
```bash
# 1. Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# 2. Install Powerlevel10k theme
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# 3. Install essential plugins
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# 4. Set Zsh as default shell
chsh -s $(which zsh)
exec zsh
```

### **Phase 5: Development Tools (10 minutes)**
```bash
# 1. Install Bun
curl -fsSL https://bun.sh/install | bash

# 2. Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Reload shell environment
exec zsh

# 4. Verify installations
bun --version && uv --version
```

### **Phase 6: GNOME Configuration (15 minutes)**
```bash
# 1. Install GNOME extensions (manual via extensions.gnome.org)
# Use reference: ~/gnome-extensions-list.txt

# 2. Restore GNOME settings
dconf load /org/gnome/shell/extensions/ < ~/.config/gnome-extensions.dconf
dconf load /org/gnome/shell/ < ~/.config/gnome-shell.dconf
dconf load /org/gnome/desktop/ < ~/.config/gnome-desktop.dconf

# 3. Configure custom keybindings
# Manual: Settings → Keyboard → Custom Shortcuts
# Add: Super+Alt+H → Hide window command

# 4. Restart GNOME Shell
# Alt+F2 → r → Enter
```

### **Phase 7: Manual Applications (20 minutes)**
```bash
# Install via package manager or download:
# - Firefox (should be pre-installed)
# - Brave Beta: https://brave.com/linux/
# - Docker: sudo dnf install docker docker-compose
# - Solaar: sudo dnf install solaar
```

### **Phase 8: Repository Setup (Optional)**
```bash
# Create development directory structure
mkdir -p ~/dev

# Clone essential repositories (to be defined)
# cd ~/dev && git clone <essential-repo-1>
# cd ~/dev && git clone <essential-repo-2>
```

---

## ✅ Validation Testing Protocol

### **Immediate Verification Checklist**
- [ ] Git SSH authentication works without errors
- [ ] Bun and UV commands execute successfully
- [ ] All 16 GNOME extensions are enabled and functional
- [ ] Custom keybinding (Super+Alt+H) works
- [ ] Terminal shows Powerlevel10k prompt with git status
- [ ] Clipboard indicator appears in top bar
- [ ] Workspace switching works smoothly

### **Workflow Testing**
- [ ] Clone a repository via SSH (should not prompt for password)
- [ ] Create a test commit with GPG signing
- [ ] Use advanced Alt-Tab between applications
- [ ] Test tiling window management with Forge
- [ ] Verify system monitoring displays in Vitals

### **Performance Verification**
- [ ] Shell startup time: `time zsh -i -c exit` (should be < 2 seconds)
- [ ] Extension load time acceptable after login
- [ ] 1Password SSH authentication frequency tolerable

---

## 🛠️ Manual Installation Reference

### **Required Downloads**
| Application | Download URL | Notes |
|-------------|--------------|-------|
| 1Password | https://1password.com/downloads/linux/ | Required for SSH keys |
| Brave Beta | https://brave.com/linux/ | Secondary browser |
| Docker | `sudo dnf install docker docker-compose` | Development tool |
| Solaar | `sudo dnf install solaar` | Logitech device management |

### **Browser Sync Setup**
- **Firefox**: Use built-in Mozilla sync (no backup needed)
- **Brave Beta**: Use Brave sync chain (no backup needed)

---

## 🔧 Optimization Opportunities

### **1. 1Password SSH Agent Improvements**
**Current Pain Point**: Frequent authentication prompts during git operations

**Research Areas**:
- SSH agent caching duration settings
- 1Password CLI integration for automated workflows
- Alternative authentication methods for high-frequency operations

**Potential Solutions**:
- Configure longer agent timeout periods
- Use SSH agent forwarding for development containers
- Implement conditional authentication based on operation type

### **2. Repository Management Automation**
**Current Gap**: Manual cloning of essential repositories

**Proposed Solution**: Create `~/dev/setup-repos.sh`:
```bash
#!/bin/bash
# Auto-clone essential development repositories
cd ~/dev

# Add repository list here
# git clone git@github.com:user/essential-repo-1.git
# git clone git@github.com:user/essential-repo-2.git

echo "Development repositories cloned successfully"
```

### **3. Custom Keybinding Backup**
**Current Gap**: Super+Alt+H not captured in dotfiles

**Solution**: Add to GNOME dconf export:
```bash
# Export custom keybindings
dconf dump /org/gnome/settings-daemon/plugins/media-keys/ > ~/.config/gnome-keybindings.dconf

# Add to yadm tracking
yadm add ~/.config/gnome-keybindings.dconf
```

### **4. Pre-flight Dependency Checking**
**Proposed Addition**: System validation script
```bash
#!/bin/bash
# check-dependencies.sh
echo "Verifying system requirements..."

# Check Fedora version
fedora_version=$(rpm -E %fedora)
echo "Fedora version: $fedora_version"

# Check GNOME version  
gnome_version=$(gnome-shell --version)
echo "GNOME version: $gnome_version"

# Check required packages
required_packages="git curl zsh gnome-shell-extensions yadm"
for package in $required_packages; do
    if rpm -q $package &>/dev/null; then
        echo "✓ $package installed"
    else
        echo "✗ $package missing - install with: sudo dnf install $package"
    fi
done
```

---

## 🎯 Success Criteria

### **Setup Time Targets**
- **Complete setup**: < 60 minutes (including manual downloads)
- **Core functionality**: < 30 minutes (Git + dev tools + basic GNOME)
- **SSH authentication**: < 5 minutes after 1Password installation

### **Reliability Requirements**
- **Zero-failure rate**: Setup should work on any fresh Fedora + GNOME system
- **Reproducible results**: Multiple setups should yield identical environments
- **Recovery capability**: Ability to restore from any point of failure

### **User Experience Goals**
- **Minimal manual intervention**: Automated where possible, clear instructions where not
- **Clear progress indication**: User knows what's happening at each step
- **Graceful failure handling**: Clear error messages and recovery steps

---

## 📝 Next Steps

### **Immediate Actions Required**
1. **Test current yadm restoration flow** on a VM or container
2. **Document exact 1Password SSH setup process** with screenshots
3. **Create repository cloning checklist** for ~/dev folder
4. **Export and backup custom keybindings** to dotfiles

### **Future Improvements**
1. **Research 1Password SSH optimization** options
2. **Create automated dependency checking** script
3. **Develop testing protocol** for validation
4. **Consider containerized testing** environment

### **Documentation Updates**
1. **Update ONBOARDING.md** with bootstrap sequence
2. **Add troubleshooting section** for common failures
3. **Create quick reference** for post-setup validation

---

## 🔍 Risk Assessment

### **High Risk**
- **Untested yadm flow**: Could fail completely when needed
- **1Password dependency**: Single point of failure for SSH access
- **GNOME extension compatibility**: May break with GNOME updates

### **Medium Risk**
- **Custom keybinding loss**: Reduced productivity until reconfigured
- **Repository cloning overhead**: Time-consuming manual process
- **SSH agent configuration**: Workflow friction if not optimized

### **Low Risk**
- **Shell aesthetic features**: Non-critical for core functionality
- **Manual application installation**: Well-documented, predictable process
- **Browser sync**: Handled by third-party services

---

*This specification was developed through iterative analysis of real-world usage patterns and systematic identification of setup blindspots. Last updated: January 2025*