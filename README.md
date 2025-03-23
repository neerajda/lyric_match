# Lyric Match

Lyric Match is a web application that generates random lyric snippets from popular songs and challenges users to guess the correct song title.

## Features
- Generates 2-4 lines of lyrics from a random song.
- Allows users to input their guess for the song title.
- Validates the user's guess and provides feedback on correctness.

## Tech Stack
- **Frontend:** React.js
- **Backend:** Flask
- **ML Model:** GPT-Neo 1.3B (via `transformers` pipeline)
- **API Calls:** Axios

## Installation & Setup
### Backend (Flask API)
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/lyric_match.git
   cd lyric_match/lyric_match_backend
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask server:**
   ```sh
   python app.py
   ```
   The API will run at `http://localhost:5000`.

### Frontend (React.js App)
1. **Navigate to the frontend directory:**
   ```sh
   cd ../lyric_match_frontend
   ```
2. **Install dependencies:**
   ```sh
   npm install
   ```
3. **Start the React app:**
   ```sh
   npm start
   ```
   The app will be available at `http://localhost:3000`.

## API Endpoints
### 1. Generate Lyric Snippet
- **Endpoint:** `GET /generate-lyric`
- **Response:**
  ```json
  {
    "lyricSnippet": "Some generated lyrics here...",
    "correctTitle": "Imagine"
  }
  ```

### 2. Check Answer
- **Endpoint:** `POST /check-answer`
- **Request Body:**
  ```json
  {
    "userGuess": "Imagine",
    "correctTitle": "Imagine"
  }
  ```
- **Response:**
  ```json
  {
    "result": "Correct"
  }
  ```


## Author
Neeraj Yadav

