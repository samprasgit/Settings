```
sudo yum update&&sudo yum -y install zsh
chsh -s /bin/zsh

sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh

```

zsh-syntax-highlighting
安装方法：

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

zsh-autosuggestions
它可以记录输入过的命令并给予建议
安装方法：

```
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

