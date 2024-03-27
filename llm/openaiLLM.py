
from llm.prompts.fillsection import FILLSECTION_PROMPT
from openai import OpenAI
client = OpenAI()


def section_fill(sop_description, section_template, example_from_knowledge):
    """
    fill the section using LLM.
    """
    prompt = FILLSECTION_PROMPT.format(sop_description = sop_description, section_template = section_template, example_from_knowledge = example_from_knowledge)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # tokens_used = completion['usage']['total_tokens']
    # print("toke usagen", tokens_used)
    # response = completion["choices"][0]["message"]["content"]
    # return response
    return completion.choices[0].message.content





# if __name__ == "__main__":
#     fill_section_helper("example sop description", "template one", "abcd")