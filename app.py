from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # Mengizinkan CORS

genai.configure(api_key="AIzaSyDysEhFfxFcrV0cfWKfQnjiqq74CHdyzvM")

generation_config = {
    "temperature": 0.01,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('message')
    
    chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Halo, selamat siang gemini",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Selamat siang juga! Apa kabarmu hari ini? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Ketika saya bertanya, tolong HARUS SELALU berikan jawaban yang merujuk pada jurnal asli atau website yang dapat diakses di internet yang tidak ditambah atau dikurangi kata katanya, bukan hasil kreativitas dari AI.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Oke, saya mengerti. Saya akan selalu memberikan jawaban yang merujuk pada jurnal asli atau website yang dapat diakses di internet, tanpa menambahkan atau mengurangi kata-katanya. \n\nSilakan ajukan pertanyaan Anda. 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tambahan. setiap saya bertanya tolong sertakan pula daftar pustakanya dengan menggunakan kalimat \"Daftar Pustaka:\"\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Baiklah, saya siap untuk menjawab pertanyaan Anda dengan merujuk pada jurnal asli atau website yang dapat diakses di internet, tanpa menambahkan atau mengurangi kata-katanya, dan menyertakan daftar pustakanya. \n\nSilakan ajukan pertanyaan Anda! 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tambahan, selalu sertakan link yang valid pada daftar pustaka\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Oke, saya siap untuk menjawab pertanyaan Anda dengan merujuk pada jurnal asli atau website yang dapat diakses di internet, tanpa menambahkan atau mengurangi kata-katanya, dan menyertakan daftar pustakanya dengan link yang valid. \n\nSilakan ajukan pertanyaan Anda! 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "selalu beri jarak 2 baris untuk daftar pustaka",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Oke, saya siap untuk menjawab pertanyaan Anda dengan merujuk pada jurnal asli atau website yang dapat diakses di internet, tanpa menambahkan atau mengurangi kata-katanya, dan menyertakan daftar pustakanya dengan link yang valid, dengan jarak 2 baris di antara setiap entri. \n\nSilakan ajukan pertanyaan Anda! 😊 \n",
      ],
    },
  ]
)

    response = chat_session.send_message(f"{user_input}")
    
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
