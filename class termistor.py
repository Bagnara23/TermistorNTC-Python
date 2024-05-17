#! /usr/bin/env python3
# -- coding: utf-8 --
"""
   Classe para calcular a temperatura em sensores do tipo Termistor-NTC
   Obrigatóriamente deve-se enviar a voltagem em milivolts para conversao.

   Parametros:
   - milivolts = valor recebido na entrada do controlador
   - vcc = Valor da alimentação do sensor em milivolts
   - res_termistor = Resistencia do termistor junto a resistencia do cabo
"""

class TermometroNTC:
   def __init__(self, milivolts, vcc=5000.0, res_termistor=10950):
       self.milivolts = float(milivolts)
       self.vcc = vcc
       self.coeficiente_a = 0.00113
       self.coeficiente_b = 0.000234
       self.coeficiente_c = 0.000000089
       self.resistencia_termistor = res_termistor
       self.temperatura = None

   def calcular_temperatura(self):
       # Metodo para convertar o valor recebido pelo rastreador para celcius.
       from math import log, pow
       # valor recebido da leitura do termistor
       leitura = 5050.5 - self.milivolts
       # x e o valor logico recebido na porta
       x = (leitura * 1023) / self.vcc
       # RNTC
       sensor = x
       sensor *= 5
       sensor /= 1024
       rntc = 50000 / sensor
       rntc = rntc - self.resistencia_termistor
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
       self.temperatura = temp - 273.15
