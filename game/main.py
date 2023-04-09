import random

options = ("piedra", "papel", "tijera")

usuarioGana = 0
maquinaGana = 0
round = 1

while True:
  print("*" * 10)
  print("ROUND ", round)
  print("*" * 10)

  userOption = input("piedra, papel o tijera => ")
  userOption = userOption.lower()
  #choice es algo basado en una tupla
  computerOption = random.choice(options)

  if not userOption in options:
    print("la opcion no es valida")
    continue

  print("Usuario => ", userOption)
  print("Maquina => ", computerOption)

  if userOption == computerOption:
    print("empate")
  elif userOption == "piedra":
    if computerOption == "tijera":
      print("piedra gana a tijera")
      print("usted gana")
      usuarioGana += 1
    else:
      print("papel gana a piedra")
      print("maquina gana")
      maquinaGana += 1

  elif userOption == "papel":
    if computerOption == "piedra":
      print("papel gana a piedra")
      print("usted gana")
      usuarioGana += 1
    else:
      print("tijera gana a papel")
      print("maquina gana")
      maquinaGana += 1

  elif userOption == "tijera":
    if computerOption == "papel":
      print("tijera gana a papel")
      print("usted gana")
      usuarioGana += 1
    else:
      print("piedra gana a tijera")
      print("maquina gana")
      maquinaGana += 1
  round += 1
  if maquinaGana == 2:
    print("PERDISTE")
    break
  if usuarioGana == 2:
    print("GANASTE")
    break
  print(f"   Puntos: Maquina {maquinaGana} Usuario {usuarioGana}")
