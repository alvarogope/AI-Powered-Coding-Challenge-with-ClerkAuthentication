import os
import json
import random
from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv

_backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(_backend_dir, ".env"))
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOPICS = [
    "Python syntax and built-ins",
    "JavaScript closures and scope",
    "time and space complexity",
    "hash maps and sets",
    "linked lists and trees",
    "recursion and dynamic programming",
    "SQL queries and joins",
    "REST API design",
    "Git workflows",
    "object-oriented design",
    "functional programming patterns",
    "concurrency and async code",
    "regular expressions",
    "bit manipulation",
    "sorting and searching algorithms",
    "memory management",
    "type systems and generics",
    "error handling strategies",
    "testing and debugging",
    "security basics (XSS, SQL injection, auth)",
]

LANGUAGES = ["Python", "JavaScript", "Java", "C++", "Go", "Rust", "SQL", "TypeScript"]


def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    topic = random.choice(TOPICS)
    language = random.choice(LANGUAGES)
    variation_id = random.randint(100000, 999999)

    system_prompt = """You are an expert coding challenge creator.
Your task is to generate a unique coding question with multiple choice answers.
Every response must be a fresh question — never repeat common textbook examples.

For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.
For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

Return the challenge in the following JSON structure:
{
    "title": "The full question text, including any code snippet if needed",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct_answer_id": 0,
    "explanation": "Detailed explanation of why the correct answer is right"
}

Make sure the options are plausible but with only one clearly correct answer.
Include a short code snippet in the title when it helps the question.
"""
    user_prompt = (
        f"Generate a unique {difficulty} difficulty coding challenge. "
        f"Focus on: {topic}. Prefer examples in {language}. "
        f"Variation ID: {variation_id} — use this to ensure the question is distinct from prior ones."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.9,
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)

        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Field {field} not found in challenge data")

        if not isinstance(challenge_data["options"], list) or len(challenge_data["options"]) != 4:
            raise ValueError("options must be a list of exactly 4 items")

        correct_id = challenge_data["correct_answer_id"]
        if not isinstance(correct_id, int) or correct_id < 0 or correct_id > 3:
            raise ValueError("correct_answer_id must be an integer between 0 and 3")

        return challenge_data

    except Exception as e:
        raise e
