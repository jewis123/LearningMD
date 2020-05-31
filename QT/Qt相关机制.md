[TOC]

## 源起QObject

作为所有Qt对象模型的核心，QObject足以在讨论所有Qt对象子类前被拿出来讨论一番。它是许多强大机制的源泉。接下来会讨论其相关的几个相对重要的内容。

1） QObject组成的树叫做对象树，做客户端的对对象树这个概念肯定不陌生，通过这棵对象树我们能轻易得获取任意一个对象

2） QObject提供了信号槽机制，使得对象通信变得更加解耦，灵活。（另外开篇讨论）

3） 通过QObject能够获取到元对象（MetaObject），利用反射机制获取到该类型相关的所有信息。

4） 使用QObject实现多线程。（详见网页资料txt），[另,手册对应讲解](https://doc.qt.io/qt-5/qobject.html#thread-affinity)

## 元对象系统和反射机制

### 之于反射的运用

- 什么是反射机制

  ​	反射机制就是指在`运行时`能够`动态的`获取到类对象的的所有类型信息、属性、成员函数等信息的一种机制。主要为了能够给C++这种静态语言增加一些类似动态语言的特性。

- 元对象系统提供的功能之一是为 QObject 派生类对象提供运行时的类型信息及数据成 员的当前值等信。程序可以获取 QObject 派生类对象所属 类的名称、父类名称、该对象的成员函数、枚举类型、数据成员等信息，其实这就是 反射机制。

- 那么元对象，是什么东西？

  它其实是QT中用来表述对象结构的另一个对象。

### Qt实现反射机制的方法

- 通过一系列类来对对象进行各方面描述。其中MetaObject类描述了QObject及其派生子类的所有元信息，可以说QMetaObject类的对象是Qt中的元对象

- 对对象成员进行描述。一个对象包括数据成员、函数成员、构造函数、枚举成员等。在 Qt 中，这些成员分别使用了不同的类对其进行描述，比如函数成员使用类 QMetaMethod 进行描述，属性使用 QMetaProperty 类进行描述等。然后使用 QMetaObject 类对整个类对象进行描述。

  ```c++
  //比如要获取成员函数的函数名
  QMetaMethod qm = metaObject->method(1);    //获取索引为 1的成员函数 
  qDebug()<<qm.name()<<"\n";    //输出该成员函数的名称。
  ```

### 使用反射机制的条件

- 需要继承QObject, 并在类中加入Q_OBJECT宏

- 注册成员函数：若希望普通成员函数能够被反射，需要在函数声明之前加入`QObject::Q_INVOKABLE` 宏。

- 注册成员变量：若希望成员变量能被反射，需要使用 `Q_PROPERTY` 宏。

- 示例如下所示：

  ```C++
  //1 .继承 QObject 
  class TestObject : public QObject
  {
      // 2.声明Q_OBJECT
      Q_OBJECT 
      //3. Q_PROPERTY 注册成员变量
      Q_PROPERTY(QString text READ text WRITE setText NOTIFY textChange) 
      //4. 注册的成员变量能够响应自定义的signals textChange
      Q_PROPERTY(QString text MEMBER m_text NOTIFY textChange)
  public:
      TestObject(QObject* parent);
      ~TestObject();
      void init();
      //------
      //5.注册类的成员函数
      Q_INVOKABLE QString text(); 
      Q_INVOKABLE void setText(const QString& strText); 
      void g1();    //注意：此函数不会被反射。 
      QString m_text; //类的成员变量
  signals:
      void textChange(); //自定义的signals
  public slots:
      void textslot(){qDebug()<<"textslot"<<endl;} //自定义的signals响应的槽函数
  };
  ```

### 示例简述

- Q_OBJECT 宏展开之后有一个虚拟成员函数 meteObject()，该函数会返回一个指向 QMetaObject 类型的指针，其原型为

  ` virtual const QMetaObject *metaObject() const; `

  因为启动了元对象系统的类都包含 `Q_OBJECT` 宏，所以这些类都有含有 `metaObject()` 虚拟成员函数，通过该函数返回的指针调用 `QMetaObject` 类中的成员函数，便可查询 到`QObject `及其派生类对象的各种信息。    

- Qt 的moc 会完成以下工作：

  为Q_OBJECT 宏展开后所声明的成员函数的成生实现代码 ；

  识别 Qt 中特殊的关键字及宏，比如识别出 Q_PROPERTY 宏、Q_INVOKABLE 宏、slot、signals 等 

- 调用时，就可以通过获取类对象持有的元对象来获取类型信息了。

## 信号和槽原理

### 简述

此所谓的对象之间的通信，从程序设计语言语法角度来看就是函数调用的问题，只不过是某个对象 的成员函数调用另一个对象的成员函数而已。事实上，信号和槽其实是观察者模式的一种实现。

### 函数调用的几种形式

![image-20200531133727669](D:/Learning/trunk/QT/函数结果调用.png)

- f 函数中直接调用 g 函数获取结果。

  存在的问题：1）f 需要知道 g 函数的存在； 2) 如果 g 函数也是调用其他函数处理结果，就形成嵌套

- 使用回调函数。在 f 函数中使用函数指针，在需要的时候取调用，这样就不会被函数名限制。

- Qt信号和槽机制：

  1）创建一个信号，并在需要调用外部函数的时候发送这个信号

  2）关联过这个信号的槽（函数），做出响应的反应

### 信号的创建和槽函数的关联/断开

QObject的各种派生都预定义了各自的信号和槽，当然开发者也能定义自己的信号。

PYQT中定义信号需要派生自QObject类型，而在C++中`signals:`则用来指明信号的定义区域，同时可以使用访问修饰符来限定作用域。

PyQt中槽函数的定义只要和信号匹配上签名就行；在C++中同样要先声明`slots`区域。

在信号和槽在关联时，通过`connect`函数来关联；通过`disconnect`来取消关联，取消关联的槽函数将不再响应信号。

## 对象树和生命周期

### 为什么要使用对象树

GUI通常是存在父子关系的，让父控件维护一系列子控件，使用树的结构能够更加直观的去描述父子关系，能够更好的去管理控件对象。

### 组合模式与对象树

- 组合模式指的是把类的对象组织成树形结构，这种树形结构也称为对象树。

- 主要作用是可以通过根节点对象间接调用子节点中的虚函数，从而可以间 接的对子节点对象进行操作。 

- 基本思想是使用父类类型的指针指向子类对象，并把这个指针存储在一个数组 中(使用容器更方便)，然后每创建一个类对象就向这个容器中添加一个指向该对象的指针。 

- 对象的删除规则

  基本规则：父对象在销毁时会一起销毁子对象

  手动删除对象：会把待删除对象从父对象的子对象列表中一处，避免父对象销毁时二次销毁

  当一个对象被销毁时，会发送destroy信号，可以捕捉该信号避免对QObject对象的悬垂引用。

  

