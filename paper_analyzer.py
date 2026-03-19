import google.generativeai as genai
import os


api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-3-flash-preview")

def summarize_paper(text):

    prompt = f"""
    Summarize this research paper.

    Provide:
    1. Summary
    2. Key Contributions
    3. Important Concepts
    4. Conclusion

    Paper:
    {text[:12000]}
    """

    response = model.generate_content(prompt)

    return response.text


def explain_simple(text):

    prompt = f"""
    Explain the following research paper in simple terms for beginners.

    Paper:
    {text[:12000]}
    """

    response = model.generate_content(prompt)

    return response.text


def ask_question(text, question):

    prompt = f"""
    Use the following research paper to answer the question.

    Paper:
    {text[:12000]}

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text
