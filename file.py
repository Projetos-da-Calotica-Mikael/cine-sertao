import os

def generate_file(filename, content):
    if os.path.exists(filename):
        print("Alerta: O arquivo", filename, "já existe e será sobreescrito!")
    try:
        with open(filename, "w") as file:
            file.write(content)
        print("Arquivo", filename, "criado com sucesso!")
    except IOError:
        print("Erro: Não foi possível criar o arquivo.")
    except Exception as e:
        print("Erro inesperado:", e)
