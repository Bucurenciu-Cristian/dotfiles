# 🚀 Dotfiles Onboarding Guide

**Complete setup guide for a professional development environment using yadm, Zsh, GNOME extensions, and comprehensive development tools.**

---

## 📋 Table of Contents

- [Quick Start](#-quick-start-10-minutes)
- [Complete Setup Guide](#-complete-setup-guide-30-45-minutes)
- [Troubleshooting](#-troubleshooting)
- [Maintenance](#-maintenance)
- [Advanced Configuration](#-advanced-configuration)

---

## ⚡ Quick Start (10 minutes)

**For experienced users who just need the commands:**

```bash
# 1. Install yadm
sudo dnf install yadm

# 2. Clone dotfiles
yadm clone https://github.com/Bucurenciu-Cristian/dotfiles

# 3. Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# 4. Install Powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# 5. Install Zsh plugins
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# 6. Set Zsh as default shell
chsh -s $(which zsh)

# 7. Install development tools
curl -fsSL https://bun.sh/install | bash
curl -LsSf https://astral.sh/uv/install.sh | sh

# 8. Restore GNOME settings
dconf load /org/gnome/shell/extensions/ < ~/.config/gnome-extensions.dconf
dconf load /org/gnome/shell/ < ~/.config/gnome-shell.dconf
dconf load /org/gnome/desktop/ < ~/.config/gnome-desktop.dconf

# 9. Restart shell
exec zsh
```

---

## 📖 Complete Setup Guide (30-45 minutes)

### Phase 1: Prerequisites & Base Setup (5 minutes)

#### **System Requirements:**
- **OS**: Fedora Linux (primary) or compatible Linux distribution
- **Desktop**: GNOME Shell
- **Internet**: Stable connection for downloading packages and themes

#### **Install Base Packages:**
```bash
# Update system
sudo dnf update -y

# Install essential packages
sudo dnf install -y git curl zsh util-linux-user gnome-shell-extensions gnome-tweaks

# Verify installations
git --version
zsh --version
gnome-shell --version
```

**Expected Output:**
```
git version 2.49.0
zsh 5.9
GNOME Shell 47.0
```

---

### Phase 2: yadm & Dotfiles Setup (5 minutes)

#### **Install yadm:**
```bash
# Install yadm
sudo dnf install yadm

# Verify installation
yadm --version
```

#### **Clone Dotfiles Repository:**
```bash
# Clone your dotfiles repository
yadm clone https://github.com/Bucurenciu-Cristian/dotfiles

# Check yadm status
yadm status
```

**Expected Output:**
```
On branch master
Your branch is up to date with 'origin/master'.
nothing to commit, working tree clean
```

#### **Verify Files Were Restored:**
```bash
# Check key files are in place
ls -la ~/.zshrc ~/.p10k.zsh ~/.gitconfig ~/.claude/
```

---

### Phase 3: Shell Environment Setup (10 minutes)

#### **Install Oh My Zsh Framework:**
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# When prompted, choose NOT to change shell yet (we'll do it manually)
```

#### **Install Powerlevel10k Theme:**
```bash
# Clone Powerlevel10k theme
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Verify installation
ls -la ~/.oh-my-zsh/custom/themes/powerlevel10k/
```

#### **Install Essential Zsh Plugins:**
```bash
# Install zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Install zsh-autosuggestions  
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Verify plugin installations
ls -la ~/.oh-my-zsh/custom/plugins/
```

#### **Set Zsh as Default Shell:**
```bash
# Change default shell to zsh
chsh -s $(which zsh)

# Verify shell change
grep $USER /etc/passwd | grep zsh
```

#### **Restart Shell Environment:**
```bash
# Start new zsh session
exec zsh

# If Powerlevel10k configuration wizard appears, configure it or skip
# The dotfiles already contain a pre-configured .p10k.zsh
```

---

### Phase 4: Development Tools Setup (10 minutes)

#### **Install Bun (JavaScript/TypeScript Package Manager):**
```bash
# Install Bun
curl -fsSL https://bun.sh/install | bash

# Source shell to update PATH
exec zsh

# Verify Bun installation
bun --version
```

#### **Install UV (Python Package Manager):**
```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Source shell to update PATH
exec zsh

# Verify UV installation
uv --version
```

#### **Verify Git Configuration:**
```bash
# Check Git user configuration
git config --global user.name
git config --global user.email

# Test Git signing (if configured)
git config --global commit.gpgsign
```

#### **Test Version Display Functions:**
```bash
# Test custom version function
versions

# Test quick version function
v
```

**Expected Output Example:**
```
🔧 Development Environment Versions:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Node.js:    v20.x.x
🥯 Bun:        1.x.x
🐍 Python:     3.11.x
🏃 UV:         0.x.x
📝 Git:        2.49.0
🐚 Zsh:        5.9
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Phase 5: GNOME Desktop Environment (10 minutes)

#### **Required Extensions List:**
Your dotfiles include configuration for these 16 extensions:

**🪟 Window Management:**
- `forge@jmmaranan.com` - Tiling window manager
- `advanced-alt-tab@G-dH.github.com` - Enhanced Alt-Tab
- `smart-auto-move@khimaros.com` - Auto-move windows to workspaces

**🖥️ System & Productivity:**
- `Vitals@CoreCoding.com` - System monitoring (CPU, RAM, network)
- `clipboard-indicator@tudmotu.com` - Clipboard history
- `extension-list@tu.berry` - Extension management
- `just-perfection-desktop@just-perfection` - Desktop customization

**🎨 Visual & UI:**
- `blur-my-shell@aunetx` - Blur effects
- `space-bar@luchrioh` - Workspace indicator
- `BingWallpaper@ineffable-gmail.com` - Daily wallpapers
- `weatherornot@somepaulo.github.io` - Weather widget
- `impatience@gfxmonk.net` - Faster animations

**📱 Built-in & System:**
- `apps-menu@gnome-shell-extensions.gcampax.github.com` - Apps menu
- `places-menu@gnome-shell-extensions.gcampax.github.com` - Places menu  
- `window-list@gnome-shell-extensions.gcampax.github.com` - Window list
- `appindicatorsupport@rgcjonas.gmail.com` - System tray support

#### **Install Extensions:**

**Option A: Manual Installation (Recommended)**
1. Visit [GNOME Extensions website](https://extensions.gnome.org/)
2. Install the browser extension when prompted
3. Search for and install each extension from the list above
4. Use the reference file: `~/gnome-extensions-list.txt`

**Option B: Package Manager (where available)**
```bash
# Some extensions may be available via dnf
sudo dnf search gnome-shell-extension
```

#### **Restore GNOME Settings:**
```bash
# Restore extension settings
dconf load /org/gnome/shell/extensions/ < ~/.config/gnome-extensions.dconf

# Restore shell configuration
dconf load /org/gnome/shell/ < ~/.config/gnome-shell.dconf

# Restore desktop settings
dconf load /org/gnome/desktop/ < ~/.config/gnome-desktop.dconf

# Restart GNOME Shell to apply changes
# Press Alt+F2, type 'r', press Enter
# Or logout and login again
```

#### **Verify Extensions:**
```bash
# List enabled extensions
gnome-extensions list --enabled

# Check if all 16 extensions are enabled
gnome-extensions list --enabled | wc -l
```

---

### Phase 6: Verification & Testing (5 minutes)

#### **Complete Environment Test:**
```bash
# 1. Test shell and theme
echo $SHELL
echo $ZSH_THEME

# 2. Test development tools
versions

# 3. Test Git configuration
git config --list | grep user

# 4. Test Claude Code integration (if applicable)
ls -la ~/.claude/

# 5. Test custom aliases
alias | grep claude

# 6. Test GNOME configuration
gnome-extensions list --enabled
dconf read /org/gnome/shell/favorite-apps
```

#### **Performance Verification:**
```bash
# Test shell startup time
time zsh -i -c exit

# Test command completion
# Type: git che<TAB> (should complete to checkout)
# Type: npm i<TAB> (should show npm install suggestions)
```

#### **Visual Verification Checklist:**
- [ ] Terminal shows Powerlevel10k prompt with git status
- [ ] Syntax highlighting works (type invalid command - should be red)
- [ ] Auto-suggestions appear (type part of previous command)
- [ ] GNOME extensions are visible in top bar
- [ ] Desktop blur effects are active (if using blur-my-shell)
- [ ] Workspace indicator shows current workspace

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### **Zsh Issues:**
```bash
# Problem: Zsh not loading properly
# Solution: Reset and restart
rm ~/.zshrc
yadm checkout ~/.zshrc
exec zsh

# Problem: Powerlevel10k not loading
# Solution: Reinstall theme
rm -rf ~/.oh-my-zsh/custom/themes/powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

#### **GNOME Extensions Issues:**
```bash
# Problem: Extensions not loading
# Solution: Check GNOME Shell version compatibility
gnome-shell --version

# Restart GNOME Shell
Alt+F2 → r → Enter

# Problem: Settings not restored
# Solution: Re-apply dconf settings
dconf reset -f /org/gnome/shell/extensions/
dconf load /org/gnome/shell/extensions/ < ~/.config/gnome-extensions.dconf
```

#### **Development Tools Issues:**
```bash
# Problem: Bun not found
# Solution: Add to PATH manually
echo 'export PATH="$HOME/.bun/bin:$PATH"' >> ~/.zshrc
exec zsh

# Problem: UV not found  
# Solution: Reinstall UV
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### **Git Issues:**
```bash
# Problem: Git signing errors
# Solution: Check GPG configuration
git config --global gpg.format
git config --global gpg.ssh.program

# Disable signing temporarily if needed
git config --global commit.gpgsign false
```

---

## 🔄 Maintenance

### Keeping Your Dotfiles Updated

#### **Update Local Configuration:**
```bash
# Pull latest changes
yadm pull

# If you make local changes, add and commit them
yadm add ~/.zshrc  # or any modified file
yadm commit -m "Update local configuration"
yadm push
```

#### **Update Dependencies:**
```bash
# Update Oh My Zsh
omz update

# Update Powerlevel10k
git -C ~/.oh-my-zsh/custom/themes/powerlevel10k pull

# Update plugins
git -C ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting pull
git -C ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions pull

# Update system packages
sudo dnf update
```

#### **Backup Current Settings:**
```bash
# Export current GNOME settings
dconf dump /org/gnome/shell/extensions/ > ~/.config/gnome-extensions.dconf
dconf dump /org/gnome/shell/ > ~/.config/gnome-shell.dconf
dconf dump /org/gnome/desktop/ > ~/.config/gnome-desktop.dconf

# Add to yadm if changed
yadm add ~/.config/gnome-*.dconf
yadm commit -m "Update GNOME configuration"
yadm push
```

---

## ⚙️ Advanced Configuration

### Optional Enhancements

#### **Install Additional Development Tools:**
```bash
# Install Node.js via NVM (if needed alongside Bun)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
exec zsh
nvm install --lts

# Install Docker
sudo dnf install docker docker-compose
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

# Install JetBrains Toolbox
# Download from: https://www.jetbrains.com/toolbox-app/
```

#### **Customize Powerlevel10k:**
```bash
# Reconfigure Powerlevel10k prompt
p10k configure

# Edit configuration directly
vim ~/.p10k.zsh
```

#### **Add More GNOME Extensions:**
```bash
# Add new extension to list
echo "new-extension@example.com" >> ~/gnome-extensions-list.txt

# Update yadm after configuration
yadm add ~/gnome-extensions-list.txt
yadm commit -m "Add new extension"
```

### Performance Optimizations

#### **Zsh Performance:**
```bash
# Profile zsh startup time
for i in $(seq 1 10); do /usr/bin/time zsh -i -c exit; done

# Optimize plugins (remove unused ones from ~/.zshrc)
vim ~/.zshrc
```

#### **GNOME Performance:**
```bash
# Disable animations for better performance
gsettings set org.gnome.desktop.interface enable-animations false

# Or use Just Perfection extension for fine-tuned control
```

---

## 📞 Support & Resources

### Getting Help

- **Repository Issues**: [GitHub Issues](https://github.com/Bucurenciu-Cristian/dotfiles/issues)
- **yadm Documentation**: [yadm.io](https://yadm.io/)
- **Oh My Zsh**: [ohmyz.sh](https://ohmyz.sh/)
- **Powerlevel10k**: [GitHub](https://github.com/romkatv/powerlevel10k)
- **GNOME Extensions**: [extensions.gnome.org](https://extensions.gnome.org/)

### Useful Commands Reference

```bash
# yadm commands
yadm status                    # Check repository status
yadm add <file>               # Add file to repository
yadm commit -m "message"      # Commit changes
yadm push/pull                # Sync with remote

# Zsh commands  
omz update                    # Update Oh My Zsh
exec zsh                      # Restart shell
which zsh                     # Check zsh location

# GNOME commands
gnome-extensions list         # List all extensions
gnome-shell --version        # Check GNOME version
dconf dump /path/             # Export settings
dconf load /path/ < file      # Import settings

# Development tools
versions                      # Show all tool versions
v                            # Quick version display
bun --version                # Check Bun version
uv --version                 # Check UV version
```

---

## ✅ Setup Complete!

Congratulations! You now have a complete, professional development environment set up with:

- **🐚 Modern Shell**: Zsh with Oh My Zsh and Powerlevel10k
- **⚙️ Development Tools**: Bun, UV, Git with GPG signing
- **🖥️ Desktop Environment**: 16 GNOME extensions for productivity
- **🎨 Visual Enhancement**: Beautiful terminal and desktop
- **🔧 Productivity Features**: Advanced window management, system monitoring
- **📋 Workflow Integration**: Claude Code integration with custom commands

Your development environment is now consistent, portable, and fully configured across any machine you use!

---

*This guide was automatically generated as part of the dotfiles repository. Last updated: June 27, 2025*