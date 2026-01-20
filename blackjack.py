# Black jack v3 
import csv
import random

dataset = []
columnas = ["ID_Partida", "Tipo_IA", "Puntuacion_Final", "Resultado", "Cartas", "Plantado"]

partidas = 0

while True:
    try:
        menu = int(input("""
1. Generar dataset muy pequeño (1 partida)
2. Generar dataset pequeño (10 partidas)
3. Generar dataset mediano (100 partidas)
4. Generar dataset grande (1000 partidas)
5. Generar dataset muy grande (10000 partidas)
-> """))
        if menu == 1 : partidas = 1
        elif menu == 2 : partidas = 10
        elif menu == 3 : partidas = 100
        elif menu == 4 : partidas = 1000
        elif menu == 5 : partidas = 10000
        else: continue
        break
    except ValueError:
        continue

print(f"Generando dataset de {partidas} partidas...")

for id_partida in range(1, partidas + 1): 
    jugadores = [
        {"Jugador": "IA_facil", "Puntuacion": 0, "Plantado": False, "Cartas": 0, "Resultado": "Derrota"},
        {"Jugador": "IA_medio", "Puntuacion": 0, "Plantado": False, "Cartas": 0, "Resultado": "Derrota"},
        {"Jugador": "IA_dificil", "Puntuacion": 0, "Plantado": False, "Cartas": 0, "Resultado": "Derrota"}
    ]

    jugando = True
    while jugando:
        todos_plantados = True
        
        puntuaciones_validas = []
        for p in jugadores:
            if p["Puntuacion"] <= 21:
                puntuaciones_validas.append(p["Puntuacion"])

        max_rival = max(puntuaciones_validas) if puntuaciones_validas else 0

        for i in jugadores:
            if i["Puntuacion"] > 21 or i["Plantado"]:
                continue

            todos_plantados = False
            pedir_carta = False

            if i["Jugador"] == "IA_facil":
                if i["Puntuacion"] < 17: pedir_carta = True 
                
            elif i["Jugador"] == "IA_medio":
                if i["Puntuacion"] < 17: pedir_carta = True
                elif i["Puntuacion"] in [17, 18, 19]:
                    if random.random() < 0.5: pedir_carta = True 
            
            elif i["Jugador"] == "IA_dificil":
                if i["Puntuacion"] < 17: pedir_carta = True
                elif i["Puntuacion"] in [17, 18, 19]:
                    if max_rival < 17:
                        if random.random() < 0.7: pedir_carta = True 
                    else:
                        if random.random() < 0.3: pedir_carta = True 

            if pedir_carta:
                i["Puntuacion"] += random.randint(1, 6)
                i["Cartas"] += 1 
                
                if partidas == 1: 
                    print(f"{i['Jugador']} pide y tiene {i['Puntuacion']}")
                
                if i["Puntuacion"] > 21:
                    i["Plantado"] = True
            else:
                i["Plantado"] = True
            
        # Si todos están plantados, termina la partida
        if todos_plantados:
            jugando = False

    # --- FINAL DE PARTIDA ---
    
    vivos = []
    for j in jugadores:
        if j["Puntuacion"] <= 21:
            vivos.append(j)

    if vivos:

        lista_puntos_vivos = []
        for j in vivos:
            lista_puntos_vivos.append(j["Puntuacion"])
        max_puntos = max(lista_puntos_vivos)

 
        ganadores = []
        for j in vivos:
            if j["Puntuacion"] == max_puntos:
                ganadores.append(j)

        estado_ganador = "Victoria" if len(ganadores) == 1 else "Empate"
        for g in ganadores:
            g["Resultado"] = estado_ganador

    for i in jugadores:
        dataset.append({
            "ID_Partida": id_partida,
            "Tipo_IA": i["Jugador"],
            "Puntuacion_Final": i["Puntuacion"],
            "Resultado": i["Resultado"],
            "Cartas": i["Cartas"],
            "Plantado": "Si" if i["Plantado"] else "No"
        })

# --- CSV ---
nombre_archivo = "dataset_blackjack.csv"
try:
    with open(nombre_archivo, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(dataset)
    print(f"\n¡Éxito! Archivo '{nombre_archivo}' creado con {len(dataset)} filas.")
except Exception as e:
    print(f"Error escribiendo el archivo: {e}")