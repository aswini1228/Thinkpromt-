import os
from huggingface_hub import InferenceClient


# AI MODEL
MODEL = "meta-llama/Llama-3.2-3B-Instruct"


def generate_response(
    prompt,
    temperature=0.2,
    max_tokens=500
):

    # Get Hugging Face API token
    hf_token = os.getenv("HF_TOKEN")

    if not hf_token:
        raise RuntimeError(
            "HF_TOKEN is not set. "
            "Please add your Hugging Face API token."
        )

    # Create Hugging Face client
    client = InferenceClient(
        api_key=hf_token
    )

    # Send prompt to the AI model
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful and accurate "
                    "educational assistant. "
                    "Give clear answers suitable "
                    "for college students."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Return generated response
    return response.choices[0].message.content
