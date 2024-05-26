from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import re

app = Flask(__name__)

# Load pre-trained model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template('index.html')

def remove_repetitions(text):
    # Simple regex to remove repeated phrases
    return re.sub(r'(\b\w+\b)(?:\s+\1\b)+', r'\1', text)

def complete_sentence(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    max_length = len(input_ids[0]) + 16  # Adjust the max_length as needed

    # Generate text with adjusted parameters
    outputs = model.generate(
        input_ids, 
        max_length=max_length, 
        num_return_sequences=1, 
        temperature=0.7,  # Control randomness
        top_k=50,  # Limit to top-k tokens
        top_p=0.95,  # Nucleus sampling
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Decode the output
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract the generated part only
    generated_part = generated_text[len(input_text):].strip()

    # Find the end of the first sentence
    sentence_end = re.search(r'[.!?]', generated_part)
    if sentence_end:
        generated_part = generated_part[:sentence_end.end()]

    # Remove repetitions
    generated_part = remove_repetitions(generated_part)

    return generated_part

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.get_json()
    input_text = data['word']

    generated_text = complete_sentence(input_text)
    
    print(f"Processed input word: {input_text}")
    print(f"Generated text: {generated_text}")
    
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
