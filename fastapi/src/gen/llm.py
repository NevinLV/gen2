from optimum.intel.openvino import OVModelForCausalLM
from transformers import AutoTokenizer, pipeline

model_id = "MTSAIR/Cotype-Nano-CPU"
model = OVModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=2048, device="cpu")

messages = [
  {"role": "user", "content": "Дана задача: \"Сколько будет 2+2?\". Напиши на python код, который будет генерировать 10 подобных задач, но с разными условиями. Так же код должен решать все эти задачи. На выходе программа должна вывести кортежи, где на первом месте будет условие задачи, а на втором - ответ. Необходимо написать только код, никаких лишних слов и сообщений."},
]

results = pipe(messages)
print(results[0].get("generated_text")[1].get("content"))