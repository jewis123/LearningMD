#ifndef SHADER_H
#define SHADER_H

#include <glad/glad.h>
#include <glm\glm.hpp>
#include <glm\gtc\type_ptr.hpp>

#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
using namespace std;

/*
作用： 
读取本地shader文件中的源代码
链接shader程序

提供一些工具函数
*/
class Shader
{
public:
	unsigned int ID;
	// 构造函数
	Shader(const char* vertexPath, const char* fragmentPath)
	{
		// 1. 从文件路径读取vertexshader和fragmentshader源代码
		string vertexCode;
		string fragmentCode;
		ifstream vShaderFile;
		ifstream fShaderFile;
		// 保证ifstream对象可以输出异常:
		vShaderFile.exceptions(ifstream::failbit | ifstream::badbit);
		fShaderFile.exceptions(ifstream::failbit | ifstream::badbit);
		try
		{
			// 打开文件
			vShaderFile.open(vertexPath);
			fShaderFile.open(fragmentPath);
			stringstream vShaderStream, fShaderStream;
			//读取文件的缓冲内容到数据流中
			vShaderStream << vShaderFile.rdbuf();
			fShaderStream << fShaderFile.rdbuf();
			//关闭文件
			vShaderFile.close();
			fShaderFile.close();
			//将数据流转换成string
			vertexCode = vShaderStream.str();
			fragmentCode = fShaderStream.str();
		}
		catch (ifstream::failure e)
		{
			cout << "ERROR::Shader:文件读取失败" << endl;
		}
		const char* vShaderCode = vertexCode.c_str();
		const char * fShaderCode = fragmentCode.c_str();
		// 2. 编译shader
		unsigned int vertex, fragment;
		// vertex shader
		vertex = glCreateShader(GL_VERTEX_SHADER);
		glShaderSource(vertex, 1, &vShaderCode, NULL);
		glCompileShader(vertex);
		checkCompileErrors(vertex, "VERTEX");
		// fragment Shader
		fragment = glCreateShader(GL_FRAGMENT_SHADER);
		glShaderSource(fragment, 1, &fShaderCode, NULL);
		glCompileShader(fragment);
		checkCompileErrors(fragment, "FRAGMENT");
		// shader Program
		ID = glCreateProgram();
		glAttachShader(ID, vertex);
		glAttachShader(ID, fragment);
		glLinkProgram(ID);
		checkCompileErrors(ID, "PROGRAM");
		//链接shader后删除无用的shader对象
		glDeleteShader(vertex);
		glDeleteShader(fragment);
	}
	//使用shader
	void use()
	{
		glUseProgram(ID);
	}
	// uniform工具函数
	void setBool(const string &name, bool value) const
	{
		glUniform1i(glGetUniformLocation(ID, name.c_str()), (int)value);
	}
	void setInt(const string &name, int value) const
	{
		glUniform1i(glGetUniformLocation(ID, name.c_str()), value);
	}
	void setFloat(const string &name, float value) const
	{
		glUniform1f(glGetUniformLocation(ID, name.c_str()), value);
	}
	void setMatrix(const string &name, const glm::mat4& transform) const {
		unsigned int transformLoc = glGetUniformLocation(ID, name.c_str());
		glUniformMatrix4fv(transformLoc, 1, GL_FALSE, glm::value_ptr(transform));
	}

private:
	// 检查shader 编译、链接异常的工具函数.
	void checkCompileErrors(unsigned int shader, string type)
	{
		int success;
		char infoLog[1024];
		if (type != "PROGRAM")
		{
			glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
			if (!success)
			{
				glGetShaderInfoLog(shader, 1024, NULL, infoLog);
				cout << "ERROR::shader编译异常 of type: " << type << "\n" << infoLog << "\n -- --------------------------------------------------- -- " << endl;
			}
		}
		else
		{
			glGetProgramiv(shader, GL_LINK_STATUS, &success);
			if (!success)
			{
				glGetProgramInfoLog(shader, 1024, NULL, infoLog);
				cout << "ERROR::shader链接异常 of type: " << type << "\n" << infoLog << "\n -- --------------------------------------------------- -- " << endl;
			}
		}
	}
};
#endif