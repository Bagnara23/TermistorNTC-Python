from math import log, pow

print(" > Tratamento Thermistor NTC 103 - 10K \n")

# Temperatura esperada = 26.6
# Tensao recebida = 2.37
# Valor analogico (0/1023) = 488

# Tensao alimentacao.: 0V a 5VCC
# Convertido de 0 a 1023

# valor recebido da leitura do termistor
value = 2198.0
leitura = 5050.5 - value

Vcc = 5000.0

# x e o valor logico recebido na porta
x = (leitura * 1023) / Vcc

a = 0.00113
b = 0.000234
c = 0.000000089

# RNTC
sensor = x
sensor *= 5
sensor /= 1024
rntc = 50000 / sensor
rntc = rntc - 10950

# b x ln(RNTC)
b1 = log(rntc)
b1 = b1 * b

# c((ln(RNTC))^3)
c1 = log(rntc)
c1 = pow(c1,3)
c1 = c1 * c

# T(C)
temp = a + b1 + c1
temp = 1 / temp
temp = temp - 273.15

print("   > temp: " + str(temp))
