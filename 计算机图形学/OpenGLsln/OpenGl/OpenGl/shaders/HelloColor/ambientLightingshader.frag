#version 330 core
out vec4 FragColor;

uniform vec3 objectColor;
uniform vec3 lightColor;

void main()
{
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;  //将光线弱化

    vec3 result = ambient * objectColor;   //应用到物体反射
    FragColor = vec4(result, 1.0);
}