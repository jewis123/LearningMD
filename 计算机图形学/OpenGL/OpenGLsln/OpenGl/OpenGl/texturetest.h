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
			 0.5f,  0.5f, 0.0f,           1.0f, 0.0f, 0.0f,     1.0f, 1.0f,   // 右上
			 0.5f, -0.5f, 0.0f,           0.0f, 1.0f, 0.0f,     1.0f, 0.0f,   // 右下
			-0.5f, -0.5f, 0.0f,          0.0f, 0.0f, 1.0f,     0.0f, 0.0f,   // 左下
			-0.5f,  0.5f, 0.0f,          1.0f, 1.0f, 0.0f,     0.0f, 1.0f    // 左上
		};
		unsigned int indices[] = {
			0, 1, 3, // first triangle
			1, 2, 3  // second triangle
		};
	

		GLuint VBO, VAO, EBO;
		glGenVertexArrays(1, &VAO);
		glBindVertexArray(VAO);
		
		glGenBuffers(1, &VBO);
		glBindBuffer(GL_ARRAY_BUFFER, VBO);
		glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

		glGenBuffers(1, &EBO);
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)0);
		glEnableVertexAttribArray(0);
		glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)3);
		glEnableVertexAttribArray(1);
		glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)6);
		glEnableVertexAttribArray(2);


		GLuint texture1, texture2;	
		// 设置第一张纹理
		glGenTextures(1, &texture1);
		glBindTexture(GL_TEXTURE_2D, texture1);

		//设置横纵向纹理环绕方式
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

		//设置纹理过滤方式
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

		//加载纹理
		int width, height, nrChannels;
		unsigned char* data = stbi_load("resources/container.jpg", &width, &height, &nrChannels,0);
		if (data){
			glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,width,height,0,GL_RGB,GL_UNSIGNED_BYTE,data);
			glGenerateMipmap(GL_TEXTURE_2D);
		}
		else
		{
			std::cout << "Failed to load texture" << std::endl;
		}
		stbi_image_free(data);

		//设置第二张纹理
		glGenTextures(1, &texture2);
		glBindTexture(GL_TEXTURE_2D, texture2);

		//设置横纵向纹理环绕方式
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

		//设置纹理过滤方式
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

		//加载纹理
		stbi_set_flip_vertically_on_load(true); // 通过stb_image.h 把加载的图片按照 y 轴翻转.
		unsigned char* data = stbi_load("resources/awesomeface.png", &width, &height, &nrChannels, 0);
		if (data) {
			glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
			glGenerateMipmap(GL_TEXTURE_2D);
		}
		else
		{
			std::cout << "Failed to load texture" << std::endl;
		}
		stbi_image_free(data);

		shaderProgram.use();
		shaderProgram.setInt("texture1", 0);
		shaderProgram.setInt("texture2", 1);

		// render loop
		// -----------
		while (!glfwWindowShouldClose(window))
		{
			// input
			// -----
			processInput(window);

			// render
			// ------
			glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
			glClear(GL_COLOR_BUFFER_BIT);

			// bind textures on corresponding texture units
			glActiveTexture(GL_TEXTURE0);
			glBindTexture(GL_TEXTURE_2D, texture1);
			glActiveTexture(GL_TEXTURE1);
			glBindTexture(GL_TEXTURE_2D, texture2);

			shaderProgram.use();

			glBindVertexArray(VAO);
			// render the triangle
			glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

			// glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
			// -------------------------------------------------------------------------------
			glfwSwapBuffers(window);
			glfwPollEvents();
		}

		// optional: de-allocate all resources once they've outlived their purpose:
		// ------------------------------------------------------------------------
		glDeleteVertexArrays(1, &VAO);
		glDeleteBuffers(1, &VBO);
		glDeleteBuffers(1, &EBO);
	}
};
#endif