# YADM Templates Documentation

## Overview

This repository uses YADM templates to handle platform-specific configurations between Linux and macOS systems. Templates allow maintaining a single dotfiles repository while automatically generating the correct configuration files based on the operating system.

## How YADM Templates Work

YADM templates are special files that end with `##template` suffix. When you run `yadm alt`, these templates are processed and generate the actual configuration files by evaluating conditional logic based on system variables.

### Template Variables

YADM provides several variables for use in templates:

- `yadm.os` - Operating system (e.g., "Linux", "Darwin" for macOS)
- `yadm.hostname` - System hostname
- `yadm.user` - Current username
- `yadm.distro` - Linux distribution name
- `yadm.arch` - System architecture

### Template Syntax

Templates use Jinja2-like syntax for conditionals:

```jinja
{% if yadm.os == "Linux" %}
  # Linux-specific configuration
{% else %}
  # macOS-specific configuration
{% endif %}
```

## Current Templates

### 1. `.zshrc##template`

Handles major platform differences in the Zsh configuration:

#### Theme Selection
- **Linux**: Uses Powerlevel10k theme with instant prompt
- **macOS**: Uses simpler agnoster theme

#### Plugin Differences
- **Linux plugins**: git, docker, node, dnf, bun, systemd, colored-man-pages, zsh-syntax-highlighting, zsh-autosuggestions, z, uv, pre-commit
- **macOS plugins**: git, docker, node, npm, brew, macos, colored-man-pages, zsh-syntax-highlighting, zsh-autosuggestions

#### Path Configuration
- **Linux**: Uses `/home/kicky` paths
- **macOS**: Uses `/Users/kicky` paths

#### Platform-Specific Tools
- **Linux**: 
  - UV package manager configuration
  - DNF package manager aliases
  - Monitor switching aliases (gdctl-instant.py)
  - Extensive project directory aliases
- **macOS**: 
  - Homebrew configuration
  - Docker Desktop completions
  - LM Studio CLI path
  - Zed editor path

#### Version Display Functions
- Adapted to show platform-specific tools (DNF vs Homebrew)
- Different implementations of the `v()` function

### 2. `.zshrc.pre-oh-my-zsh##template`

Handles pre-Oh My Zsh initialization:

- **Linux**: Minimal setup (just a comment)
- **macOS**: Includes Bun, Docker, NVM configurations and Claude alias

## Testing Templates

After making changes to templates, process them with:

```bash
yadm alt
```

This command regenerates the actual configuration files from the templates.

## Adding New Platform-Specific Configurations

1. Create a new template file with `##template` suffix
2. Use conditional blocks for platform-specific content:
   ```jinja
   {% if yadm.os == "Darwin" %}
     # macOS specific config
   {% elif yadm.os == "Linux" %}
     # Linux specific config
   {% endif %}
   ```
3. Run `yadm alt` to test the template
4. Commit both the template and any documentation updates

## Benefits

1. **Single Source of Truth**: One template file instead of multiple platform-specific versions
2. **Automatic Detection**: YADM automatically uses the correct configuration based on the OS
3. **No Manual Stashing**: Eliminates the need to stash platform-specific changes
4. **Easy Maintenance**: Changes only need to be made in one place
5. **Version Control Friendly**: Templates are text files that diff nicely

## Common Issues and Solutions

### Templates Not Processing
- Ensure file has `##template` suffix
- Run `yadm alt` to process templates
- Check that YADM is properly installed

### Syntax Errors
- Verify all `{% if %}` blocks have matching `{% endif %}`
- Check for proper quoting in conditional expressions
- Use `yadm.os == "Darwin"` for macOS, not "macOS"

### Generated Files Being Overwritten
- YADM regenerates files from templates when `yadm alt` is run
- Make changes to the template file, not the generated file
- Generated files should not be manually edited

## Examples

### Adding a New Tool Only on Linux

```jinja
{% if yadm.os == "Linux" %}
export PATH="$PATH:/opt/linux-tool/bin"
alias lt='linux-tool'
{% endif %}
```

### Platform-Specific Aliases

```jinja
# Git aliases
alias gs='git status'
{% if yadm.os == "Darwin" %}
alias updatedb='sudo /usr/libexec/locate.updatedb'
{% else %}
alias updatedb='sudo updatedb'
{% endif %}
```

### Conditional PATH Additions

```jinja
{% if yadm.os == "Darwin" %}
export PATH="/opt/homebrew/bin:$PATH"
{% elif yadm.os == "Linux" %}
export PATH="/usr/local/bin:$PATH"
{% endif %}
```

## Maintenance Notes

- Always test templates on both platforms after significant changes
- Document any new platform-specific features in this file
- Keep template logic simple and readable
- Consider using includes for very large platform-specific sections