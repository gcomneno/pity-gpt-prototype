import sys
from config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

def send_prompt_and_get_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=500
        )

        generated_text = response['choices'][0]['text']
        print("\nAnnuncio rigenerato:", generated_text)

    except Exception as e:
        print("Errore durante l'interazione con OpenAI:", str(e))

if __name__ == "__main__":
    # Leggi il contesto da indicare all'AI
    with open('case.ctx', 'r') as file:
        context = file.read()

    # Leggi il testo dell'annuncio
    with open('annuncio.txt', 'r') as file:
        text_to_be_boosted = file.read()

    print("Annuncio da valutare:\n\n", text_to_be_boosted)

    # Crea il prompt con la richiesta di traduzione
    prompt = f"{context}\n{text_to_be_boosted}"

    # Invia il prompt a OpenAI e mostra la risposta
    send_prompt_and_get_response(prompt)
