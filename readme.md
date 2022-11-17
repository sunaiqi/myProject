## 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```

## 自动化用例与测试管理-自动化用例库中用例关联方式：当前支持通过用例id关联，使用示例（测试方法testFoo()下通过id=用例id，匹配多条功能用例用英文逗号","隔开）：

```
def testFoo():
  """
  id="1500,1600"
  """
```
