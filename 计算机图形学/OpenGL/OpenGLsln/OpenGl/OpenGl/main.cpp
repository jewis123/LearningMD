#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>
using namespace std;

void framebuffer_size_callback(GLFWwindow* window, int width, int height);
int windowInit();
int mngGlPointer();
int createShaderProgram();
void helloTriangle(GLFWwindow *window, int shaderProgram);
void helloRectangle(GLFWwindow *window, int shaderProgram);
void drawTwoTriangles(GLFWwindow *window, int shaderProgram);
void drawWith2VAO(GLFWwindow *window, int shaderProgram);
void processInput(GLFWwindow *window);

const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HIGHT = 600;

const char *vertexShaderSource = "#version 330 core\n"
"layout (location = 10) in vec3 aPos;\n"
"void main()\n"
"{\n"
"   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
"}\0";
const char *fragmentShaderSource = "#version 330 core\n"
"out vec4 FragColor;\n"
"void main()\n"
"{\n"
"   FragColor = vec4(1.0f, 0.3f, 0.5f, 1.0f);\n"
"}\n\0";


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

	int shaderProgram = createShaderProgram();

	//helloTriangle(window,shaderProgram);
	//helloRectangle(window, shaderProgram);
	//drawTwoTriangles(window, shaderProgram);
	drawWith2VAO(window, shaderProgram);
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

int createShaderProgram() {
	/*******************创建并编译shader程序    START************************/
	//创建顶点着色器
	int vertexShader = glCreateShader(GL_VERTEX_SHADER);
	glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
	glCompileShader(vertexShader);
	//检查是否编译出错
	int success;
	char infoLog[512];
	glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
	if (!success) {
		glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
		std::cout << "顶点着色器编译失败：\n" << infoLog << std::endl;
	}

	//创建片段着色器
	int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
	glCompileShader(fragmentShader);
	//检查是否编译出错
	glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
	if (!success)
	{
		glGetShaderInfoLog(fragmentShader, 512, NULL, infoLog);
		std::cout << "片段着色器编译失败：\n" << infoLog << std::endl;
	}

	//链接着色器
	int shaderProgram = glCreateProgram();
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);
	glLinkProgram(shaderProgram);
	//检查是否编译出错
	glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
	if (!success) {
		glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
		std::cout << "着色器连接失败：" << infoLog << std::endl;
	}
	//完成链接后删除原shader对象
	glDeleteShader(vertexShader);
	glDeleteShader(fragmentShader);
	/*******************创建并编译shader程序     END*******************/
	return shaderProgram;
}

// 你好，VAO,VBO！
void helloTriangle(GLFWwindow *window, int shaderProgram) {

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
		glUseProgram(shaderProgram);
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
void helloRectangle(GLFWwindow *window, int shaderProgram) {
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

	glVertexAttribPointer(10, 3, GL_FLOAT, GL_FALSE, 3*sizeof(float), (void *) 0);
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
		glUseProgram(shaderProgram);
		glBindVertexArray(VAO); 
		glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

		glfwSwapBuffers(window);
		glfwPollEvents();
	}
}

// 课后作业：
//1. 绘制两个相连的三角形
void drawTwoTriangles(GLFWwindow *window, int shaderProgram) {
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
	glVertexAttribPointer(10, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GL_FLOAT), (void* )0);
	glEnableVertexAttribArray(10);

	glBindBuffer(GL_ARRAY_BUFFER, 0);
	glBindVertexArray(0);

	while (!glfwWindowShouldClose(window))
	{
		processInput(window);

		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);  
		glClear(GL_COLOR_BUFFER_BIT);

		
		glUseProgram(shaderProgram);
		glBindVertexArray(VAO);  
		glDrawArrays(GL_TRIANGLES, 0,6);

		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	glDeleteVertexArrays(1, &VAO);
	glDeleteBuffers(1, &VBO);
}

//2. 创建相同的两个三角形，但对它们的数据使用不同的VAO和VBO
void drawWith2VAO(GLFWwindow *window, int shaderProgram) {
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

	//VAO，VBO本质上是数组，不用下面这么麻烦
	//GLuint VAO1, VBO1,VAO2,VBO2;

	GLuint VBOs[2], VAOs[2];
	glGenVertexArrays(2, VAOs);
	glBindVertexArray(VAOs[0]);
	glGenBuffers(2, VBOs);
	glBindBuffer(GL_ARRAY_BUFFER, VBOs[0]);
	glBufferData(GL_ARRAY_BUFFER, sizeof(firstTriangle), firstTriangle, GL_STATIC_DRAW);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);	// Vertex attributes stay the same
	glEnableVertexAttribArray(0);
	// glBindVertexArray(0); // 因为后续还要绑定VAO，所以没必要解绑
	// second triangle setup
	// ---------------------
	glBindVertexArray(VAOs[1]);	// note that we bind to a different VAO now
	glBindBuffer(GL_ARRAY_BUFFER, VBOs[1]);	// and a different VBO
	glBufferData(GL_ARRAY_BUFFER, sizeof(secondTriangle), secondTriangle, GL_STATIC_DRAW);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, (void*)0); // because the vertex data is tightly packed we can also specify 0 as the vertex attribute's stride to let OpenGL figure it out
	glEnableVertexAttribArray(0);
	// glBindVertexArray(0); // not really necessary as well, but beware of calls that could affect VAOs while this one is bound (like binding element buffer objects, or enabling/disabling vertex attributes)

	
	while (!glfwWindowShouldClose(window))
	{
		processInput(window);

		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT);


		glUseProgram(shaderProgram);
		/*glBindVertexArray(tar);
		if (tar == VAO1) {
			tar = VAO2;
		}
		else
		{
			tar = VAO1;
		}*/
		glBindVertexArray(VAOs[0]);
		glDrawArrays(GL_TRIANGLES, 0, 3);
		// then we draw the second triangle using the data from the second VAO
		glBindVertexArray(VAOs[1]);
		glDrawArrays(GL_TRIANGLES, 0, 3);
		glDrawArrays(GL_TRIANGLES, 0, 3);

		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	/*glDeleteVertexArrays(1, &VAO1);
	glDeleteBuffers(1, &VBO1);
	glDeleteVertexArrays(1, &VAO2);
	glDeleteBuffers(1, &VBO2);*/
	glDeleteVertexArrays(2, VAOs);
	glDeleteBuffers(2, VBOs);
}