#version 330 core

in vec3 ourColor;
in vec2 TexCoord;
uniform sampler2D texture1;
uniform sampler2D texture2;

out vec4 FragColor;

void main()
{
    //FragColor = texture(texture1, TexCoord) * vec4(ourColor,1.0f);
	//(80% texture1, 20% texture2)
	FragColor = mix(texture(texture1, TexCoord), texture(texture2, TexCoord), 0.2) 