## Mac

```
{
    "cmd": ["g++", "${file}", "-o", "${file_path}/${file_base_name}"],
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "working_dir": "${file_path}",
    "selector": "source.c, source.c++",

    "variants":
    [
        {
            "name": "Run",
            "cmd": ["zsh", "-c", "g++ '${file}' -o '${file_path}/${file_base_name}' && open -a Terminal.app '${file_path}/${file_base_name}'"]
        }
    ]
}
```

解决cin,scanf问题

```
{
    "cmd": ["clang++", "${file}","-std=c++11", "-stdlib=libc++", "-o", "${file_path}/${file_base_name}"],
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "working_dir": "${file_path}",
    "selector": "source.c, source.c++",
    "cmd": ["zsh", "-c", "g++ '${file}' -o '${file_path}/${file_base_name}' && open -a Terminal.app '${file_path}/${file_base_name}'"],
    "variants":
    [
        {
            "name": "Run",
            "cmd": ["zsh", "-c", "clang++  '${file}' -std=c++11 -stdlib=libc++ -o '${file_path}/${file_base_name}' && '${file_path}/${file_base_name}'"]
        }
]}
```

代码格式化

```
[
    {
        "keys": ["ctrl+alt+l"], "command": "coolformat", "args": {"action": "quickFormat"}
    },
    {
        "keys": ["ctrl+alt+shift+s"], "command": "coolformat", "args": {"action": "selectedFormat"}
    }
]
```



Win10
-------
Win10

```

{
    "cmd": ["g++", "${file}", "-fexec-charset=gbk", "-o", "${file_path}/${file_base_name}"],
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "working_dir": "${file_path}",
    "selector": "source.c, source.c++",
    "variants":
    [
        {
            "name": "Run",
            "cmd": ["cmd", "/c", "g++", "${file}", "-o", "${file_path}/${file_base_name}", "&&", "start", "cmd", "/c", "${file_path}/${file_base_name} & pause"]
        }
    ]
}

```

Linux

``` powershell
{
    "cmd" : ["g++", "$file_name", "-o", "${file_base_name}", "-lm", "-Wall"],
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "selector" : "source.c, source.c++",
    "shell":false,
    "working_dir" : "$file_path",
 
    "variants":
    [
        {
            "name": "Run",
            "cmd": ["gnome-terminal", "-e", "bash -c \"g++ '${file}' -o '${file_path}/${file_base_name}' -lm -Wall && '${file_path}/${file_base_name}' ; read -p '\nPress any key to continue...'\""]
        }
    ]
}

```

>>>>>>> ecee1d40908de0686b8b1369e2e2f0d91a153bc1
