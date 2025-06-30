class triangulos:
    def __init__(self, lado1, lado2, lado3):
        self.lado1= lado1
        self.lado2= lado2
        self.lado3= lado3
    
    def tipo_triangulo(self):
       if self.lado1 == self.lado2 and self.lado2 == self.lado3:
           return print("El triangulo es equilatero")
       elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
           return print("El triangulo es escaleno")
       else:
           return print("El triangulo es isoceles")
       
    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            return print(f"El lado 1 es el mayor con {self.lado1}cm.")
        elif self.lado2 > self.lado3 and self.lado2 > self.lado1:
            return print(f"El lado 2 es el mayor con {self.lado2}cm.")
        else:
             return print(f"El lado 3 es el mayor con {self.lado3}cm.")

        
print("Ingrese las medidas de cada lado del triangulo")       
lado1= int(input("medidas: "))
lado2= int(input("medidas: "))
lado3= int(input("medidas: "))

triangulo1 = triangulos(lado1,lado2,lado3)

triangulo1.tipo_triangulo()
triangulo1.lado_mayor()