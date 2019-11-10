之前的预备知识能让我们掌握shader的基本用法，并且写出一些简单的shader。这次我们通过积雪效果来更进一步的了解shader是如何结合数学，实现效果。
另外注意，关注有强烈光照需求的shader才使用surface shader，否则使用VF shader就可。
```
Shader "Custom/SnowEffect" {   //定义shader的路径
	Properties{
	
       _MainTex("Albedo (RGB)", 2D) = "white" {}       //要使用的纹理

	//定义了默认值为“bump”的2D类型的纹理_Bump，初始值为空。
	  _Bump("Bump",2D) = "bump"{}

	  _Snow("Snow Level",Range(0,1)) = 0            
	  _SnowColor("Snow Color",Color) = (1,1,1,1)
	  _SnowDirection("Snow Direction",Vector) = (0,1,0)  //默认水平方向，值为1，而不是-1
	  _SnowDepth("Snow Depth",Range(0,0.3)) = 0.1        //积雪厚度
	}
		SubShader{
            //在脚本中可以通过判断rendertype来做一些处理，比如shader替换、shader关闭
			//参考：  https://blog.csdn.net/nnsword/article/details/17840439   类型
			//        https://blog.csdn.net/zmafly/article/details/51141011    作用
			//       http://lib.csdn.net/article/unity3d/44793                解析
			Tags { "RenderType" = "Opaque" }

			CGPROGRAM        //shader的正文

            //声明surface shader 函数名，光照类型，使用的顶点函数（自定顶点函数名为vert）
			#pragma surface surf Lambert vertex:vert  

		  //添加对PROPERTIES的引用
		  sampler2D _MainTex;
		  sampler2D _Bump;
		  float _Snow;
		  float4 _SnowColor;
		  float4 _SnowDirection;
		  float _SnowDepth;

		  struct Input {
			  float2 uv_MainTex;

			  //添加一个变量float2 uv_Bump来获得_Bump纹理的uv坐标。
			  float2 uv_Bump;
			  //获取世界坐标下的法向值
			  float3 worldNormal;
			  INTERNAL_DATA
		  };

		  void surf(Input IN, inout SurfaceOutput o) {
			  //tex2D对纹理进行采样
			  half4 c = tex2D(_MainTex, IN.uv_MainTex);
			  o.Albedo = c.rgb;
			  o.Alpha = c.a;

			  //tex2D根据输入参数的类型，获取对应含义的值，此处从_Bump纹理中提取法向信息
			  //UnpackNormal函数的作用就是将tex2D函数获取到的fixed4类型值转换成fixed3类型的值
			  o.Normal = UnpackNormal(tex2D(_Bump, IN.uv_Bump));

			  //得到世界坐标系下的真正法向量（而非凹凸贴图产生的法向量，要做一个凹凸贴图法向值到世界坐标系法向值的转化）和雪落
			  //下相反方向的点乘结果，即两者余弦值，并和_Snow（积雪程度）比较
			  if (dot(WorldNormalVector(IN, o.Normal), _SnowDirection.xyz) > lerp(1, -1, _Snow))
			  {
				  /*
				  我们知道，余弦值是-1和1之间的一个数，越接近于1，说明该点法向与雪落下相反方向越一致，当为-1时，说明两者方向相反。
				 此处我们可以看出_Snow参数只是一个插值项，当上述夹角余弦值大于
				  lerp(1,-1,_Snow)=1-2*_Snow时，即表示此处积雪覆盖，所以此值越大

				  多讲一点，lerp的第三个参数是一个（0，1）之间的比例因子，代表所处前两个参数范围的位置
				  注意为了符合正常的自然现象，我们_Snow一般只取0~0.5，因为大于0.5时，插值的结果将小于0，会造成雪好像穿过了岩石，落到了岩石的后面。这个道理和光照的道理一样，物体背面是见不到阳光的。
				  */

				  //积雪程度程度越大。此时给覆盖积雪的区域填充雪的颜色
				  o.Albedo = _SnowColor.rgb;
			  }

			  else      //否则表示未覆盖
			  {
				  o.Albedo = c.rgb;
			  }

			  o.Alpha = 1;

		  }
		  //自定义顶点函数
		  /*
		     参数appdata_full v，参数的类型为appdata_full（Unity内置类型），该类型包含了纹理坐标，法向量，顶点位置，以及切线信息
		  */
		  void vert(inout appdata_full v)
		  {
			  //将_SnowDirection从世界坐标系转换到模型的局部坐标系下
			  /*
			      将_SnowDirection乘以Unity内置矩阵 – UNITY_MATRIX_IT_MV
				  （IT表示Inverse Transpose逆转置矩阵，MV表示 ModelView矩阵，该矩阵表示是ModelView的逆转置矩阵）。
			    现在我们得到了该顶点的法向量。
				_Snow*2/3，这表示只有那些更接近雪落下方向的区域才会增加雪的厚度，更符合自然现象。
			    而这些通过测试的区域，沿着(sn.xyz+v.normal)方向进行加厚，也就是将其顶点沿此方向伸展一定距离。
				注意到增厚的程度取决于_SnowDepth和_Snow，而增厚的方向是由物体法向和雪落的方向综合作用的，这也符合自然现象。
			  */
			   float4 sn = mul(UNITY_MATRIX_IT_MV, _SnowDirection);

			   if (dot(v.normal, sn.xyz) >= lerp(1, -1, (_Snow * 2) / 3))
				   v.vertex.xyz += (sn.xyz + v.normal) * _SnowDepth * _Snow;
		   }
			   ENDCG
	  }
		  FallBack "Diffuse"      //shader失败时回滚
}

```

![调节箭头所指落雪方向可以改变落雪效果](http://upload-images.jianshu.io/upload_images/3806085-83d4a9e231969666.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)