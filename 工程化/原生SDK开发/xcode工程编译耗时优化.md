### 背景情况

Unity在构建xcode工程时，即使C#代码没有发生变化，也会进行全量编译

### 资料

https://networm.me/2018/09/16/unity-xcode-cache/

> - BuildOptions.AcceptExternalModificationsToPlayer这个接口是Unity提供的增量编译的标记位, 但是只有在工程存在的时候可以使用，不然会报错
> - 