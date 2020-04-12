1、新建一个插件（Tools --- Developer --- New Plugin）写入如下内容，并保存为 head.py

```python
import sublime
import sublime_plugin
import datetime


class PyHeadCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.run_command("insert_snippet",
                              {
                                  "contents":
                                  "# !/usr/bin/env python""\n"
                                  "# -*- coding:utf-8 -*- ""\n"
                                  # "# 作者: xxxx""\n"
                                  # "# 邮箱: xxxx@qq.com\n"
                                  "# time: ""%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                                  "# 描述: xxxx""\n"
                                  "\n"
                              }
                              )
```

2、定义快捷键（Preferences --- Key Bindings），加入如下一行，这样按 Ctrl + Enter 就能添加头部注释信息了，快捷键可以自定义

```python
{"command":"py_head","keys":["ctrl+enter"]},
```

