import json
import psycopg2
import os

def lambda_handler(event, context):
    try:
        connection = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD']
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT product_id, product_name, price FROM products")
        rows = cursor.fetchall()
        
        products = [{"id": row[0], "name": row[1], "price": float(row[2])} for row in rows]
        
        return {
            'statusCode': 200,
            'body': json.dumps(products)
        }
    
    except psycopg2.DatabaseError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
