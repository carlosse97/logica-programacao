#!/bin/bash



print ("Olá!", f"Seja bem vindo ao Calculator 3000!\n")

while True:

  op_mat = input(f"Qual operação matemática gostaria de fazer? ")
  print (op_mat,". Entendido!\n ")

  num1 = int(input("Digite o primeiro número: "))

  print (num1)
  num2 = int(input("Digite o segundo número: "))
  print (num2)



  if op_mat.lower() == "soma":
    print ("Resposta:", num1 + num2)
  elif op_mat.lower() == "subtração":
    print ("Resposta:", num1 - num2)
  elif op_mat.lower() == "multiplicação":
    print ("Resposta:", num1 * num2)
  elif op_mat.lower() == "divisão":
    print ("Resposta:", num1 / num2)
  else:
    print ("Operação inválida")
