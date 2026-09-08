import json
from pathlib import Path
import time

from openai import OpenAI


system_prompt = """
Task:
Classify the customer message into exactly one category.

Rules:
- Use the customer's primary issue.
- Do not infer sensitive attributes.
- If ambiguous, choose other.

Output:
Return JSON matching:
{
  "category": "billing | access | bug | feature_request | other",
  "confidence": 0.0,
  "reason": "short evidence-based explanation"
}
"""


user_prompt = """
Context:
<customer_message>
{{message}}
</customer_message>
"""


def build_prompt(message: str) -> str:
    return user_prompt.replace("{{message}}", message)


def main() -> None:
    inputs_path = Path(__file__).with_name("inputs.json")
    inputs = json.loads(inputs_path.read_text())
    client = OpenAI()

    for item in inputs:
        start_time = time.time()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": build_prompt(item["message"])},
            ],
            temperature=0.0,
            top_p=1.0,
            response_format={"type": "json_object"},
        )
        end_time = time.time()
        print("##################################################################")
        print(f"OUTPUT: {response.choices[0].message.content}")
        print(f"TOTAL TOKENS: {response.usage.total_tokens}")
        print(f"PROMPT TOKENS: {response.usage.prompt_tokens}")
        print(f"COMPLETION TOKENS: {response.usage.completion_tokens}")
        print(f"TIME TAKEN: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
