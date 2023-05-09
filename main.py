# Creado el 09 de Mayo de 2023 por José Luis Santos Mendoza
# Actividad 7: productor - consumidor 1
# Universidad de Guadalajara, Seminario de Solución de Problemas de Sistemas Operativos
# Profesor Javier Rosales Martínez, Sección D06

import random
import time

parking = [""] * 12
inFreq = 1
outFreq = 1


def addVehicle():
    global parking
    global inFreq
    if "" not in parking:
        print("Parking is full, can't add another car.")
        return
    # Creating the ID
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456"
    id = ""
    for i in range(4):
        id += random.choice(letters)
    for i in range(3):
        id += str(random.randint(0, 9))
    emptyPosition = parking.index("")
    parking[emptyPosition] = id
    print(f"Car with id {id} is in the parking")
    print("Current status of the parking lot: ", parking)
    time.sleep(inFreq)


def outVehicle():
    global parking
    global inFreq
    # Make sure that the parking is empty
    if "" in parking:
        print("Parking is empty, can't free a spot.")
        return
    # Finding a spot in the parking
    fullPos = random.randint(0, 11)
    while parking[fullPos] == "":
        fullPos = random.randint(0, 11)
    id = parking[fullPos]
    parking[fullPos] = ""
    print(f"Car with id {id} is out the parking")
    print("Current status of the parking lot: ", parking)
    time.sleep(outFreq)


while True:
    inUser = input(
        "Put 'exit' to finish or press Enter to continue: ")
    if inUser == "exit":
        break
    addVehicle()
    outVehicle()
    newFreq = input("Put a new frequency (actual frequency is: " + str(
        inFreq) + " seconds), or press Enter to continue: ")
    if newFreq:
        inFreq = float(newFreq)
