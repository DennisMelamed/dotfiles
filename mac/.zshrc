test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

# Set PATH, MANPATH, etc., for Homebrew.
eval "$(/opt/homebrew/bin/brew shellenv)"

#autoload -U promptinit; promptinit
#prompt spaceship
eval "$(starship init zsh)"

alias l='ls -lh'
export CLICOLOR=1
#find /code/repo/root/dir -type f -exec grep -Hni -C3 "case-insensitive-string-to-match" {} \;
export PATH="/usr/local/bin/:/opt/homebrew/opt/openjdk/bin:$PATH"


#myssh() {
#    session_name=base
#    if [ "$TERM_PROGRAM" = "iTerm.app" ]
#    then
#        ssh -t $1 "bash ~/select_tmux.sh"
#    else
#        ssh -t $1 ""
#    fi
#}

# >>> mamba initialize >>>
# !! Contents within this block are managed by 'mamba init' !!
export MAMBA_EXE='/opt/homebrew/opt/micromamba/bin/micromamba';
export MAMBA_ROOT_PREFIX='/Users/dennis.melamed/micromamba';
__mamba_setup="$("$MAMBA_EXE" shell hook --shell zsh --root-prefix "$MAMBA_ROOT_PREFIX" 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias micromamba="$MAMBA_EXE"  # Fallback on help from mamba activate
fi
unset __mamba_setup
# <<< mamba initialize <<<

# Created by `pipx` on 2024-02-16 15:03:59
export PATH="$PATH:/Users/dennis.melamed/.local/bin"
# switch if need access to my regular github
#
#export GIT_SSH_COMMAND='ssh -i ~/.ssh/id_rsa_yorick_to_hamlet  -o IdentitiesOnly=yes'
export GIT_SSH_COMMAND='ssh -i ~/.ssh/id_ed25519  -o IdentitiesOnly=yes'
[ -f "${HOME}/.google-drive-upload/bin/gupload" ] && [ -x "${HOME}/.google-drive-upload/bin" ] && PATH="${HOME}/.google-drive-upload/bin:${PATH}"


## openeb
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
export HDF5_PLUGIN_PATH=$HDF5_PLUGIN_PATH:/usr/local/lib/hdf5/plugin

check_cmd()
{
    if ! command -v $1 &> /dev/null
    then
        echo "could not find $1, install first before running"
    fi
}


mdrender()
{
    check_cmd glow
    check_cmd entr
    check_cmd find
    echo $1
    find . -name "$1" | entr -c glow -p "$1"
}
