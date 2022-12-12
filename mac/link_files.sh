ln -s $(pwd)/.zshrc ~/.zshrc
ln -s $(pwd)/../vim/.vimrc ~/.vimrc
mkdir -p ~/.matplotlib/stylelib
ln -s $(pwd)/../python/matplotlib/*.mplstyle ~/.matplotlib/stylelib/
