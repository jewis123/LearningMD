#ifndef USEUNIFORMTEST_H
#define USEUNIFORMTEST_H

#include <iostream>
#include <GLFW/glfw3.h>
#include "shader_s.h"
using namespace std;

void helloUniform(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*));

class HelloUniform {
public:
	void Do(GLFWwindow* window, void processInput(GLFWwindow*)) {
		Shader ourshader("shaders/HelloUniform/useuniform.vertex", "shaders/HelloUniform/useuniform.frag");
		helloUniform(window, ourshader, processInput);
	}

	void helloUniform(GLFWwindow *window, Shader shaderProgram, void processInput(GLFWwindow*)){
		float vertices[] = {
			0.5f, -0.5f, 0.0f,  // bottom right
			-0.5f, -0.5f, 0.0f,  // bottom left
			0.0f,  0.5f, 0.0f   // top 
		};

		unsigned int VBO, VAO;
		glGenVertexArrays(1, &VAO);
		glGenBuffers(1, &VBO);
		// bind the Vertex Array Object first, then bind and set vertex buffer(s), and then configure vertex attributes(s).
		glBindVertexArray(VAO);

		glBindBuffer(GL_ARRAY_BUFFER, VBO);
		glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

		glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
		glEnableVertexAttribArray(0);

		// You can unbind the VAO afterwards so other VAO calls won't accidentally modify this VAO, but this rarely happens. Modifying other
		// VAOs requires a call to glBindVertexArray anyways so we generally don't unbind VAOs (nor VBOs) when it's not directly necessary.
		// glBindVertexArray(0);


		// bind the VAO (it was already bound, but just to demonstrate): seeing as we only have a single VAO we can 
		// just bind it beforehand before rendering the respective triangle; this is another approach.
		glBindVertexArray(VAO);


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

			// be sure to activate the shader before any calls to glUniform
			shaderProgram.use();

			// update shader uniform
			float timeValue = glfwGetTime();
			float greenValue = sin(timeValue) / 2.0f + 0.5f;
			int vertexColorLocation = glGetUniformLocation(shaderProgram.ID, "ourColor");
			glUniform4f(vertexColorLocation, 0.0f, greenValue, 0.0f, 1.0f);

			// render the triangle
			glDrawArrays(GL_TRIANGLES, 0, 3);

			// glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
			// -------------------------------------------------------------------------------
			glfwSwapBuffers(window);
			glfwPollEvents();
		}

		// optional: de-allocate all resources once they've outlived their purpose:
		// ------------------------------------------------------------------------
		glDeleteVertexArrays(1, &VAO);
		glDeleteBuffers(1, &VBO);
	}
};
#endif