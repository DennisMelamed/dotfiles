#!/bin/sh

# Set Session Name
SESSION=${PWD##*/}
echo $session
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)

# Only create tmux session if it doesn't already exist
if [ "$SESSIONEXISTS" = "" ]
then
    # Start New Session with our name
    tmux new-session -d -s $SESSION

    # Name first Pane and start zsh
    tmux rename-window -t 0 'Main'
    tmux split-window -vf -t 'Main'
#    tmux send-keys -t 'Main' 'zsh' C-m 'clear' C-m # Switch to bind script?

    # Create and setup pane for tensorboard
    tmux new-window -t $SESSION:1 -n 'Tensorboard'
    tmux send-keys -t 'Tensorboard' 'source *_venv/bin/activate && tensorboard --logdir=./experiments' C-m # Switch to bind script?

fi

# Attach Session, on the Main window
tmux attach-session -t $SESSION:0
