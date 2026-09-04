# Algoritmo de Análise de Perfil

Aplicação interativa em **Python + Streamlit** que aplica um questionário vocacional e recomenda a área/curso com maior afinidade com o perfil do estudante, entre: Ciência de Dados, Desenvolvimento de Sistemas, Enfermagem, Exatas e Humanas.

Desenvolvido para apoiar a orientação educacional de estudantes da **Escola Renato De Arruda Penteado**.

> **Escopo:** projeto educacional/institucional. O resultado é uma indicação de afinidade baseada em um questionário simplificado, não uma avaliação psicométrica validada.

## Stack

- **Python 3**
- **Streamlit** — interface e gerenciamento de estado da sessão
- **Pandas** — estruturação e ordenação dos resultados
- **CSS personalizado** — identidade visual da instituição

## Como funciona o algoritmo

O questionário tem 10 perguntas, cada uma com 5 alternativas. Cada alternativa carrega um conjunto de pesos para as 5 áreas avaliadas — por exemplo, escolher a alternativa que reflete afinidade com dados soma pontos em "Ciência de Dados".

**Decisão de design:** os pesos são definidos por **posição da alternativa**, e essa posição é consistente em todas as perguntas (a alternativa "ligada a dados" está sempre na 1ª posição, a "ligada a cuidado com pessoas" sempre na 2ª, e assim por diante). Isso foi uma simplificação proposital: manter uma estrutura fixa de pesos facilita adicionar novas perguntas no futuro (basta escrever o texto das 5 alternativas mantendo a ordem temática) e evita inconsistência entre pesos definidos pergunta a pergunta.

Ao final, as pontuações de todas as respostas são somadas por área, e a área com maior pontuação é exibida como resultado principal, junto com uma tabela comparativa de afinidade com as demais áreas.

## Estrutura do projeto

```
Principal/
├── app.py               # Interface Streamlit, navegação e cálculo do resultado
├── questions_data.py     # Banco de perguntas, alternativas e pesos (load_questions)
├── style.css             # Estilo visual (cores, layout, rodapé)
└── images/
    ├── logo.png
    └── barra.png
```

O estado do questionário (pergunta atual, respostas dadas, se já foi finalizado) é mantido inteiramente em `st.session_state` — não há persistência em banco de dados; cada sessão do navegador é independente e os dados não são salvos após o fechamento.

## Fluxo da aplicação

1. **Tela inicial** — apresentação do teste e botão para iniciar
2. **Questionário** — uma pergunta por vez, com navegação Anterior/Próximo e barra de progresso
3. **Finalização** — cálculo das pontuações por área a partir de todas as respostas
4. **Resultado** — área de maior afinidade em destaque, com tabela comparativa das demais áreas
5. **Reiniciar** — limpa o estado da sessão e volta à tela inicial

## Rodando o projeto

```bash
pip install streamlit pandas
streamlit run Principal/app.py
```

A aplicação abre automaticamente em `http://localhost:8501`.

## Personalização

O arquivo `style.css` controla cores, estilo do bloco de recomendação, rodapé e tipografia. Pode ser adaptado para outra identidade visual sem alterar a lógica da aplicação.

## Autores

Projeto desenvolvido por alunos para apoiar a orientação educacional dos estudantes da Escola Renato De Arruda Penteado.

Instagram da instituição: [@escola_renato](https://www.instagram.com/escola_renato/)

## Licença

Uso livre para fins educacionais.


