import psycopg2
from bcrypt import gensalt, hashpw, checkpw

conn = psycopg2.connect(
    dbname="db",
    user="user",
    password="password",
    host="localhost",
)
cursor = conn.cursor()


def create_hash_password(password):
    salt = gensalt(rounds=10)
    bpassword = password.encode('utf-8')    # Convert the password to bytes
    hashed_password = hashpw(bpassword, salt)   # Hash the password
    hashed_password = hashed_password.decode('utf-8')  # Convert the hashed password to string
    return hashed_password


def store_password(username, email, password):
    hashed_password = create_hash_password(password)
    sql = """
    INSERT INTO users 
    (username, email, password) 
    VALUES (%s, %s, %s)
    RETURNING id
    """
    cursor.execute(sql, (username, email, hashed_password))
    conn.commit()
    user_id = cursor.fetchone()[0]
    print(f"User {username} has been created with id {user_id}")
    return user_id


def verify_password_username(username, password):
    sql = """
    SELECT password FROM users 
    WHERE username = %s
    """
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    
    #Guard clause
    if result is None:
        print("Username does not exist")
        return False
    
    stored_password = result[0].encode('utf-8')
    bpassword = password.encode('utf-8')
    #Guard clause 2
    if not checkpw(bpassword, stored_password):
        print("Password is incorrect")
        return False
    print("Password is correct")
    return True


if __name__ == "__main__":
    username = "test1"
    email = "teste1@gmail.com"
    password = "teste@123"
    # store_password(username, email, password)
    verify_password_username(username, "senha_errada")
    verify_password_username(username, password)
    
    cursor.close()
    conn.close()

\





