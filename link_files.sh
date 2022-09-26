ln -s $(pwd)/.bashrc ~/.bashrc
ln -s $(pwd)/.vimrc ~/.vimrc
mkdir ~/.config/matplotlib/stylelib
ln -s $(pwd)/matplotlib/*.mplstyle ~/.config/matplotlib/stylelib/
