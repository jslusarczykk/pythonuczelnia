import numpy as np
import matplotlib.pyplot as plt

# Funkcja wykładnicza
a = 2
x_exp = np.linspace(-2, 2, 100)
y_exp = a**x_exp

# Funkcja odwrotna - logarytmiczna
x_log = np.linspace(0.01, 4, 100)  # unikamy logarytmu z zera
y_log = np.log(x_log) / np.log(a)

# Rysowanie wykresów
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_exp, y_exp, label=f'$f(x)={a}^x$')
plt.title('Funkcja wykładnicza')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_log, y_log, label=f'$f^{-1}(x)=\log_{a}(x)$')
plt.title('Funkcja odwrotna - logarytmiczna')
plt.xlabel('x')
plt.ylabel('$f^{-1}(x)$')
plt.legend()

plt.tight_layout()
plt.show()