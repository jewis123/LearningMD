#ifndef TRIANGLETEST_H
#define TRIANGLETEST_H

#include <iostream>
#include <GLFW/glfw3.h>
#include "shader_s.h"
using namespace std;

void helloTriangle(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*));
void helloRectangle(GLFWwindow* window, Shader shaderProgram, void processInput(GLFWwindow*));
void drawTwoTriangles(GLFWwindow* window, Shader shaderProgram, void processInput(GLFWwindow*));
void drawWith2VAO(GLFWwindow* window, Shader shaderProgram, void processInput(GLFWwindow*));
void drawWith2VBO(GLFWwindow* window, Shader shaderProgram, void processInput(GLFWwindow*));

class HelloTriangle {
public:
	void Do(GLFWwindow* window, void processInput(GLFWwindow*)) {
		Shader ourshader("shaders/HelloTriangle/hellotriangle.vertex", "shaders/HelloTriangle/hellotriangle.frag");
		helloTriangle(window, ourshader, processInput);
		//helloRectangle(window, ourshader, processInput);
		//drawTwoTriangles(window, ourshader, processInput);
		//drawWith2VAO(window, ourshader, processInput);

		//Shader ourshader ("shaders/HelloTriangle/doublevertexpointer.vertex", "shaders/HelloTriangle/doublevertexpointer.frag");
		//drawWith2VBO(window, ourshader, processInput);
	}

	// 你好，VAO,VBO！
	void helloTriangle(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*)) {

		/*******************设置顶点数据     START*******************/
		//初始顶点数据
		float vertices[] = {
			-0.5f, -0.5f, 0.0f, // left  
			0.5f, -0.5f, 0.0f, // right 
			0.0f,  0.5f, 0.0f  // top   
		};

		//首先绑定顶点数组对象，然后绑定并设置顶点缓冲区，然后配置顶点属性。
		GLuint VBO, VAO;
		glGenVertexArrays(1, &VAO);
		//绑定VAO
		glBindVertexArray(VAO);

		glGenBuffers(1, &VBO);
		glBindBuffer(GL_ARRAY_BUFFER, VBO);
		glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

		// 设置顶点属性指针
		glVertexAttribPointer(10, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
		glEnableVertexAttribArray(10);
		//请注意，这是允许的，
		//对 glVertexAttribPointer 的调用将 VBO 注册为顶点属性的绑定顶点缓冲区对象，
		//因此之后我们可以安全地取消绑定
		glBindBuffer(GL_ARRAY_BUFFER, 0);
		//之后可以取消绑定 VAO，以便其他 VAO 调用不会意外修改此 VAO，但这种情况很少发生。
		//修改其他VAO 需要调用 glBindVertexArray，因此，在非直接需要时，我们通常不会取消绑定 VAO。
		glBindVertexArray(0);
		/*******************设置顶点数据     END*******************/

		//glPolygonMode(GL_FRONT_AND_BACK, GL_LINE); //配置线框渲染模式

		// 循环渲染
		while (!glfwWindowShouldClose(window))
		{
			processInput(window);

			glClearColor(0.2f, 0.3f, 0.3f, 1.0f);  //使用给定颜色重置颜色缓冲区
			glClear(GL_COLOR_BUFFER_BIT);

			//绘制三角形
			shaderProgram.use();
			glBindVertexArray(VAO);  //虽然只有只一个VAO看似没必要每次循环都绑定一下，但是为了规范

									 //glDrawArrays(GL_LINES, 0, 2);    // 绘制线
									 //glDrawArrays(GL_LINE_LOOP, 0, 3);  //绘制首尾相连的线
			glDrawArrays(GL_TRIANGLES, 0, 3);

			// glBindVertexArray(0);     //没必要每次都解绑

			glfwSwapBuffers(window);
			glfwPollEvents();
		}

		glDeleteVertexArrays(1, &VAO);
		glDeleteBuffers(1, &VBO);
	}

	//你好，EBO！
	void helloRectangle(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*)) {
		float vertices[] = {
			0.5f,  0.5f, 0.0f,  // top right
			0.5f, -0.5f, 0.0f,  // bottom right
			-0.5f, -0.5f, 0.0f,  // bottom left
			-0.5f,  0.5f, 0.0f   // top left 
		};
		GLuint indices[] = {  // note that we start from 0!
			0, 1, 3,  // first Triangle
			1, 2, 3   // second Triangle
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

		glVertexAttribPointer(10, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void *)0);
		glEnableVertexAttribArray(10);

		//重置缓冲区
		glBindBuffer(GL_ARRAY_BUFFER, 0);
		glBindVertexArray(0);

		while (!glfwWindowShouldClose(window))
		{
			processInput(window);

			glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
			glClear(GL_COLOR_BUFFER_BIT);

			// draw our first triangle
			shaderProgram.use();
			glBindVertexArray(VAO);
			glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

			glfwSwapBuffers(window);
			glfwPollEvents();
		}
	}

	// 课后作业：
	//1. 绘制两个相连的三角形
	void drawTwoTriangles(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*)) {
		float vertices[] = {
			// first triangle
			-0.9f, -0.5f, 0.0f,  // left 
			-0.0f, -0.5f, 0.0f,  // right
			-0.45f, 0.5f, 0.0f,  // top 
			 // second triangle
			 0.0f, -0.5f, 0.0f,  // left
			 0.9f, -0.5f, 0.0f,  // right
			 0.45f, 0.5f, 0.0f   // top 
		};

		GLuint VAO, VBO;
		glGenVertexArrays(1, &VAO);
		glBindVertexArray(VAO);

		glGenBuffers(1, &VBO);
		glBindBuffer(GL_ARRAY_BUFFER, VBO);
		glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

		//踩坑点：第二个参数的含义是顶点的维数
		glVertexAttribPointer(10, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GL_FLOAT), (void*)0);
		glEnableVertexAttribArray(10);

		glBindBuffer(GL_ARRAY_BUFFER, 0);
		glBindVertexArray(0);

		while (!glfwWindowShouldClose(window))
		{
			processInput(window);

			glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
			glClear(GL_COLOR_BUFFER_BIT);


			shaderProgram.use();
			glBindVertexArray(VAO);
			glDrawArrays(GL_TRIANGLES, 0, 6);

			glfwSwapBuffers(window);
			glfwPollEvents();
		}

		glDeleteVertexArrays(1, &VAO);
		glDeleteBuffers(1, &VBO);
	}

	//2. 创建相同的两个三角形，但对它们的数据使用不同的VAO和VBO
	void drawWith2VAO(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*)) {
		float firstTriangle[] = {
			-0.9f, -0.5f, 0.0f,  // left 
			-0.0f, -0.5f, 0.0f,  // right
			-0.45f, 0.5f, 0.0f,  // top 
		};
		float secondTriangle[] = {
			0.0f, -0.5f, 0.0f,  // left
			0.9f, -0.5f, 0.0f,  // right
			0.45f, 0.5f, 0.0f   // top 
		};
		unsigned int VBOs[2], VAOs[2];
		glGenVertexArrays(2, VAOs); // we can also generate multiple VAOs or buffers at the same time
		glGenBuffers(2, VBOs);
		// first triangle setup
		// --------------------
		glBindVertexArray(VAOs[0]);
		glBindBuffer(GL_ARRAY_BUFFER, VBOs[0]);
		glBufferData(GL_ARRAY_BUFFER, sizeof(firstTriangle), firstTriangle, GL_STATIC_DRAW);
		glVertexAttribPointer(10, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);	// Vertex attributes stay the same
		glEnableVertexAttribArray(10);
		// glBindVertexArray(0); // no need to unbind at all as we directly bind a different VAO the next few lines
		// second triangle setup
		// ---------------------
		glBindVertexArray(VAOs[1]);	// note that we bind to a different VAO now
		glBindBuffer(GL_ARRAY_BUFFER, VBOs[1]);	// and a different VBO
		glBufferData(GL_ARRAY_BUFFER, sizeof(secondTriangle), secondTriangle, GL_STATIC_DRAW);
		glVertexAttribPointer(10, 3, GL_FLOAT, GL_FALSE, 0, (void*)0); // because the vertex data is tightly packed we can also specify 0 as the vertex attribute's stride to let OpenGL figure it out
		glEnableVertexAttribArray(10);
		// glBindVertexArray(0); // not really necessary as well, but beware of calls that could affect VAOs while this one is bound (like binding element buffer objects, or enabling/disabling vertex attributes)


		// uncomment this call to draw in wireframe polygons.
		//glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);

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

			shaderProgram.use();
			// draw first triangle using the data from the first VAO
			glBindVertexArray(VAOs[0]);
			glDrawArrays(GL_TRIANGLES, 0, 3);
			// then we draw the second triangle using the data from the second VAO
			glBindVertexArray(VAOs[1]);
			glDrawArrays(GL_TRIANGLES, 0, 3);

			// glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
			// -------------------------------------------------------------------------------
			glfwSwapBuffers(window);
			glfwPollEvents();
		}

		// optional: de-allocate all resources once they've outlived their purpose:
		// ------------------------------------------------------------------------
		glDeleteVertexArrays(2, VAOs);
		glDeleteBuffers(2, VBOs);
	}

	//3.使用不同VBO修饰同一个物体
	void drawWith2VBO(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*)) {
		float triangle[] = {
			0.0f, 0.5f, 0.0f,
			0.5f, -0.5f, 0.0f,
			-0.5f, -0.5f, 0.0f,
		};
		float color[] = {
			1.0f, 0.0f, 0.0f,
			0.0f, 1.0f, 0.0f,
			0.0f, 0.0f, 1.0f,
		};
		GLuint VBOs[2], VAO;
		glGenVertexArrays(1, &VAO);
		glBindVertexArray(VAO);
		glGenBuffers(2, VBOs);

		//绑定顶点
		glBindBuffer(GL_ARRAY_BUFFER, VBOs[0]);
		glBufferData(GL_ARRAY_BUFFER, sizeof(triangle), triangle, GL_STATIC_DRAW);
		glVertexAttribPointer(10, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
		glEnableVertexAttribArray(10);

		//绑定颜色
		glBindBuffer(GL_ARRAY_BUFFER, VBOs[1]);
		glBufferData(GL_ARRAY_BUFFER, sizeof(triangle), triangle, GL_STATIC_DRAW);
		glVertexAttribPointer(11, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
		glEnableVertexAttribArray(11);

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

			shaderProgram.use();
			// draw first triangle using the data from the first VAO
			glBindVertexArray(VAO);
			glDrawArrays(GL_TRIANGLES, 0, 3);

			// glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
			// -------------------------------------------------------------------------------
			glfwSwapBuffers(window);
			glfwPollEvents();
		}

		// optional: de-allocate all resources once they've outlived their purpose:
		// ------------------------------------------------------------------------
		glDeleteVertexArrays(1, &VAO);
		glDeleteBuffers(2, VBOs);
	}
};

#endif