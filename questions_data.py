import pandas as pd

def load_questions():
    return [
        {
            "pergunta": "Como você prefere passar seu tempo livre?",
            "alternativas": [
                "Explorando novas ferramentas de análise ou tecnologia",
                "Ajudando amigos ou familiares com algo que precisam",
                "Criando pequenos projetos ou programando algo novo",
                "Resolvendo quebra-cabeças ou estudando temas científicos",
                "Lendo sobre culturas, história ou assistindo documentários"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você reage a novas tecnologias ou inovações?",
            "alternativas": [
                "Analiso como elas podem melhorar a interpretação de dados",
                "Penso em como podem ajudar no cuidado com as pessoas",
                "Quero aprender a usá-las para criar algo novo",
                "Estudo os princípios científicos por trás delas",
                "Reflito sobre o impacto social ou ético que podem causar"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de desafio intelectual você prefere?",
            "alternativas": [
                "Decifrar padrões ou prever resultados com dados",
                "Entender as necessidades de outras pessoas e ajudá-las",
                "Resolver falhas em sistemas ou criar algo funcional",
                "Resolver equações ou problemas científicos complexos",
                "Analisar contextos históricos ou sociais para tirar lições"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você prefere se comunicar com os outros?",
            "alternativas": [
                "Usando gráficos ou dados para explicar minhas ideias",
                "De forma empática, ouvindo e oferecendo apoio",
                "Explicando soluções técnicas ou funcionais",
                "Apresentando conceitos lógicos ou científicos",
                "Discutindo ideias e valores humanos ou culturais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de evento ou atividade mais te interessa participar?",
            "alternativas": [
                "Conferências sobre tecnologia de dados ou inovação",
                "Campanhas de saúde ou voluntariado em comunidades",
                "Hackathons ou eventos de programação",
                "Feiras de ciências ou competições matemáticas",
                "Debates ou palestras sobre questões sociais e culturais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você avalia o sucesso de um projeto?",
            "alternativas": [
                "Pela precisão dos dados e resultados obtidos",
                "Pelo impacto positivo na vida das pessoas ajudadas",
                "Pela funcionalidade e eficiência do que foi criado",
                "Pela correção técnica ou científica das soluções",
                "Pelo benefício social ou cultural que gerou"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de impacto você gostaria de causar no mundo?",
            "alternativas": [
                "Melhorar decisões com base em dados e análises",
                "Ajudar diretamente na saúde e qualidade de vida das pessoas",
                "Criar tecnologias que facilitem a vida cotidiana",
                "Contribuir para descobertas científicas ou técnicas",
                "Promover mudanças sociais ou culturais positivas"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você prefere planejar algo importante?",
            "alternativas": [
                "Usando dados e previsões para antecipar resultados",
                "Considerando as necessidades e o bem-estar de todos envolvidos",
                "Desenvolvendo um sistema ou ferramenta para organizar tudo",
                "Baseando-me em lógica e métodos estruturados",
                "Pensando no impacto humano e nas relações interpessoais"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Que tipo de aprendizado mais te motiva?",
            "alternativas": [
                "Aprender a interpretar e usar grandes quantidades de dados",
                "Aprender técnicas para ajudar e cuidar de outras pessoas",
                "Aprender a programar ou construir sistemas digitais",
                "Aprender sobre teorias científicas e cálculos avançados",
                "Aprender sobre a história e o comportamento humano"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
        {
            "pergunta": "Como você define uma boa liderança?",
            "alternativas": [
                "Tomar decisões baseadas em dados e análises sólidas",
                "Cuidar da equipe e garantir o bem-estar de todos",
                "Guiar a equipe na criação de soluções práticas e inovadoras",
                "Resolver problemas complexos com lógica e precisão",
                "Inspirar com valores humanos e compreensão cultural"
            ],
            "pesos": [
                {"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1, "Exatas": 2, "Humanas": 0},
                {"Enfermagem": 3, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 1},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 3, "Exatas": 1, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 1, "Desenvolvimento de Sistemas": 0, "Exatas": 3, "Humanas": 0},
                {"Enfermagem": 0, "Ciência de Dados": 0, "Desenvolvimento de Sistemas": 0, "Exatas": 0, "Humanas": 3}
            ],
        },
    ]

def ask_questions(questions):
    scores = {}
    for q in questions:
        print("\n" + q["pergunta"])
        for i, alt in enumerate(q["alternativas"], start=1):
            print(f"  {i}. {alt}")
        while True:
            escolha = input("Escolha uma opção (número): ").strip()
            if not escolha.isdigit():
                print("Entrada inválida. Digite o número da opção.")
                continue
            idx = int(escolha) - 1
            if 0 <= idx < len(q["alternativas"]):
                pesos = q["pesos"][idx]
                for materia, peso in pesos.items():
                    scores[materia] = scores.get(materia, 0) + peso
                break
            else:
                print("Opção fora do intervalo. Tente novamente.")
    return scores

def show_results(scores):
    df = pd.DataFrame(list(scores.items()), columns=["Curso/Area", "Score"])
    df = df.sort_values("Score", ascending=False).reset_index(drop=True)
    print("\nResultados (ordenados):")
    print(df.to_string(index=False))
    
    if not df.empty:
        curso_maior_pontuacao = df.iloc[0]["Curso/Area"]
        pontuacao = df.iloc[0]["Score"]
        print(f"\n**Recomendação**: Com base nas suas respostas, você parece ter maior afinidade com **{curso_maior_pontuacao}** (Pontuação: {pontuacao}).")
        print("Isso indica que você pode se sair muito bem nesta área! Explore mais sobre este curso ou itinerário para confirmar seu interesse.")
    else:
        print("\n**Recomendação**: Não foi possível determinar uma área de maior afinidade. Por favor, tente responder às perguntas novamente.")

def main():
    questions = load_questions()
    scores = ask_questions(questions)
    show_results(scores)

if __name__ == "__main__":
    main()