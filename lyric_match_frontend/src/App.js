import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Import the CSS file

function App() {
  const [lyricSnippet, setLyricSnippet] = useState('');
  const [userGuess, setUserGuess] = useState('');
  const [result, setResult] = useState('');
  const [correctTitle, setCorrectTitle] = useState('');

  const generateLyricSnippet = async () => {
    try {
      const response = await axios.get('http://localhost:5000/generate-lyric');
      setLyricSnippet(response.data.lyricSnippet);
      setCorrectTitle(response.data.correctTitle);
      setResult('');
    } catch (error) {
      console.error('Error generating lyric snippet:', error);
    }
  };

  const checkAnswer = async () => {
    try {
      const response = await axios.post('http://localhost:5000/check-answer', {
        userGuess,
        correctTitle,
      });
      setResult(response.data.result);
    } catch (error) {
      console.error('Error checking answer:', error);
    }
  };

  return (
    <div className="App">
      <h1>Lyric Match</h1>
      <button onClick={generateLyricSnippet}>Generate Lyric Snippet</button>
      <div>
        <h3>Lyric Snippet:</h3>
        <p>{lyricSnippet}</p>
      </div>
      <input
        type="text"
        placeholder="Enter your guess"
        value={userGuess}
        onChange={(e) => setUserGuess(e.target.value)}
      />
      <button onClick={checkAnswer}>Check Answer</button>
      <div className="result">
        <h3>Result:</h3>
        <p>{result}</p>
        {result === 'Incorrect' && <p>Correct Title: {correctTitle}</p>}
      </div>
    </div>
  );
}

export default App;
