QUIZ_PROMPT_TEMPLATE = """
Generate {num_questions} quiz questions from the article below.

For each question provide:
- Question
- Option A
- Option B
- Option C
- Option D
- Correct Answer (A/B/C/D)
- Difficulty (easy/medium/hard)
- Explanation
- Related topics (comma separated)

Return the response in this EXACT format for every question:

QUESTION:
...
A:
...
B:
...
C:
...
D:
...
ANSWER:
...
DIFFICULTY:
...
EXPLANATION:
...
TOPICS:
...

ARTICLE TITLE:
{title}

SUMMARY:
{summary}

SECTIONS:
{sections}
"""
