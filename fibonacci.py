import unittest

def fibonacci(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else: return fibonacci(n-1) + fibonacci(n-2)
        
n = int(input("Ingrese un número mayor que 0:"))

print (fibonacci(n))

class Testfibonacci(unittest.TestCase):

    def test_caso_1(self):
        esperado = 1
        resultado = fibonacci(3)
        self.assertEqual(resultado, esperado)
        
    def test_caso_2(self):
        esperado = 5
        resultado = fibonacci(6)
        self.assertEqual(resultado, esperado)
        
    def test_caso_3(self):
        esperado = 13
        resultado = fibonacci(8)
        self.assertEqual(resultado, esperado)
        
    def test_caso_4(self):
        esperado = 89
        resultado = fibonacci(12)
        self.assertEqual(resultado, esperado)
        
    def test_caso_5(self):
        esperado = 46368
        resultado = fibonacci(25)
        self.assertEqual(resultado, esperado)
        
    def test_caso_5(self):
        esperado = 514229
        resultado = fibonacci(30)
        self.assertEqual(resultado, esperado)
        
    

if __name__ == '__main__':
    unittest.main()