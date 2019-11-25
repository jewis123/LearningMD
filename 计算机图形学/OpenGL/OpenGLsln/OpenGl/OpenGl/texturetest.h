#ifndef TEXTURETEST_H
#define TEXTURETEST_H

#include <iostream>
#include <GLFW/glfw3.h>
#include "shader_s.h"
#include "stb_image.h"
using namespace std;

void helloTexture(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*));

class HelloTexture {
public:
	void Do(GLFWwindow* window, void processInput(GLFWwindow*)) {
		Shader ourshader("shaders/HelloTexture/usetexture.vertex", "shaders/HelloTexture/usetexture.frag");
		helloTexture(window, ourshader, processInput);
	}

	void helloTexture(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*)) {
		float vertices[] = {
			//     ---- 位置 ----       ---- 颜色 ----     - 纹理坐标 -
			 0.5f,0.5f, 0.0f,           1.0f, 0.0f, 0.0f,     1.0f, 1.0f,   // 右上
			 0.5f,-0.5f, 0.0f,           0.0f, 1.0f, 0.0f,     1.0f, 0.0f,   // 右下
			-0.5f, -0.5f, 0.0f,          0.0f, 0.0f, 1.0f,     0.0f, 0.0f,   // 左下
			-0.5f, 0.5f, 0.0f,          1.0f, 1.0f, 0.0f,     0.0f, 1.0f    // 左上
		};
		
		unsigned int indices[] = {
			0, 1, 3, // first triangle
			1, 2, 3  // second triangle
		};
	

		unsigned int VBO, VAO, EBO;
		glGenVertexArrays(1, &VAO);
		glGenBuffers(1, &VBO);
		glGenBuffers(1, &EBO);

		glBindVertexArray(VAO);

		glBindBuffer(GL_ARRAY_BUFFER, VBO);
		glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

		// position attribute
		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)0);
		glEnableVertexAttribArray(0);
		// color attribute
		glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(3 * sizeof(float)));
		glEnableVertexAttribArray(1);
		// texture coord attribute
		glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(6 * sizeof(float)));
		glEnableVertexAttribArray(2);


		unsigned int  texture1, texture2;
		// 设置第一张纹理
		glGenTextures(1, &texture1);
		glBindTexture(GL_TEXTURE_2D, texture1);
		// 设置纹理环绕方式
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);	
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
		// 设置纹理过滤方式
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

		int width, height, nrChannels;
		unsigned char *data = stbi_load("resources/container.jpg", &width, &height, &nrChannels, 0);
		if (data)
		{
			glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
			glGenerateMipmap(GL_TEXTURE_2D);
		}
		else
		{
			cout << "Failed to load texture" << endl;
		}
		stbi_image_free(data);

		////设置第二张纹理
		glGenTextures(1, &texture2);
		glBindTexture(GL_TEXTURE_2D, texture2);

		//设置横纵向纹理环绕方式
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

		//设置纹理过滤方式
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

		//加载纹理
		stbi_set_flip_vertically_on_load(true); // 图片的原点在左上角，OpenGL原点在左下角，通过stb_image.h 把加载的图片按照 y 轴翻转.
		data = stbi_load("resources/bean.jpg", &width, &height, &nrChannels, 0);
		if (data) {
			glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
			glGenerateMipmap(GL_TEXTURE_2D);
		}
		else
		{
			cout << "Failed to load texture" << endl;
		}
		stbi_image_free(data);

		shaderProgram.use();
		//绑定纹理，将不同纹理绑定到不同纹理单元
		shaderProgram.setInt("texture1", 0);   
		shaderProgram.setInt("texture2", 1);

		// render loop
		// -----------
		while (!glfwWindowShouldClose(window))
		{
			processInput(window);
			glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
			glClear(GL_COLOR_BUFFER_BIT);

			// bind textures on corresponding texture units
			glActiveTexture(GL_TEXTURE0);
			glBindTexture(GL_TEXTURE_2D, texture1);
			glActiveTexture(GL_TEXTURE1);
			glBindTexture(GL_TEXTURE_2D, texture2);

			//// bind Texture  只有一个纹理单元时，在绑定时会默认激活这个纹理单元
			//glBindTexture(GL_TEXTURE_2D, texture1);

			shaderProgram.use();
			glBindVertexArray(VAO);
			glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

			glfwSwapBuffers(window);
			glfwPollEvents();
		}

		glDeleteVertexArrays(1, &VAO);
		glDeleteBuffers(1, &VBO);
		glDeleteBuffers(1, &EBO);
	}

	//课后作业
	// 问题1：修改片段着色器，仅让笑脸图案朝另一个方向看
	//	   错误：修改纹理顶点，左右对换？不行，这会让其他纹理也被影响。可以尝试把修改顶点中的纹理坐标，看看效果
	//    正确：注意前半句，我们在采样第二块纹理的时候把纹理坐标先按X轴翻转，这样只有第二块纹理坐标是左右互换的。
	//    思考：想想一下四个顶点水平互换就是需要的效果，公式就是 1-x  。  后续课程会详细接触变换。
	//问题2：修改纹理坐标取值范围，修改纹理环绕方式，让笑脸分布在箱子四个角落
	//    错误：还是不能直接修改顶点的纹理坐标
	//    正确：有了上题基础，我们知道还是得在片段着色器中修改获取到的纹理坐标，将其*2即可。
	//    思考：为什么*2后采样到的图像变小了，不是猜测的放大两倍？
	//    原因：纹理坐标的乘法更好的理解方式是在一个纹理在这个纹理坐标的每个轴方向上平铺几次。因为我们知道正常的纹理坐标取值范围在【0，1】，做乘法后势必用到纹理环绕方式，而纹理环绕方式会让纹理在正常范围内变化
	//问题3：使用uniform修改多纹理采样比例
	//    思考：渲染循环中，通过glGetUniformLocation找到变量位置，然后使用glUniform操作函数改值，没啥好说的。
	     
};
#endif