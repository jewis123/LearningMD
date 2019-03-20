**前言**
shader代码文件的框架在初学的时候是很有必要记住的，它有利于我们理解shader的整个流程，但是当我们写习惯了之后，一遍遍的重写shader框架就很麻烦，同时VSCode并没有带类似需求snippet的插件，于是我们就要自己写snippet,也就是代码片段。
先吹一波VSCode，好灵活好快。
**实现**
点击文件>首选项>用户代码片段，命名好名字，就会以snippet格式保存在工程中。
然后就是编写内容了，json格式很简单。
```
		"Quick write shader framework":   
	{
		"prefix": "fk",
		"body":[
			"Shader \"$1\"{\n\t Properties{$2\n\t}\n\t SubShader{\n\t Tags{$3}\n\t pass{\n\t\t Tags{$4}\n\t\t CGPROGRAM\n\t\t #pragma vertex vert\n\t\t #pragma fragment frag $5\n\t\t #include \"UnityCG.cginc\"\n\t\t struct a2v{$6\n\t\t};\n\t\t struct v2f{$7\n\t\t};\n\t\t v2f vert(a2v v){$8\n\t\t}\n\t\t fixed4 frag(v2f f){$9\n\t\t}\n\t\tENDCG\n\t}\n}\n\tFallback\"Diffuse$10\"\n}"
		]
		 ,
		"description": "快速搭建shader框架"
	}
```
这里的$n代表按下Tab键后光标的移动位置。
保存之后，新建一个shader文件输入fk就能有提示了。完美