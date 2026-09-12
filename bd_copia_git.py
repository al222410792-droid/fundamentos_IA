from pymongo import MongoClient

try:
   
    MONGO_URI = "mongodb://localhost:27017/"
    
   
    client = MongoClient(MONGO_URI)
    
    db = client["bigdata_ventas_db"]
    coleccion = db["registros"]
    
    documento_ejemplo = {
        "programa": "PySpark + MongoDB",
        "estado": "Conexión Exitosa",
        "mensaje": "Hola profesor, la práctica funciona perfectamente",
        "version_python": "3.10+",
        "nombre_estudiante": "Edith",
        "apellido_estudiante": "González",
    }
    
    resultado = coleccion.insert_one(documento_ejemplo)
    print(f"\n ¡Conectado con éxito a MongoDB Compass!")
    print(f" Documento insertado correctamente con el ID: {resultado.inserted_id}")
    
    busqueda = coleccion.find_one({"nombre_estudiante": "Edith"})
    print("\n Datos recuperados de la Base de Datos:")
    print(busqueda)

except Exception as e:
    print(f"\n Error de conexión: No se pudo establecer comunicación con MongoDB.")
    print(f"Detalle del error: {e}")
