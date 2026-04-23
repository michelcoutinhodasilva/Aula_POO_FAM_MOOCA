from connect import Connect
from usuario import Usuario
    
    ## 3 main
if __name__ =="__main__":
    db = Connect()

#criar 4 usuarios usando as classes

    lista = [
        Usuario("Marcos","Marcos@email.com"),
        Usuario("Julia","julia@email.com"),
        Usuario("Pedro", "pedro@gmail.com"),
        Usuario("Michel","Michelcoutinho010@gmail.com")
    ]

#inserir no banco de dados
    for p in lista:
        db.inserir(p)

    ##alterar o nome do primeiro usuario
    db.alterar(1,"Marcos editado")

    ## lendo os dados
    print (f"{'ID':<4} | {'NOME':<15} | {'EMAIL'}")
    print ("-" * 40)
    for user in db.listar():
        print(f"{user[0]:<4} | {user[1]:<15} | {user[2]}")
