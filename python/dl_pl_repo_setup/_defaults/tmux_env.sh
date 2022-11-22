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
#    tmux send-keys -t 'Main' 'zsh' C-m 'clear' C-m # Switch to bind script?
    tmux new-window -t $SESSION:1 -n 'Data'
    tmux send-keys -t 'Data' 'cd ./data' C-m 
    tmux new-window -t $SESSION:2 -n 'Models'
    tmux send-keys -t 'Models' 'cd ./models' C-m 
    tmux new-window -t $SESSION:3 -n 'Configs'
    tmux send-keys -t 'Configs' 'cd ./configs' C-m 

    # Create and setup pane for tensorboard
    tmux new-window -t $SESSION:4 -n 'Monitors'
    tmux send-keys -t 'Monitors' 'source *_venv/bin/activate && tensorboard --logdir=./experiments' C-m 
    tmux split-window -vf -t "Monitors"
    tmux send-keys -t 'Monitors.1' "watch -n 10 'df -h'" C-m 
    tmux resize-pane -t 'Monitors.1' -U 10
    tmux split-window -hf -t "Monitors"
    tmux send-keys -t 'Monitors.2' 'watch -n 3 nvidia-smi' C-m 

fi

# Attach Session, on the Main window
tmux attach-session -t $SESSION:0
