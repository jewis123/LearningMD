## **Xcode教程**

#### 熟悉编程语言

[objectC基础语法](https://www.runoob.com/ios/ios-objective-c.html)

[c基础语法](https://www.runoob.com/cprogramming/c-data-types.html)

#### 文件类型

.mm文件：可以包含`c，c++，object-C`代码

.m文件：只可以包含`Objective-C, C`代码

.bundle目录：静态库的资源内容

.framework目录：静态库（不包含资源）

.a目录：一站式静态库分享方案，包含了资源文件、库文件。

## **Unity+IOS原生交互**

### **交互方式**

#### **C#侧**

添加`[DllImport("__Internal")]`使得`C#`和`C`交互

```
using System.Runtime.InteropServices;
public static class PhoneInfo
{
#if UNITY_IPHONE
    //导入定义到.mm文件中的c函数
    [DllImport("__Internal")]
    private static extern string carrierName();
    
    //C#外部函数调用C
    public static void GetCarrierName(){
        return carrierName();
    }
#endif
}
```

#### **xcode侧**

在Unity中创建一个[.mm文件](https://blog.csdn.net/weixin_42433480/article/details/90173887)，并提供`C#`侧调用所需的`C`函数，在C函数中沟通`Object-C`

```
extern "C"
{
    //网络运营商名称
    char * carrierName()
    {
        NSString *name = [PhoneInfo CarrierName]; /*实例了一个Object-C类*/
        const char * _output =[name UTF8String];
        char* res = (char*)malloc(strlen(_output)+1);
        strcpy(res, _output);
        return res;
    }
}
```

实现C中需要的Object-C类型

```
#import <CoreTelephony/CTTelephonyNetworkInfo.h>
#import <CoreTelephony/CTCarrier.h>

/*类声明*/
@interface PhoneInfo : NSObject
+(NSString*) CarrierName;  
@end

/*类函数实现*/
@implementation PhoneInfo
+ (NSString*)CarrierName
{
    CTTelephonyNetworkInfo *info = [[CTTelephonyNetworkInfo alloc] init];
    CTCarrier *carrier = [info subscriberCellularProvider];
    if (!carrier.isoCountryCode || [carrier carrierName] == nil)
    {
        /*设备处于飞行模式。
         设备中没有SIM卡。
         该设备不在蜂窝服务范围内。*/
        return  @"NULL";
    }
    else
    {
        NSString *moblie = [carrier carrierName];
        return moblie;
    }
}
```

#### **此外，如果需要导入别的依赖**

在OnPostProcessBuild函数里使用[UnityEditor.iOS.Xcode.PBXProject](https://docs.unity3d.com/ScriptReference/iOS.Xcode.PBXProject.html)

(待补充)

#### **OC回调Unity**

方式一：

C调用UnitySendMessage(objName, callbackFuncName, str);

这种方式接口声明固定，只能回调obj身上挂载脚本中的public void method(string message)

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=NzUxYTg0ZTdmZWMxNTAwN2JhZjAxYzhjODUzNTNiYzFfREVMa2d2anl0dmhZSmZtU21CY0xrU3g3UHdwajhoNUVfVG9rZW46Ym94Y25yUzh1QklWWFllMDFpTFUyY2xVZXVoXzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=YTBmMDhlNWFjZGVmMmJmZTYwNWIyMjcyMDUzODRhYjVfQ0VEU0wxVmdrUnFGVE1NWWFQdVBsQm9BRWZLMmx4ZlVfVG9rZW46Ym94Y25EZnZlSTZUTlBIeHdscTFGUVhaU1ZnXzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

方式二：

C#传委托给C的函数指针。

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=OTk5MDE0NWEzMGNjZjYzMjYwNjIyZTgzNDE4NjI2NWFfNmVHVXVJT3Q1aVVsTWo4dVdMZGlTNFFBY1dndmJkUVdfVG9rZW46Ym94Y25lWlYwMEtNbmJXSDVBVmE1RU1OUmplXzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTVjZWUxNzZmMmFiMjAzNjgwOGI3NGMyMWJlODExM2ZfcExyZzQ3UUZiMTZOOFpTZTBOeHZQSzU2Mk1Wamtkc2dfVG9rZW46Ym94Y256YmIwV1VJQTJ2dXQ0TUxMdkI1VWVnXzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

**参考**

[iOS开发之OC回调Unity](https://blog.csdn.net/IceTeaSet/article/details/53142929)的两种方法：UnitySendMessage和函数指针。

### **导出Xcode工程**

.mm文件写好后，直接把Unity工程导出为xcode工程，后续调试iOS原生代码，直接在xcode中进行。这样能够直接通过xcode调试，节省时间。

**注**：每次导出的和原先的工程是不一样的。

#### **打开Xcode工程**

导出完后，双击导出的xcode工程，打开工程。

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=MmRjZTFmNmUyNjQ2YzY1ZWRhODMyMWRkMmMyYzg1YjVfTVBXeHJpa09yRzY0U1YxNXNNaG12Tk96VFk1azhGRzhfVG9rZW46Ym94Y25TanlNR3JXSDFQb0hZcU1oeXUwWUN4XzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

接下来就是实现xcode功能。这里需要了解C数据类型和OC数据类型之间的转化方式。

#### **真机测试**

功能做完之后需要测试：需要配置app的签名和团队。自动选择签名如果不对，就手动指定。

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=MmU1NDk1YmZhZWU1NTkyYWVlNWNmOTdlOWMxYzRmYjVfeU9hN2RNTG9NRnBNa21jN2NOaVM0eWZRV2VobFVaekpfVG9rZW46Ym94Y25vOXVpekVNWE1lTU53Y2t5WnBMMW1oXzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

然后点击箭头按钮，Build, 在真机上测试功能。

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=MDU3MzZlNjZmMzdkYWFhMjBlYzViZjYzNDIyMWUzNzZfbTZiQ2tKM0pUT3JZeHJKWlJVaXFjZHNHcVNwbEIwdWFfVG9rZW46Ym94Y25ReFBGeHFtdE93YkF3amJJNjY0S241XzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

build完，调试完了之后，需要archive编译保存一下。

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=YTYxNzkxMTk4YTI5NmU5NTEyOGE4ZjBjYzY0M2QyNTZfRFFqM2NNSE9RQ1BNR2FKZDJqOFZmcHg2a1JiQ1VXU0lfVG9rZW46Ym94Y25FcTNRSWtxckUxUWJTcXF0Ylk2dE5kXzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

### 将修改同步到Unity

![img](https://youzu.feishu.cn/space/api/box/stream/download/asynccode/?code=MTExMGE4ZDVkOGM2MjMzZWU3YzJmOTNhZTNlY2U3NDBfejJMQ2hEc0k1cWFNeHJOT3dIaTdoU3ZRcHlrRDVpbHFfVG9rZW46Ym94Y24zd1Zjb3J5R1k3eUhEWlJIRU9wemZmXzE2MTI5MzA4ODI6MTYxMjkzNDQ4Ml9WNA)

这一步就是简单的将文件夹直接复制到Unity工程相同地方。

由于原生功能需求比较简单，所以只一个mm文件即可。

### 扩展阅读

如果sdk功能比较重，就需要将sdk分装成framework，然后放到Unity中去调用。

[Xcode Unity 项目 Framework 封包](https://blog.csdn.net/kan464872327/article/details/106758783)