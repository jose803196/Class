class Rectangulo:
	def __init__(self, base, altura):
		self.altura = altura
		self.base = base

	def area(self):
		return self.base*self.altura

	def perimetro(self):
		return 2*self.altura + 2*self.base


if __name__ == '__main__':
	altura = input("Ingrese altura: ")
	base = input("Ingrese base: ")
	Rectangulo_1 = Rectangulo(float(base), float(altura))
	print(Rectangulo_1.area())
	print(Rectangulo_1.perimetro())