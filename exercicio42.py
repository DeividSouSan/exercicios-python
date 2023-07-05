"""
Refaça o exercício 35 acrescentando o recurso de mostrar que tipo de triângulo será formado.
- Equilátero: todos os lados iguais;
- Isóceles: dois lados iguais;
- Escaleno: todos os lados diferentes.
"""
from cprint import *

    


segUm = float(input("Primeiro segmento: "))
segDois = float(input("Segundo segmento: "))
segTres = float(input("Terceito segmento: "))

FORMA_TRIANGULO = segUm < (segDois + segTres) and segDois < (segUm + segTres) and segTres < (segUm + segDois)

EQUILATERO = segUm == segDois == segTres
ISOCELES = segUm == segDois or segUm == segTres or segDois == segTres
ESCALENO = segUm != segDois and segUm != segTres  and segDois != segTres

if EQUILATERO:
    tipo = "EQUILÁTERO"
elif ISOCELES:
    tipo = "ISÓCELES"
elif ESCALENO:
    tipo = "ESCALENO"


if FORMA_TRIANGULO:
    cprint("Os segumentos acima !PODEM FORMAR! um triângulo.", ITALIC, C_GREEN)
    cprint(f"O tipo de triângulo formado será !{tipo}!.", BOLD, BG_CYAN)
else:
    cprint("Os segumentos acima !NÃO PODEM FORMAR! um triângulo.", ITALIC, C_RED)