from random import randint # para gerar os nums aleatorios

vec1 = []
vec2 = []
vec3 = []

for i in range(0,50):
    vec1.append(randint(0, 100))
    vec2.append(randint(0, 100))
vec1.sort()
vec2.sort()

vec3.extend(vec1)
vec3.extend(vec2)
vec3.sort()

print(vec3)