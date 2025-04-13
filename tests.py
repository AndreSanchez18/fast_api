DB = [
    {"id":1, "nombre":"Andres"},
    {"id":2, "nombre":"Oscar"},
    {"id":3, "nombre":"Raul"},
    {"id":4, "nombre":"Andres"},
      ]

lista = [u for u in DB if u["nombre"] == "Andres"]



def generador_func(nombre):
    for u in DB:
        if u["nombre"] == nombre:
            yield u

generador = generador_func("Andres")

otro_generador = (u for u in DB if u["nombre"] == "Andres")

print(next(otro_generador))
print(next(otro_generador))
print(next(otro_generador, 1))

