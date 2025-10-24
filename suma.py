def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b


# ✅ Bloque principal (se ejecutará en GitHub Actions también)
if __name__ == "__main__":
    a = 10
    b = 5
    resultado = sumar(a, b)
    print(f"La suma de {a} + {b} es = {resultado}")

    # Prueba simple automática
    assert resultado == 12, "❌ La suma no es correcta"
    print("✅ Prueba pasada correctamente")
