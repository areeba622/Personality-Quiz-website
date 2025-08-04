from flask import Flask, render_template, request, redirect, url_for, session
from collections import Counter

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# List of questions with options and associated personality types
questions = [
   {
    "id": 1,
    "text": "How do you react when you get unexpected marks in an exam?",
    "options": {
        "OMG Yesss! Full chill vibes 😎": "Chill",
        "Of course I failed... I already knew. 😔": "Disappointed",
        "BROOO this exam was not even in the syllabus! 🤯📚": "Drama"
    }
},
{
    "id": 2,
    "text": "What’s your excuse when the professor catches you late to class?",
    "options": {
        "Sir, traffic was like Fast & Furious today 🏎️💨": "Disappointed",
        "!Breathing like I ran a marathon! Sir, I RAN! 🏃‍♂️😤": "Drama",
        "Chill sir, thoda late hi toh hua 😌⌚": "Chill"
    }
},
{
    "id": 3,
    "text": "How do you feel when your friends cancel a group hangout last minute?",
    "options": {
        "Told you! Group plans NEVER work. 🙄": "Disappointed",
        "Wait WHAT?! No one told me?! 😤💔": "Drama",
        "Haha good. I didn’t wanna go anyway 😎": "Chill"
    }
},
{
    "id": 4,
    "text": "What’s your strategy for group projects?",
    "options": {
        "Guess I’ll do everything... again. 😩📄": "Disappointed",
        "Someone will do it. Not my tension ✌️": "Chill",
        "I’m here for vibes, not assignments ✨💁‍♀️": "Drama"
    }
},
{
    "id": 5,
    "text": "What’s your reaction when a professor extends the deadline?",
    "options": {
        "Yay! Now I can chill even more 🛌🍿": "Chill",
        "Bruhh I already submitted 😩": "Disappointed",
        "We had a deadline?? 😳📚": "Drama"
    


        },
    },
]

@app.route("/")
def index():
    return redirect(url_for("question", qid=1))

@app.route("/question/<int:qid>", methods=["GET", "POST"])
def question(qid):
    if qid > len(questions):
        return redirect(url_for("results"))

    if request.method == "POST":
        answer = request.form.get("answer")
        session[f"question_{qid}"] = answer
        return redirect(url_for("question", qid=qid + 1))

    current_question = questions[qid - 1]
    return render_template("question.html", question=current_question, qid=qid)

@app.route("/results")
def results():
    answers = [
        {
            "question": questions[i]["text"],
            "answer": session.get(f"question_{i + 1}", "No answer"),
        }
        for i in range(len(questions))
    ]
    
    # Determine personality type based on answers
    personality_counter = Counter()
    for i, answer in enumerate(answers):
        question = questions[i]
        selected_answer = answer["answer"]
        personality_type = question["options"].get(selected_answer, "Unknown")
        personality_counter[personality_type] += 1

    # Get the most common personality type
    personality = personality_counter.most_common(1)[0][0] if personality_counter else "Unknown"

    # Map personality to an image
    personality_images = {
        "Chill": "chill_image.jpg",
        "Disappointed": "disappointed_image.jpg",
        "Drama": "drama_image.jpg",
    }
    image = personality_images.get(personality, "default_image.jpg")

    return render_template("results.html", answers=answers, personality=personality, image=image)

if __name__ == "__main__":
    
    # For development (running locally)
    app.run(debug=True, host='0.0.0.0', port=80)
