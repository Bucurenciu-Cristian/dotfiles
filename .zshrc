# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="powerlevel10k/powerlevel10k"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  docker
  node
  dnf
  bun
  systemd
  colored-man-pages
  zsh-syntax-highlighting
  zsh-autosuggestions
  z
  uv
  pre-commit
)

source $ZSH/oh-my-zsh.sh

# User configuration

# Path configuration
export PATH="$HOME/.local/bin:$HOME/bin:$PATH"

# Bun configuration
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"

# NVM configuration
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# pnpm configuration
export PNPM_HOME="/home/kicky/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac

# Editor configuration
export EDITOR="cursor"
export VISUAL="cursor"

# Other environment variables
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring

# Project aliases (from bashrc)
alias claude-mcp-settings='zed ~/.claude/settings.local.json'

# Dev folder projects
alias claude-work-sepa='cd /home/kicky/dev/sepa && claude'
alias claude-work-sepa-hausfabrik='cd /home/kicky/dev/sepa/hausfabrik; cursor .; claude'
alias claude-work-sepa-thelia-react='cd /home/kicky/dev/sepa/thelia-react; cursor .; claude'
alias claude-work-sepa-kubernetes-fastapi='cd /home/kicky/dev/sepa/kubernetes-fastapi; cursor .; claude'
alias claude-work-scenextras='cd /home/kicky/dev/sceneXtras; cursor .; claude'
alias claude-work-claude-hooks='cd /home/kicky/dev/claude-hooks; cursor .; claude'

# Work folder projects
alias claude-work-windows-draft='cd /home/kicky/work/01-active/windows-draft; cursor .; claude'
alias claude-work-flo='cd /home/kicky/work/01-active/Flo-manager/flo_lets_fit; cursor .; claude'
alias claude-work-clinic='cd /home/kicky/work/01-active/clinic-scheduler; cursor .; claude'
alias claude-work-devfusion='cd /home/kicky/work/01-active/devfusion-portfolio; cursor .; claude'
alias claude-work-focus='cd /home/kicky/work/01-active/focus; cursor .; claude'
alias claude-work-woodcraft='cd /home/kicky/work/01-active/woodcraft-mob; cursor .; claude'
alias claude-work-template='cd /home/kicky/work/05-templates/client-boilerplate-template; cursor .; claude'

# Gemini aliases - Dev folder projects
alias gemini-work-sepa='cd /home/kicky/dev/sepa && gemini'
alias gemini-work-sepa-hausfabrik='cd /home/kicky/dev/sepa/hausfabrik; cursor .; gemini'
alias gemini-work-sepa-thelia-react='cd /home/kicky/dev/sepa/thelia-react; cursor .; gemini'
alias gemini-work-sepa-kubernetes-fastapi='cd /home/kicky/dev/sepa/kubernetes-fastapi; cursor .; gemini'
alias gemini-work-scenextras='cd /home/kicky/dev/sceneXtras; cursor .; gemini'
alias gemini-work-claude-hooks='cd /home/kicky/dev/claude-hooks; cursor .; gemini'

# Gemini aliases - Work folder projects
alias gemini-work-windows-draft='cd /home/kicky/work/01-active/windows-draft; cursor .; gemini'
alias gemini-work-flo='cd /home/kicky/work/01-active/Flo-manager/flo_lets_fit; cursor .; gemini'
alias gemini-work-clinic='cd /home/kicky/work/01-active/clinic-scheduler; cursor .; gemini'
alias gemini-work-devfusion='cd /home/kicky/work/01-active/devfusion-portfolio; cursor .; gemini'
alias gemini-work-focus='cd /home/kicky/work/01-active/focus; cursor .; gemini'
alias gemini-work-woodcraft='cd /home/kicky/work/01-active/woodcraft-mob; cursor .; gemini'
alias gemini-work-template='cd /home/kicky/work/05-templates/client-boilerplate-template; cursor .; gemini'

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='nvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch $(uname -m)"

# Set personal aliases, overriding those provided by Oh My Zsh libs,
# plugins, and themes. Aliases can be placed here, though Oh My Zsh
# users are encouraged to define aliases within a top-level file in
# the $ZSH_CUSTOM folder, with .zsh extension. Examples:
# - $ZSH_CUSTOM/aliases.zsh
# - $ZSH_CUSTOM/macos.zsh
# For a full list of active aliases, run `alias`.
#
# Custom version display functions
versions() {
  echo "🔧 Development Environment Versions:"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  # Node.js
  if command -v node &> /dev/null; then
    echo "📦 Node.js:    $(node --version)"
  fi

  # npm
  if command -v npm &> /dev/null; then
    echo "📋 npm:        $(npm --version)"
  fi

  # Bun
  if command -v bun &> /dev/null; then
    echo "🥯 Bun:        $(bun --version)"
  fi

  # Python
  if command -v python3 &> /dev/null; then
    echo "🐍 Python:     $(python3 --version | cut -d' ' -f2)"
  fi

  # UV
  if command -v uv &> /dev/null; then
    echo "🏃 UV:         $(uv --version | cut -d' ' -f2)"
  fi

  # Git
  if command -v git &> /dev/null; then
    echo "📝 Git:        $(git --version | cut -d' ' -f3)"
  fi

  # Docker
  if command -v docker &> /dev/null; then
    echo "🐳 Docker:     $(docker --version | cut -d' ' -f3 | cut -d',' -f1)"
  fi

  # DNF
  if command -v dnf &> /dev/null; then
    echo "📦 DNF:        $(dnf --version | head -n1 | cut -d' ' -f2)"
  fi

  # Zsh
  if command -v zsh &> /dev/null; then
    echo "🐚 Zsh:        $(zsh --version | cut -d' ' -f2)"
  fi

  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# Quick version display
v() {
  local versions=()

  [[ -x "$(command -v node)" ]] && versions+=("Node: $(node --version)")
  [[ -x "$(command -v python3)" ]] && versions+=("Python: $(python3 --version | cut -d' ' -f2)")
  [[ -x "$(command -v git)" ]] && versions+=("Git: $(git --version | cut -d' ' -f3)")
  [[ -x "$(command -v docker)" ]] && versions+=("Docker: $(docker --version | cut -d' ' -f3 | cut -d',' -f1)")

  # Join array elements with " | "
  (IFS=" | "; echo "${versions[*]}")
}

# Fedora-specific aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias dnf-search='dnf search'
alias dnf-info='dnf info'
alias update='sudo dnf update'
alias install='sudo dnf install'

# Development aliases
alias python='python3'
alias pip='pip3'

# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

alias claude="/home/kicky/.claude/local/claude"

# Monitor switching aliases (INSTANT with gdctl)
alias m0='~/bin/monitors/gdctl-instant.py DP-2'
alias m1='~/bin/monitors/gdctl-instant.py DP-4'
alias m3='~/bin/monitors/gdctl-instant.py triple'
alias mlist='~/bin/monitors/gdctl-instant.py show'
alias mshow='gdctl show'
alias mreset='~/bin/monitors/monitors-reset'
