Mac 

参考

https://harttle.land/2015/07/18/vim-cpp.html

[nvim 与vim 区别](https://www.jianshu.com/p/f2a208de7f59)

[安装使用配置Neovim](https://www.jianshu.com/p/c382222e5151)



Vundle安装

```shell
git clone https://github.com/VundleVim/Vundle.vim.git ~/.config/nvim/bundle/Vundle.vim
# vimrc首部添加
set nocompatible " be iMproved, required
filetype off " required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'

call vundle#end()
filetype plugin indent on

# 安装脚本
:PluginInstall

# cmd
nvim +PluginInstall +qall

```

[Vim-Plug](https://github.com/junegunn/vim-plug)

```shell
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

补全框架

- [nvim-completion-manager](https://github.com/roxma/nvim-completion-manager)
- 