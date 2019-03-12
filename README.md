## Baidu_translate
### 由来
首先，这是一个百度翻译接口API破解，衍生而来的小脚本。ok，其实是我自己英语太垃圾，然后昨晚去百度翻译查单词，忽然觉得太麻烦了，就打算写一个解析百度的翻译页面API的爬虫，然后做成命令行工具。
于是，就有了这个小case。

### 依赖
创建软链接：
```bash
sudo ln -s 当前完整路径标识 /usr/bin/cha
```

```python
pip install -r requests.txt
```

### 原理

- 分析百度翻译页面的网络情况，分析加密的js脚本，获取到关键的函数和值的来源或者计算方法。
- 构建关键的请求头和POST携带的数据，对百度接口：[https://fanyi.baidu.com/v2transapi](https://fanyi.baidu.com/v2transapi) 进行数据请求。
- 得到的json数据，再进行分析和解构。
- 输出结果

### 支持
- 自动中文查英文互查
- 语句查询
- 帮助信息（-h）

### 心得
- 分析百度的页面，主要注意js加载的部分，寻找到js生成的关键参数是什么。
- 通过针对的api的接口，去查看有关的js脚本。可以复制到编辑器格式化搜索关键字。
- 相关的逻辑，大多数是写在附近的，而不会是东拼西凑来的。所有，注意观察关键字部分的代码，寻找蛛丝马迹～
- Google浏览器支持在线debug，一步步跳入查看变量和函数，配合关键的脚本去查询。
- js中可能含有python无法直接读取的字符串，可以使用raw格式去读取和修改。js2py听说比execpy更快，可以试试。
- 待续

### 更多功能（暂未实现）
- 调用系统功能，播放语音（读音）
- 更好的代码结构优化和设计优化
- 更优秀的界面和输出结果解构
- 对使用者的操作有更高的容错率，对错误的处理和记录相关日志功能。
- 等等

### 最后我想说

- 我知道自己写得很垃圾 = =
- 并且，真诚的希望得到朋友们的指点，说真的，如果有任何建议或者意见，请给我发邮件，谢谢。
- 有任何问题，可以联系我邮箱。

### 相关资源推荐
- [百度翻译爬虫（JS加载） - 补发课程_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/video/av25542134)
- [百度翻译接口 破解 - hujingshuang - CSDN博客](https://blog.csdn.net/hujingshuang/article/details/80180294)
- [hujingshuang/MTrans: Multi-source Translation](https://github.com/hujingshuang/MTrans)
- [Python计算字符宽度的方法_python_脚本之家](https://www.jb51.net/article/86577.htm)
- [Python3使用Print输出带颜色字体 - 比特量化 - 博客园](https://www.cnblogs.com/fangbei/p/python-print-color.html)
