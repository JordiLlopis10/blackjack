# Black Jack V2
#rama nueva
import random
import time

jugadores = [
    {"Jugador": "Humano", "Puntuacion": 0, "Plantado": False},
    {"Jugador": "IA_facil", "Puntuacion": 0, "Plantado": False},
    {"Jugador": "IA_medio", "Puntuacion": 0, "Plantado": False},
    {"Jugador": "IA_dificil", "Puntuacion": 0, "Plantado": False}
]

jugando = True

while jugando:
    todosplantados = True

    for i in jugadores:

        # --- SI YA SE PASÓ, NO JUEGA ---
        if i["Puntuacion"] > 21:
            i["Plantado"] = True
            continue

        if not i["Plantado"]:
            todosplantados = False

            # -------- HUMANO --------
            if i["Jugador"] == "Humano":
                pedir = ""
                print("\n-------------------")
                print("Tienes", i["Puntuacion"], "puntos")

                while pedir != "D" and pedir != "P":
                    pedir = input("Quieres pedir dado (D) o plantarte (P)? ").upper()

                if pedir == "D":
                    dado = random.randint(1, 6)
                    print("Te ha tocado un", dado)
                    i["Puntuacion"] += dado
                else:
                    print("Te has plantado")
                    i["Plantado"] = True

            # -------- IA FÁCIL --------
            elif i["Jugador"] == "IA_facil":
                if i["Puntuacion"] < 17:
                    dado = random.randint(1, 6)
                    i["Puntuacion"] += dado
                    print(i["Jugador"], "tiene", i["Puntuacion"], "puntos")
                else:
                    i["Plantado"] = True
                    print(i["Jugador"], "se planta con", i["Puntuacion"], "puntos")

            # -------- IA MEDIA --------
            elif i["Jugador"] == "IA_medio":
                if i["Puntuacion"] < 17:
                    dado = random.randint(1, 6)
                    i["Puntuacion"] += dado
                    print(i["Jugador"], "tiene", i["Puntuacion"], "puntos")
                elif i["Puntuacion"] in [17, 18, 19]:
                    if random.randint(1, 10) <= 5:
                        dado = random.randint(1, 6)
                        i["Puntuacion"] += dado
                        print(i["Jugador"], "tiene", i["Puntuacion"], "puntos")
                    else:
                        i["Plantado"] = True
                        print(i["Jugador"], "se planta con", i["Puntuacion"], "puntos")
                else:
                    i["Plantado"] = True
                    print(i["Jugador"], "se planta con", i["Puntuacion"], "puntos")

            # -------- IA DIFÍCIL --------
            elif i["Jugador"] == "IA_dificil":
                if i["Puntuacion"] < 17:
                    dado = random.randint(1, 6)
                    i["Puntuacion"] += dado
                    print(i["Jugador"], "tiene", i["Puntuacion"], "puntos")
                elif i["Puntuacion"] in [17, 18, 19]:
                    if jugadores[0]["Puntuacion"] < 17:
                        prob = 7
                    else:
                        prob = 3

                    if random.randint(1, 10) <= prob:
                        dado = random.randint(1, 6)
                        i["Puntuacion"] += dado
                        print(i["Jugador"], "tiene", i["Puntuacion"], "puntos")
                    else:
                        i["Plantado"] = True
                        print(i["Jugador"], "se planta con", i["Puntuacion"], "puntos")
                else:
                    i["Plantado"] = True
                    print(i["Jugador"], "se planta con", i["Puntuacion"], "puntos")

            # -------- COMPROBAR 21 --------
            if i["Puntuacion"] == 21:
                print(i["Jugador"], "ha llegado a 21. ¡Se acaba el juego!")
                jugando = False
                break

            # -------- PASARSE DE 21 --------
            if i["Puntuacion"] > 21:
                print(i["Jugador"], "se ha pasado de 21")
                i["Plantado"] = True

        # --- COMPROBAR SI SOLO QUEDA UNO SIN PASARSE ---
            vivos = [j for j in jugadores if j["Puntuacion"] <= 21]

            if len(vivos) == 1:
                print("\nTodos se han pasado menos uno.")
                print("¡El ganador es", vivos[0]["Jugador"], "con", vivos[0]["Puntuacion"], "puntos!")
                jugando = False
                break

    if todosplantados:
        jugando = False

# -------- RESULTADOS --------
max_puntuacion = 0
ganadores = []
time.sleep(3)
for i in jugadores:
    if i["Puntuacion"] <= 21:
        if i["Puntuacion"] > max_puntuacion:
            max_puntuacion = i["Puntuacion"]
            ganadores = [i]
        elif i["Puntuacion"] == max_puntuacion:
            ganadores.append(i)

print("\n===================")
if not ganadores:
    print("Todos los jugadores se han pasado de 21")
elif len(ganadores) == 1:
    print("Ha ganado el jugador", ganadores[0]["Jugador"],
          "con", ganadores[0]["Puntuacion"], "puntos.")
else:
    print("¡EMPATE!")
    print("Jugadores empatados con", max_puntuacion, "puntos:")
    for g in ganadores:
        print("-", g["Jugador"])

print("\n--- Resultados finales ---")
for i in jugadores:
    print(i["Jugador"], "ha hecho un total de", i["Puntuacion"], "puntos")
