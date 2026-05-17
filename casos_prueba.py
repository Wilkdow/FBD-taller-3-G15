import mongo_api

BASE_URL = "https://fbd-taller-3-g15.onrender.com"

def test_post_comentario(bar_id: int):
    print(f"\n--- POST comentario para bar {bar_id} ---")
    url = f"{BASE_URL}/bares/{bar_id}/comentarios"
    datos = {
        "texto": "Excelente bar, muy buen ambiente!",
        "autor": "Juan Perez"
    }
    response = mongo_api.post(url, json=datos)
    print(f"Status: {response.status_code}")
    print(f"Respuesta: {response.json()}")

def test_get_comentarios(bar_id: int):
    print(f"\n--- GET comentarios del bar {bar_id} ---")
    url = f"{BASE_URL}/bares/{bar_id}/comentarios"
    response = mongo_api.get(url)
    print(f"Status: {response.status_code}")
    comentarios = response.json()
    print(f"Total comentarios: {len(comentarios)}")
    for c in comentarios:
        print(f"  - {c['autor']}: {c['texto']}")

def test_post_evento_concierto(bar_id: int):
    print(f"\n--- POST evento concierto para bar {bar_id} ---")
    url = f"{BASE_URL}/bares/{bar_id}/eventos"
    datos = {
        "nombre": "Noche de Jazz",
        "artista": "Trio Bogota",
        "cover": 15000,
        "cupos": 80
    }
    response = mongo_api.post(url, json=datos)
    print(f"Status: {response.status_code}")
    print(f"Respuesta: {response.json()}")

def test_post_evento_happyhour(bar_id: int):
    print(f"\n--- POST evento happy hour para bar {bar_id} ---")
    url = f"{BASE_URL}/bares/{bar_id}/eventos"
    datos = {
        "nombre": "Happy Hour Martes",
        "descuento": "2x1 en cervezas",
        "hora_inicio": "17:00",
        "hora_fin": "19:00"
    }
    response = mongo_api.post(url, json=datos)
    print(f"Status: {response.status_code}")
    print(f"Respuesta: {response.json()}")

def test_get_eventos(bar_id: int):
    print(f"\n--- GET eventos del bar {bar_id} ---")
    url = f"{BASE_URL}/bares/{bar_id}/eventos"
    response = mongo_api.get(url)
    print(f"Status: {response.status_code}")
    eventos = response.json()
    print(f"Total eventos: {len(eventos)}")
    for e in eventos:
        print(f"  - {e['nombre']}: {e}")

def test_inicio():
    print("\n--- GET / ---")
    response = mongo_api.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Respuesta: {response.json()}")




if __name__ == "__main__":
    BAR_ID = 1

    test_inicio()

    test_post_comentario(BAR_ID)
    test_get_comentarios(BAR_ID)

    test_post_evento_concierto(BAR_ID)
    test_post_evento_happyhour(BAR_ID)
    test_get_eventos(BAR_ID)

    print("\nTodo funciona")