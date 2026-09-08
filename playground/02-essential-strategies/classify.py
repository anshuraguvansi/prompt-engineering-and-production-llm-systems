import json
from pathlib import Path
import time

from openai import OpenAI


system_prompt_zero_shot = """
Classify this review as positive, neutral, or negative.
Return only JSON: {"label": "positive|neutral|negative", confidence: number}
"""

system_prompt_one_shot = """
Classify given <review> as positive, neutral, or negative.
Return only JSON: {"label": "positive|neutral|negative", confidence: number}

Example:
Review: "It arrived, but I have not used it yet."
Label: neutral
"""

system_prompt_few_shot = """
Classify give <review> as positive, neutral, or negative.
Return only JSON: {"label": "positive|neutral|negative", confidence: number}

Examples:
Review: "Setup took five minutes and everything worked." -> positive
Review: "It arrived, but I have not used it yet." -> neutral
Review: "The device stopped charging after two days." -> negative
"""

user_prompt = """
<review>{{review}}</review>
"""


def build_prompt(message: str) -> str:
    return user_prompt.replace("{{review}}", message)


def main() -> None:
    inputs_path = Path(__file__).with_name("inputs.json")
    inputs = json.loads(inputs_path.read_text())
    client = OpenAI()

    for item in inputs:
        start_time = time.time()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt_few_shot},
                {"role": "user", "content": build_prompt(item["review"])},
            ],
            temperature=0.0,
            top_p=1.0,
            response_format={"type": "json_object"},
        )
        end_time = time.time()
        print("##################################################################")
        print(
            f"OUTPUT: {response.choices[0].message.content} Expected:{item['expected_label']}"
        )
        print(f"TOTAL TOKENS: {response.usage.total_tokens}")
        print(f"PROMPT TOKENS: {response.usage.prompt_tokens}")
        print(f"COMPLETION TOKENS: {response.usage.completion_tokens}")
        print(f"TIME TAKEN: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
