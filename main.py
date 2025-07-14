import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("SENTIMENTANALYZER_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

# Fungsi analisis
def analyze_post(text):
  try:
    prompt = f"""
    Analisis kalimat atau kata ini '{text}'. Tentukanlah sentimen dari kalimat atau kata tersebut.
    Apakah kalimat atau kata tersebut positif, negatif, atau netral? Berikan jawaban hanya dengan positif, negatif dan netral saja.
    """
    response = model.generate_content(prompt)
    if 'positif' in response.text.lower():
      return 'Positif 😊'
    elif 'negatif' in response.text.lower():
      return 'Negatif 😕'
    else:
      return 'Netral 😐'
  except Exception as e: # jika terjadi error lainnya
    print(f"Terjadi kesalahan: {e}")
    return None

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
      text = request.form.get('text')
      hasil = analyze_post(text)
      return render_template('index.html', message=hasil, text=text)
    return render_template("index.html", message="", text="..")

if __name__ == "__main__":
    app.run(debug=True)


