# Lista de perguntas e respostas
quiz = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Paris", "Londres", "Roma", "Berlim"],
        "resposta": "Paris"
    },
    {
        "pergunta": "Em que continente está o Brasil?",
        "opcoes": ["Ásia", "Europa", "América do Sul", "África"],
        "resposta": "América do Sul"
    },
    {
        "pergunta": "Qual país tem a maior população do mundo?",
        "opcoes": ["Índia", "Estados Unidos", "China", "Rússia"],
        "resposta": "China"
    }
]

# Função para rodar o quiz
def iniciar_quiz():
    pontuacao = 0
    for i, q in enumerate(quiz, 1):
        print(f"\nPergunta {i}: {q['pergunta']}")
        for idx, opcao in enumerate(q["opcoes"], 1):2
            print(f"{idx}. {opcao}")
        escolha = input("Digite o número da resposta: ")
        try:
            if q["opcoes"][int(escolha) - 1] == q["resposta"]:
                print("✅ Correto!")
                pontuacao += 1
            else:
                print(f"❌ Errado! A resposta correta é: {q['resposta']}")
        except (ValueError, IndexError):
            print("⚠️ Resposta inválida.")
    print(f"\nSua pontuação final: {pontuacao}/{len(quiz)}")

# Iniciar o quiz
iniciar_quiz()
