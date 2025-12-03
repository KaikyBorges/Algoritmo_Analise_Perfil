# Algoritmo_Analise_Perfil
Algoritmo para analise de perfil estudantil, tem o intuito de calcular o seu perfil estudantil para a designação de melhor indicação de curso técnico entre: Ciencia De Dados, Desenvolvimento De Sistemas, Enferagem e Itinerários Formativos


Algoritmo de Análise de Perfil – Streamlit

Este projeto é uma aplicação interativa desenvolvida em Python + Streamlit para auxiliar estudantes a descobrir qual área ou curso combina melhor com seu perfil.
Através de um questionário adaptativo, o algoritmo calcula pontuações com base nas respostas e recomenda a área com maior afinidade, como:

Enfermagem

Ciência de Dados

Desenvolvimento de Sistemas

Exatas

Humanas

🚀 Funcionalidades

✔️ Questionário com várias perguntas e múltiplas alternativas
✔️ Cálculo automático de pontuações por área
✔️ Interface moderna e personalizada via style.css
✔️ Sistema de navegação com Anterior, Próximo e Finalizar
✔️ Exibição da área mais compatível + tabela completa dos resultados
✔️ Possibilidade de reiniciar o teste
✔️ Logo e link institucional

🛠️ Tecnologias Utilizadas

Python 3+

Streamlit

Pandas

Altair

CSS personalizado

▶️ Como executar o projeto
1️⃣ Instale as dependências

No terminal:

pip install streamlit pandas altair

2️⃣ Execute a aplicação
streamlit run app.py


O navegador abrirá automaticamente em http://localhost:8501.

📊 Como funciona o algoritmo?

Cada alternativa escolhida possui um conjunto de pesos que soma pontos para diferentes áreas.
Exemplo simplificado:

{"Enfermagem": 0, "Ciência de Dados": 3, "Desenvolvimento de Sistemas": 1}


Ao final, o curso com maior pontuação é o recomendado.

🎨 Personalização

O arquivo style.css controla:

cores do app

estilo do bloco de recomendação

rodapé personalizado Sobre nós

fonte, espaçamentos e organização visual

Você pode editar livremente para combinar com sua identidade visual.

👥 Autores

Projeto desenvolvido por alunos para auxiliar na orientação educacional dos estudantes da Escola Renato De Arruda Penteado

Instagram da instituição:
🔗 https://www.instagram.com/escola_renato/

📜 Licença

Este projeto é de uso livre para fins educacionais.
