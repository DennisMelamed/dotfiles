ln -s $(pwd)/.bashrc ~/.bashrc
ln -s $(pwd)/../vim/.vimrc ~/.vimrc
mkdir ~/.config/matplotlib/stylelib
ln -s $(pwd)/../python/matplotlib/*.mplstyle ~/.config/matplotlib/stylelib/
