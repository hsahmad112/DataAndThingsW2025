import psycopg2
import numpy as np

conn = psycopg2.connect("dbname=vector_test user=postgres password=postgres")
cur = conn.cursor()

embedding = np.array([1.5, 2.5, 3.5])
cur.execute("INSERT INTO items (embedding) VALUES (%s)", (embedding.tolist(),)) 

query_vector = np.array([2,3,4])
cur.execute("SELECT * FROM items ORDER BY embedding <-> %s LIMIT 1", (query_vector.tolist(),))
result = cur.fetchone()

print(f"Nearest neighbor: {result}")    

conn.commit()
cur.close()
conn.close()
