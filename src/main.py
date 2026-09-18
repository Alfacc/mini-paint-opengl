import glfw
from janela import Janela

def main():
    print("Iniciando programa.")

    janela = Janela(1200, 900, "Mini Paint")
    estado = janela.inicializar()
    if estado == 1:
        print("Não foi possível inicializar o GLFW.")
    elif estado == 2:
        print("Erro ao criar janela.")
    else:
         print("Janela criada com sucesso.")

    # LOOP PRINCIPAL
    while janela.esta_aberta():

        janela.atualizar_tela()
        janela.processar_eventos()

    # Finaliza o GLFW
    janela.encerrar()

if __name__ == "__main__":
    main()