Unity内部提供了一些可以直接使用的着色器，这些内置着色器包括以下6个方面：



**1)Performance of Unity shaders**
　　着色器的性能和两个方面有关：shader本身和render path。
　　Deferred Lighting：每个对象都会被绘制2遍，无论其是否受到光照，性能与纹理数和具体的计算过程有关。
　　Vertex Lit：每个对象只被绘制一次，性能与纹理数和具体的计算过程有关。
　　Forward rendering：性能和灯光数量有关。
　　Vertex-Lit shader in Forward rendering path：基于每个顶点计算所有光照的影响，只绘制一遍。
　　Pixel-Lit shader in Forward rendering path：N rendering passes，每个光照会增加一次绘制，性能和物体在屏幕上的尺寸也有关系。
　　性能开销很大，但是可以用来制作一些特殊的效果，比如shadows、normal-mapping、good look specular highlights and light cookies等。
　　通常的shader性能开销排序如下：
　　Unlit 不受光
　　Vertex Lit 顶点光
　　Diffuse 漫反射
　　Normal mapped 法线贴图
　　Specular 高光
　　Normal Mapped Specular 高光法线贴图
　　Parallax Normal mapped 视差法线贴图
　　Parallax Normal Mapped Specular 视差高光法线贴图
**(2)Normal Shader Family**
　　Specular 高光，强度和camera的观察角度有关，main_tex的alpha通道可以用来做Specular Map(反射贴图，也称Gloss Map)，用于定义物体不同区域的反光率的大 
小。
　　Bumped Diffuse 法线贴图漫反射，使用Normal map来表现物体表面的细节。
　　Parallax 视差着色器，通过HeightMap来实现，用来模拟高度信息。这个高度信息可以包含在Normal Map的Alpha通道里，也可以单独包含在一张贴图里面。
　　Decal 贴花着色器，需要主纹理、贴花纹理（带alpha），用来对主纹理追加纹理，可以用来做涂鸦。性能比Vertex-Lit稍大一点，因为它需要多一张纹理。
　　Diffuse Detail 漫反射细节着色器，需要主纹理、细节灰度纹理（50%中性灰）,细节纹理必须是无缝贴图（四方连续的）。
　　细节贴图是细小的，精致的纹理在你靠近一个表面的时候可以察觉，可用于地形细节、木纹、石头纹理等。
**(3)Transparent Shader Family**
　　透明着色器用于实现全透明或者半透明效果。
　　当多层透明时，会出现一些渲染问题。
**(4)Transparent Cutout Shader Family**
　　透明镂空着色器使用的对象有完全不透明的，完全透明的部分（无半透明部分）。像铁栅栏，树木，草等之类的东西。
　　带有Alpha cutoff参数用于控制透明和不透明的范围。
　　没有透明着色器的图形排序问题，并可以接收和进行投影。
**(5)Self-Illuminated Shader Family**
　　主要用于发光物体。
　　一张主帖图，一张自发光纹理。
　　发光基于发光纹理的alpha值，alpha为0的不发光，1表示充分发光。不需要任何灯光照射来发光。
　　任何顶点灯光或像素灯光将简单增加更多光照到自发光上。
**(6)Reflective Shader Family**
　　一张主帖图，一个Cubemap用于反射。
　　主纹理的alpha通道定义在物体表面的反射强度。
　　任何场景灯光将会增加反射表面的照明。**