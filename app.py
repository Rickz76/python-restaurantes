from modelos.restaurante import Restaurante #Pegando o que foi definido em outros arquivos

# Restaurantes
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_churrascaria = Restaurante('Churrascaria', 'carne')

# Avaliações
restaurante_praca.receber_avaliacao('Paulo', 2)
restaurante_praca.receber_avaliacao('Lais', 5)
restaurante_praca.receber_avaliacao('Samara', 4)

restaurante_mexicano.receber_avaliacao('Maria', 5)
restaurante_mexicano.receber_avaliacao('Natalia', 4)
restaurante_mexicano.receber_avaliacao('Marcos', 5)

restaurante_japones.receber_avaliacao('Luisa', 5)
restaurante_japones.receber_avaliacao('Ryan', 2)
restaurante_japones.receber_avaliacao('Moraes', 1)

 # Status
restaurante_mexicano.alternar_estado()
restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__': # Sempre que foi o script principal se escreceve isso
    main()
