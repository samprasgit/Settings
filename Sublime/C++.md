Mac

```
{
    "cmd": ["clang++", "${file}","-std=c++11", "-stdlib=libc++", "-o", "${file_path}/${file_base_name}"],
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "working_dir": "${file_path}",
    "selector": "source.c, source.c++",
    "cmd": ["bash", "-c", "g++ '${file}' -o '${file_path}/${file_base_name}' && open -a Terminal.app '${file_path}/${file_base_name}'"],
    "variants":
    [
        {
            "name": "Run",
            "cmd": ["bash", "-c", "clang++  '${file}' -std=c++11 -stdlib=libc++ -o '${file_path}/${file_base_name}' && '${file_path}/${file_base_name}'"]
        }
]}
```

Win10