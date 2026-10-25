from groq import AsyncGroq
from config import GROQ_API_KEY, GROQ_MODEL

client = AsyncGroq(
    api_key=GROQ_API_KEY,
    timeout=15.0,
)


async def generate_text(
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.2,
):
    print("Menghubungi Groq...", flush=True)

    response = await client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        reasoning_effort="low",
        max_completion_tokens=1024,
    )

    result = response.choices[0].message.content or ""

    print("Respons Groq diterima.", flush=True)

    return result
