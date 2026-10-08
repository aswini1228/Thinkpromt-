import streamlit as st
from llm import generate_response
from prompt_templates import build_prompt


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="ThinkPrompt",
    page_icon="🧠",
    layout="centered"
)


# -----------------------------------
# HEADER
# -----------------------------------

st.title("🧠 ThinkPrompt")

st.subheader("Think Better. Prompt Smarter.")

st.write(
    "Explore different Prompt Engineering techniques "
    "and generate AI responses using the same task."
)


# -----------------------------------
# TASK INPUT
# -----------------------------------

task = st.text_area(
    "Enter your task:",
    placeholder=(
        "Example: Explain Artificial Intelligence "
        "to a school student."
    ),
    height=150
)


# -----------------------------------
# PROMPTING TECHNIQUE
# -----------------------------------

technique = st.selectbox(
    "Select Prompting Technique:",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)


# -----------------------------------
# MODEL SETTINGS
# -----------------------------------

st.subheader("⚙️ Generation Settings")

temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.2,
    step=0.1
)

max_tokens = st.slider(
    "Maximum Tokens",
    min_value=100,
    max_value=1000,
    value=500,
    step=100
)


# -----------------------------------
# GENERATE RESPONSE
# -----------------------------------

if st.button("🚀 Generate Response"):

    if task.strip() == "":
        st.warning("Please enter a task.")

    else:

        try:

            # Generate prompt based on technique
            final_prompt = build_prompt(
                technique,
                task
            )

            # Display generated prompt
            st.subheader("📝 Generated Prompt")

            st.code(
                final_prompt,
                language="text"
            )

            # Generate AI response
            with st.spinner(
                "Generating response..."
            ):

                answer = generate_response(
                    final_prompt,
                    temperature,
                    max_tokens
                )

            # Display response
            st.subheader("💡 AI Response")

            st.write(answer)

        except Exception as e:

            st.error(
                f"Error while generating response: {e}"
          )
