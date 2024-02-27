## Passos para Executar o Container

1. Inicialize o container utilizando o comando:
    ```
    docker-compose up -d
    ```

2. Execute o comando `docker ps` para obter o ID do container.

3. Em seguida, utilize o seguinte comando para copiar o arquivo:
    ```
    docker cp <caminho_do_arquivo_local> <id_do_container>:<caminho_no_container>
    ```

4. Acesse o shell do container usando o comando:
    ```
    docker exec -it <id_do_container> bash
    ```

5. Execute o script SQL dentro do container usando o comando `psql`:
    ```
    psql -h localhost -p 5432 -U user -d db -W -f create_table.sql
    ```

6. Para acessar o banco de dados, utilize o comando:
    ```
    psql -U user -d db
    ```

7. Por fim, você pode executar consultas SQL, como por exemplo:
    ```
    select * from users;
    ```

Certifique-se de substituir `<caminho_do_arquivo_local>` pelo caminho do arquivo no seu sistema local e `<id_do_container>` pelo ID do container gerado no passo 2. Os outros parâmetros como `user`, `db`, e `create_table.sql` devem ser substituídos pelos valores correspondentes do seu ambiente.
