Mac 

参考

https://harttle.land/2015/07/18/vim-cpp.html

[nvim 与vim 区别](https://www.jianshu.com/p/f2a208de7f59)

[安装使用配置Neovim](https://www.jianshu.com/p/c382222e5151)

[Linux 下 Neovim 安装与配置 Python 开发环境指南]([https://jdhao.github.io/2018/09/05/centos_nvim_install_use_guide/#%E6%9B%B4%E6%94%B9%E6%98%BE%E7%A4%BA%E5%AD%97%E4%BD%93-font](https://jdhao.github.io/2018/09/05/centos_nvim_install_use_guide/#更改显示字体-font))



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

基本配置：

```shell
call plug#begin('~/.local/share/nvim/plugged')

Plug 'scrooloose/nerdtree'
" 主题
Plug 'morhetz/gruvbox'
Plug 'numirias/semshi', {'do' : ':UpdateRemotePlugins'}
" 语法检查
Plug 'neomake/neomake'
" 自动补全
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'zchee/deoplete-jedi'
" 括号匹配
Plug 'jiangmiao/auto-pairs'

call plug#end()


" 主题
colorscheme gruvbox
"set background=dark " 或者 set background=light
" 语法检查 忽视警告
let g:neomake_python_enabled_makers = ['pyflakes']
call neomake#configure#automake('nrwi', 500)	" 自动检查
" 代码补充的键位替换
inoremap <expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"
let g:deoplete#enable_at_startup = 1

map ,q :call CompileRunGcc()<CR>
" 一键执行
func! CompileRunGcc()
    exec "w"
    if &filetype == 'c'
        exec '!g++ % -o %<'
        exec '!time ./%<'
    elseif &filetype == 'cpp'
        exec '!g++ % -o %<'
        exec '!time ./%<'
    elseif &filetype == 'python'
        exec '!python %'
    elseif &filetype == 'sh'
        :!time bash %
    endif                                                                       
endfunc<Paste>

" 键位的映射
noremap T :NERDTree<CR>
noremap ,l :sp<CR><C-w>j:term ipython<CR> i %run 

set guifont=Courier/20
set foldenable      " 允许折叠  
set showcmd         " 输入的命令显示出来，看的清楚些 
set shortmess=atI   " 启动的时候不显示那个援助乌干达儿童的提示 
" 语法高亮
set syntax=on
" 自动缩进
set autoindent
set cindent
" Tab键的宽度
set tabstop=4
" 匹配括号高亮的时间（单位是十分之一）
set matchtime=1
"去掉讨厌的有关vi一致性模式，避免以前版本的一些bug和局限  
set nocompatible  
"设置编码
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
" 括号匹配
set showmatch
" 鼠标
set mouse=a
set selection=exclusive
set selectmode=mouse,key
" 显示行号
set number
" 高亮当前行
set cursorline
" 设置空白字符的视觉提示
set list listchars=extends:❯,precedes:❮,tab:▸\ ,trail:˽


```

