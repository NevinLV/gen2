from huggingface_hub import InferenceClient
from optimum.intel.openvino import OVModelForCausalLM
from transformers import AutoTokenizer, pipeline

import re

import transformers
import torch

model_id = "MTSAIR/Cotype-Nano-CPU"
model = OVModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=2048, device="cpu")

def remove_quoted_text(input_string):
    # Регулярное выражение для поиска текста в тройных апострофах
    pattern = r"```python(.*?)```"
    # Заменяем найденные подстроки на пустую строку

    result = re.findall(pattern, input_string, re.DOTALL)
    # Удаляем лишние пробелы
    result = ' '.join(result.split())
    return result


def generate_code(task_text: str):
    messages = [
        {
            "role": "user",
            "content": f"Дана задача: \"{task_text}\". Напиши на python код, который будет генерировать 10 подобных задач, но с разными условиями. Так же код должен решать все эти задачи. На выходе программа должна вывести кортежи, где на первом месте будет условие задачи, а на втором - ответ. Необходимо написать только код, никаких лишних слов и сообщений."
        },
    ]

    results = pipe(messages)
    print(results[0].get("generated_text")[1].get("content"))

    code = results[0].get("generated_text")[1].get("content")
    res = re.search(r'```python\n(.*?)\n```', code, re.DOTALL).group(1)

    return res
