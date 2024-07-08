import sys
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH="./CodeLlama3-8B-Python"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH,local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH,local_files_only=True)


def generate_code(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Write a Python hello world program"
    generated_code = generate_code(prompt)
    print(generated_code)


if __name__ == "__main__":
    main()