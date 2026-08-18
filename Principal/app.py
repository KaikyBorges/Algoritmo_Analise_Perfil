import streamlit as st
import pandas as pd
from pathlib import Path

from questions_data import load_questions


st.set_page_config(
    page_title="Algoritmo de Análise de Perfil",
    page_icon="🎓",
    layout="wide"
)

.StMarkdown a {
    color:red
}



BASE_DIR = Path(__file__).resolve().parent

logo = BASE_DIR.parent / "images" / "logo.png"
style = BASE_DIR / "style.css"


if logo.exists():
    st.logo(
        str(logo),
        size="large",
        link="https://www.instagram.com/escola_renato/"
    )


if style.exists():
    with open(style, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def calcular_resultados(answers, questions):
    scores = {}

    for q_idx, answer_idx in answers.items():
        if answer_idx is None:
            continue

        pesos = questions[q_idx]["pesos"][answer_idx]

        for materia, peso in pesos.items():
            scores[materia] = scores.get(materia, 0) + peso

    return scores


def show_results(scores):
    if not scores:
        st.warning(
            "Não foi possível determinar uma área de afinidade. "
            "Tente novamente."
        )
        return

    df = pd.DataFrame(
        list(scores.items()),
        columns=["Curso/Área", "Pontuação"]
    )

    df = (
        df
        .sort_values("Pontuação", ascending=False)
        .reset_index(drop=True)
    )

    curso_top = df.iloc[0]["Curso/Área"]
    pontuacao = df.iloc[0]["Pontuação"]

    st.subheader(f"Resultado: {curso_top}")

    esq, dir = st.columns(2)

    with esq:
        st.markdown("### 📊 Afinidade com outras áreas")
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


if "tela_inicial" not in st.session_state:
    st.session_state.tela_inicial = True

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "questions" not in st.session_state:
    st.session_state.questions = load_questions()

if "submitted" not in st.session_state:
    st.session_state.submitted = False


if st.session_state.tela_inicial:

    st.title("🎓 Algoritmo para Análise de Perfil")

    st.markdown(
        """
        ### Descubra qual área combina mais com você!

        Este teste foi criado para ajudar você a descobrir
        qual curso ou área pode ter maior compatibilidade
        com o seu perfil estudantil.

        Você responderá perguntas simples sobre como pensa,
        age e aprende.

        Ao final, verá:

        - 🎯 O curso/área mais compatível
        - 📊 A pontuação das outras áreas
        - 💡 Uma recomendação baseada nas suas respostas
        """
    )

    if st.button(
        "🚀 Iniciar Teste",
        use_container_width=True
    ):
        st.session_state.tela_inicial = False
        st.session_state.current_question = 0
        st.rerun()


else:

    total = len(st.session_state.questions)

    if total == 0:
        st.error("Nenhuma pergunta foi encontrada.")

    else:

        current = st.session_state.current_question

        if current >= total:
            current = total - 1
            st.session_state.current_question = current

        if not st.session_state.submitted:

            q = st.session_state.questions[current]

            progress = (current + 1) / total

            st.progress(progress)

            st.markdown(
                f"""
                <div id="Perguntas">
                    <center>
                        <h4>
                            Pergunta {current + 1} de {total}
                        </h4>
                    </center>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <h3>{q["pergunta"]}</h3>
                """,
                unsafe_allow_html=True
            )

            key = f"q_{current}"

            alternativas = q["alternativas"]

            resposta = st.radio(
                "Escolha uma opção:",
                alternativas,
                key=key
            )

            idx = alternativas.index(resposta)

            st.session_state.answers[current] = idx

            col1, col2 = st.columns(2)

            with col1:
                if current > 0:
                    if st.button(
                        "⬅️ Anterior",
                        use_container_width=True
                    ):
                        st.session_state.current_question -= 1
                        st.rerun()

            with col2:
                if current < total - 1:
                    if st.button(
                        "Próximo ➡️",
                        use_container_width=True
                    ):
                        st.session_state.current_question += 1
                        st.rerun()
                else:
                    if st.button(
                        "Finalizar ✅",
                        use_container_width=True
                    ):
                        st.session_state.submitted = True
                        st.rerun()

        else:

            scores = calcular_resultados(
                st.session_state.answers,
                st.session_state.questions
            )

            show_results(scores)

            st.markdown("---")

            if st.button(
                "🔁 Reiniciar Teste",
                use_container_width=True
            ):
                st.session_state.tela_inicial = True
                st.session_state.current_question = 0
                st.session_state.answers = {}
                st.session_state.submitted = False

                for key in list(st.session_state.keys()):
                    if key.startswith("q_"):
                        del st.session_state[key]

                st.rerun()


st.markdown(
    """
    <div class="sobre_nos">
        <center>
            <p>
                <a
                    href="https://www.instagram.com/escola_renato/"
                    target="_blank"
                >
                    Sobre nós
                </a>
            </p>
        </center>
    </div>
    """,
    unsafe_allow_html=True
)
