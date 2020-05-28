- 区分toolTip、statusTip、whatsThis

  . toolTip属性设置部件的toolTip提示信息，toolTip提示信息在鼠标放到控件上会浮动出一个小框显示提示信息。

  . statusTip提示信息在鼠标放到控件上时在窗口的状态栏显示提示信息

  . whatsThis的帮助信息一般在部件获得焦点后按Shift+F1弹出显示

- 区分LineEdit, TextEdit, PlainTextEdit, TextBrowser

- QLineEdit中`textEdited`和`textChanged`区别

  文本编辑修改发出textEdited信号；动态赋值发出textChanged信号

  