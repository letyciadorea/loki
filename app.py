# ================================================
# PROGRAMA: CÁLCULO DO ÍNDICE DE MASSA CORPORAL (IMC)
# ================================================

# Importamos a função round (não é obrigatório, mas deixamos para clareza)
# Na verdade, round é uma função nativa do Python, por isso não precisamos importar nada


def calcular_imc(peso, altura):           # Criamos uma função chamada calcular_imc que recebe dois parâmetros
    """
    Função responsável por calcular o IMC.
    Recebe peso em kg e altura em metros.
    """
    # Verificação de segurança: altura não pode ser zero ou negativa
    if altura <= 0:                       # Se a altura for menor ou igual a zero
        raise ValueError("A altura deve ser maior que zero!")  # Levanta um erro
    
    # Cálculo real do IMC
    imc = peso / (altura ** 2)            # Fórmula: peso dividido pela altura ao quadrado
    
    # Arredonda o resultado para 2 casas decimais
    return round(imc, 2)                  # Retorna o valor arredondado


def classificar_imc(imc):                 # Função que recebe o IMC e retorna a classificação
    """Classifica o IMC de acordo com os padrões da OMS."""
    
    if imc < 18.5:                        # Se o IMC for menor que 18.5
        return "Abaixo do peso"           # Retorna esta mensagem
    
    elif imc < 25.0:                      # Senão, se for menor que 25.0
        return "Peso normal"
    
    elif imc < 30.0:                      # Senão, se for menor que 30.0
        return "Sobrepeso"
    
    elif imc < 35.0:                      # Senão, se for menor que 35.0
        return "Obesidade grau I"
    
    elif imc < 40.0:                      # Senão, se for menor que 40.0
        return "Obesidade grau II"
    
    else:                                 # Se não se encaixar em nenhuma das acima
        return "Obesidade grau III (mórbida)"


# ====================== PROGRAMA PRINCIPAL ======================

print("=== CÁLCULO DE IMC ===\n")        # Exibe o título do programa

# Bloco try para tratar possíveis erros do usuário
try:
    # Solicita o peso do usuário
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))      # Converte a entrada para número decimal
    
    # Solicita a altura do usuário
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))  # Converte para número decimal
    
    # Chamada da função para calcular o IMC
    imc = calcular_imc(peso, altura)      # Guarda o resultado na variável imc
    
    # Chamada da função para classificar
    classificacao = classificar_imc(imc)  # Guarda a classificação na variável
    
    # Exibe o resultado formatado
    print("\n" + "="*40)                  # Imprime uma linha de separação
    print(f"Seu IMC é: {imc}")            # Mostra o valor do IMC
    print(f"Classificação: {classificacao}")  # Mostra a classificação
    print("="*40)                         # Outra linha de separação

# Tratamento de erros
except ValueError:                        # Se o usuário digitar letra ao invés de número
    print("❌ Erro: Por favor, digite apenas números válidos.")
    
except Exception as e:                    # Qualquer outro erro
    print(f"❌ Ocorreu um erro: {e}")


# Mensagem final de orientação
print("\nDica: O IMC é apenas uma referência.")
print("Consulte um nutricionista ou médico para avaliação completa.")