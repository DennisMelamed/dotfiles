test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"
#autoload -U promptinit; promptinit
#prompt spaceship
eval "$(starship init zsh)"

alias l='ls -lh'
export CLICOLOR=1
#find /code/repo/root/dir -type f -exec grep -Hni -C3 "case-insensitive-string-to-match" {} \;
