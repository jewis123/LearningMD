#version 330 core
out vec4 FragColor;

in vec3 Normal;  
in vec3 FragPos;  
  
uniform vec3 lightPos; 
uniform vec3 lightColor;
uniform vec3 objectColor;

void main()
{
    // 环境光
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;  //计算环境光
  	
    // 漫反射 
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);   //法向量和光源方向夹角肯定小于90度，也就是说这条语句计算范围是[0，1]
    vec3 diffuse = diff * lightColor;  //计算反射光
            
    vec3 result = (ambient + diffuse) * objectColor;  //计算结合光
    FragColor = vec4(result, 1.0);
} 