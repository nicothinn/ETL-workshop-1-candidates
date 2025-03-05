import os
import psycopg2

# Obtener credenciales de variables de entorno, con valores por defecto si no están definidas
dbname   = os.environ.get("DB_NAME")
user     = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host     = os.environ.get("DB_HOST")
port     = os.environ.get("DB_PORT")

# Conectar a la base de datos usando las variables de entorno
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()

# Crear la tabla 'candidates' si no existe
create_table_query = """
CREATE TABLE IF NOT EXISTS public.candidates (
    "First Name" TEXT,
    "Last Name" TEXT,
    "Email" TEXT,
    "Application Date" DATE,
    "Country" TEXT,
    "YOE" INTEGER,
    "Seniority" TEXT,
    "Technology" TEXT,
    "Code Challenge Score" INTEGER,
    "Technical Interview Score" INTEGER
);
"""
cur.execute(create_table_query)
conn.commit()

# Ruta del CSV (se asume que el archivo está correctamente formateado y separado por comas)
csv_file_path = '../data/fixed_candidates.csv'
copy_query = """
COPY public.candidates FROM STDIN WITH CSV HEADER DELIMITER ','
"""
with open(csv_file_path, 'r', encoding='utf-8') as f:
    cur.copy_expert(copy_query, f)

conn.commit()
cur.close()
conn.close()

print("Migración completada.")
