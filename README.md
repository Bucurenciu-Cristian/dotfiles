# 🏠 Personal Dotfiles Repository

**Professional development environment configuration managed with yadm for Fedora + GNOME**

---

## 🎯 What This Repository Contains

This is my comprehensive dotfiles setup that provides a complete, professional development environment across any machine. Built through systematic analysis of real-world usage patterns and optimized for productivity.

### **Core Components**
- **🐚 Modern Shell**: Zsh + Oh-My-Zsh + Powerlevel10k with 13 productivity plugins
- **⚙️ Development Tools**: Bun (JS), UV (Python), Git with 1Password GPG signing
- **🖥️ Desktop Environment**: 16 carefully curated GNOME extensions
- **🤖 Claude Code Integration**: Custom commands and global configuration
- **📋 Complete Documentation**: Detailed setup and troubleshooting guides

---

## 🚀 Quick Start (New Machine Setup)

**Prerequisites**: Fresh Fedora installation with GNOME desktop

### **1. Install Base Dependencies**
```bash
sudo dnf update -y
sudo dnf install -y yadm git curl zsh
```

### **2. Install 1Password & Configure SSH**
```bash
# Download 1Password from: https://1password.com/downloads/linux/
# Enable SSH agent in 1Password settings
```

### **3. Clone Dotfiles**
```bash
yadm clone https://github.com/Bucurenciu-Cristian/dotfiles
```

### **4. Follow Complete Setup**
```bash
# Read the comprehensive setup guide
cat ~/ONBOARDING.md
```

**⏱️ Total Setup Time**: 30-45 minutes for complete environment

---

## 📚 Documentation Guide

This repository contains multiple documentation files for different purposes:

### **🎯 For New Machine Setup**
- **`ONBOARDING.md`** - Complete step-by-step setup guide (30-45 min)
- **`spec.md`** - Comprehensive specification with blindspot analysis

### **🔧 For Daily Usage**
- **`CLAUDE.md`** - Project-specific Claude Code configuration
- **`gnome-extensions-list.txt`** - Reference list of all extensions

---

## 🏗️ Repository Structure

```
~/
├── README.md                    # This file - project overview
├── ONBOARDING.md               # Complete setup guide
├── spec.md                     # Detailed specification & analysis
├── CLAUDE.md                   # Project Claude Code config
├── .gitconfig                  # Git configuration with 1Password signing
├── .zshrc                      # Zsh configuration with Oh-My-Zsh
├── .p10k.zsh                   # Powerlevel10k theme configuration
├── .claude/
│   ├── CLAUDE.md              # Global Claude Code configuration
│   └── commands/              # Custom Claude Code slash commands (15 files)
├── .config/
│   ├── gnome-extensions.dconf # GNOME extensions settings
│   ├── gnome-shell.dconf      # GNOME shell configuration  
│   └── gnome-desktop.dconf    # GNOME desktop settings
└── gnome-extensions-list.txt  # Extension reference list
```

---

## 🛠️ Key Technologies & Tools

### **Shell Environment**
- **Zsh** with Oh-My-Zsh framework
- **Powerlevel10k** theme with classic powerline style
- **13 Plugins**: git, docker, node, dnf, bun, systemd, colored-man-pages, zsh-syntax-highlighting, zsh-autosuggestions, z, dotenv, uv, pre-commit

### **Development Stack**
- **Package Managers**: Bun (JavaScript), UV (Python)
- **Version Control**: Git with GPG signing via 1Password SSH agent
- **Authentication**: SSH keys managed through 1Password

### **GNOME Extensions (16 Total)**
**🪟 Window Management**:
- Forge (tiling), Advanced Alt-Tab, Smart Auto-Move

**🖥️ Productivity**:
- Vitals (system monitoring), Clipboard Indicator, Extension List

**🎨 Visual Enhancement**:
- Blur my Shell, Space Bar, Bing Wallpaper, Weather or Not

### **Claude Code Integration**
- **Global Configuration**: Package manager preferences, tool usage patterns
- **15 Custom Commands**: brainstorm, plan, setup, security-review, find-missing-tests, and more
- **Workflow Automation**: GitHub integration, task management, development workflows

---

## 🎯 Design Philosophy

### **Critical vs. Nice-to-Have**
Based on real usage analysis:
- **Must Work Day 1**: Git SSH, development tools, GNOME extensions
- **Productivity Focused**: All 16 extensions contribute to daily workflow
- **Aesthetic Secondary**: Shell beautification is nice but not critical

### **Optimization Priorities**
1. **Git SSH Setup** - Biggest pain point, highest priority
2. **GNOME Extensions** - Daily usage, productivity multiplier  
3. **Development Tools** - Bun, UV critical for projects
4. **Shell Environment** - Workflow enhancement, moderate priority

---

## 🔄 Maintenance Commands

### **Update Dotfiles**
```bash
yadm pull                        # Get latest changes
yadm add <modified-file>         # Stage local changes
yadm commit -m "Update config"   # Commit changes
yadm push                        # Push to repository
```

### **Update Dependencies**
```bash
omz update                       # Update Oh-My-Zsh
git -C ~/.oh-my-zsh/custom/themes/powerlevel10k pull  # Update theme
sudo dnf update                  # Update system packages
```

### **Backup Current Settings**
```bash
# Export GNOME settings
dconf dump /org/gnome/shell/extensions/ > ~/.config/gnome-extensions.dconf
dconf dump /org/gnome/shell/ > ~/.config/gnome-shell.dconf

# Add to yadm if changed
yadm add ~/.config/gnome-*.dconf
yadm commit -m "Update GNOME configuration"
```

---

## 🆘 Troubleshooting

### **Common Issues**
- **Git SSH Problems**: Check 1Password SSH agent configuration
- **Extensions Not Loading**: Verify GNOME Shell version compatibility
- **Shell Issues**: Reset with `exec zsh` or reinstall Oh-My-Zsh

### **Getting Help**
- **Detailed Troubleshooting**: See `ONBOARDING.md` troubleshooting section
- **Complete Analysis**: See `spec.md` for blindspot identification
- **Repository Issues**: [GitHub Issues](https://github.com/Bucurenciu-Cristian/dotfiles/issues)

---

## 📊 Setup Statistics

- **⏱️ Quick Setup**: 10 minutes (experienced users)
- **📖 Complete Setup**: 30-45 minutes (with all extensions)
- **🔧 Core Tools**: 5 essential development tools
- **🖥️ Extensions**: 16 GNOME extensions for productivity
- **📝 Documentation**: 1000+ lines of setup documentation
- **🎯 Success Rate**: Designed for zero-failure setup on Fedora + GNOME

---

## 🌟 What Makes This Setup Special

1. **🔍 Blindspot Analysis**: Identified and addressed common setup failures
2. **📊 Usage-Based Optimization**: Prioritized based on real daily workflows  
3. **🧪 Systematic Testing**: Comprehensive validation protocols
4. **📚 Complete Documentation**: From quick start to advanced troubleshooting
5. **🔄 Maintenance Ready**: Built for long-term sustainability

---

## 🏁 Next Steps

1. **New Machine Setup**: Start with `ONBOARDING.md`
2. **Detailed Analysis**: Read `spec.md` for complete understanding
3. **Daily Usage**: Enjoy your optimized development environment!

---

*This dotfiles repository represents a carefully curated, battle-tested development environment optimized for productivity on Fedora + GNOME. Last updated: June 2025*