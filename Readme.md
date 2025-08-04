# Meme-Based Personality Quiz App 🎭😂

A light-hearted, meme-inspired personality quiz web app designed to entertain users while categorizing them into funny personality types — *Chill*, *Drama*, or *Disappointed* — based on their responses to relatable student life scenarios.

---

## 🧠 Description

This web application presents a series of multiple-choice questions (inspired by common university life experiences). Based on the user's responses, the app calculates a personality type and displays a corresponding meme and meme picture.

---

## 🌐 Front-End

The front-end is built using **HTML**, **CSS**.

- Clean and minimalist UI.
- **Hover effects** for option highlighting.
- Displays result-specific meme image.
- Simple, humor friendly language.

---

## 🖥️ Back-End

The back-end is developed using **Python Flask**.

- Flask handles routing, rendering templates, and form submission.
- Questions and options are loaded from a structured dictionary (`quiz_data`).
- User responses are collected, personality is calculated based on response types.
- Corresponding result and meme image are rendered dynamically.

---

## 📁 Project Structure

MemeQuiz/
├── static/
│   ├── images/
│   │   ├── chill_image.jpg
│   │   ├── dissapointed_image.jpg
│   │   └── drama_image.jpg
|   |
│   └── styles.css 
|
├── templates/
│   ├── question.html
│   └── results.html
├── app.py
├── requirements.txt
└── README.md


## ⚙️ Installation & Running the App

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/meme-personality-quiz.git
cd meme-personality-quiz

