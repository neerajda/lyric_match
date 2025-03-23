from flask import Flask, request, jsonify
from transformers import pipeline
import re

app = Flask(__name__)

# Load a text generation model (e.g., GPT-Neo 1.3B)
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

# List of songs
songs = [
    "Bohemian Rhapsody",
    "Hotel California",
    "Imagine",
    "Rolling in the Deep",
    "Shape of You",
    "Someone Like You",
    "Hey Jude",
    "Billie Jean",
    "Smells Like Teen Spirit",
    "Wonderwall",
    "Yesterday",
    "Let It Be",
    "Purple Haze",
    "Stairway to Heaven",
    "Sweet Child O' Mine",
    "Thriller",
    "Like a Rolling Stone",
    "Hallelujah",
    "Fix You",
    "Dancing Queen"
]

def clean_lyrics(text):
    # Remove the prompt and extract only the lyric snippet
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    # Skip the first line (which contains the prompt) and return the next 2-4 lines
    return '\n'.join(lines[1:5])

@app.route('/generate-lyric', methods=['GET'])
def generate_lyric():
    try:
        import random
        random_song = random.choice(songs)
        prompt = f'Write 2-4 lines of lyrics from the song "{random_song}" without revealing the title. The lyrics should be poetic, evocative, and recognizable. Do not include any additional text or explanations.'
        result = generator(prompt, max_length=100, num_return_sequences=1)
        lyric_snippet = clean_lyrics(result[0]['generated_text'])
        return jsonify({
            'lyricSnippet': lyric_snippet,
            'correctTitle': random_song
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/check-answer', methods=['POST'])
def check_answer():
    try:
        data = request.json
        user_guess = data.get('userGuess')
        correct_title = data.get('correctTitle')
        is_correct = user_guess.lower() == correct_title.lower()
        return jsonify({'result': 'Correct' if is_correct else 'Incorrect'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)