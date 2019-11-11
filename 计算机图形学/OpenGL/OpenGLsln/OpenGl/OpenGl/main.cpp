#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "triangletest.h"

using namespace std;

void framebuffer_size_callback(GLFWwindow* window, int width, int height);
int windowInit();
int mngGlPointer();
void processInput(GLFWwindow *window);

const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HIGHT = 600;

int main()
{
	windowInit();
}

int windowInit() {
	glfwInit();
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	GLFWwindow* window = glfwCreateWindow(800, 600, "LearnOpenGL", NULL, NULL);  //设置GLFW窗口大小
	if (window == NULL)
	{
		std::cout << "GLFW window创建失败" << std::endl;
		glfwTerminate();
		return -1;
	}

	glfwMakeContextCurrent(window);

	mngGlPointer();

	glfwSetFramebufferSizeCallback(window, framebuffer_size_callback); // 注册窗口回调

	//调用
	HelloTriangle triangle;
	triangle.Do(window, processInput);

	//清理释放
	glfwTerminate();

	return 0;
}


// GLAD用来管理所有opengl函数指针，调用gl函数之前都要初始化glad
int mngGlPointer() {
	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
	{
		std::cout << "Failed to initialize GLAD" << std::endl;
		return -1;
	}
	return 0;
}


// 窗口大小更改回调
void framebuffer_size_callback(GLFWwindow* window, int width, int height){
	glViewport(0, 0, width, height);  // 设置gl渲染视口
}

// 接受用户输入
void processInput(GLFWwindow *window) {
	//esc键退出
	if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
		glfwSetWindowShouldClose(window, true);
	}
}

