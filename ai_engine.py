import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from euriai import EuriaiClient

load_dotenv()

llm = EuriaiClient(
    api_key=os.getenv("EURIAI_API_KEY"),
    model="gpt-4.1-nano",
)


def explain_code(language: str, topic: str, level: str) -> str:
    """
    Generate an explanation of a code snippet in the specified language and topic.

    Args:
        language (str): The programming language of the code.
        topic (str): The topic or concept to explain.
        level (str): The level of detail for the explanation (e.g., 'beginner', 'intermediate', 'advanced').

    Returns:
        str: The generated explanation.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful coding assistant."),
            ("user", "Explain the {topic} in {language} at a {level} level."),
        ]
    )
    prompt_str = prompt.format(topic=topic, language=language, level=level)
    response = llm.generate_completion(
        prompt=prompt_str,
        max_tokens=2000,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']


def generate_code(language: str, topic: str, level: str) -> str:
    """
    Generate a code snippet in the specified language and topic.

    Args:
        language (str): The programming language for the code.
        topic (str): The topic or concept to generate code for.
        level (str): The level of detail for the code (e.g., 'beginner', 'intermediate', 'advanced').

    Returns:
        str: The generated code snippet.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful coding assistant."),
            ("user", "Generate a {level} level code snippet in {language} for {topic}."),
        ]
    )
    
    prompt_str = prompt.format(topic=topic, language=language, level=level)
    response = llm.generate_completion(
        prompt=prompt_str, 
        max_tokens=1000,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']

def debug_code(language: str, code: str) -> str:
    """
    Debug a code snippet in the specified language.

    Args:
        language (str): The programming language of the code.
        code (str): The code snippet to debug.

    Returns:
        str: The debugged code snippet or error message.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful coding assistant."),
            ("user", "Debug the following {language} code:\n{code}"),
        ]
    )
    prompt_str = prompt.format(language=language, code=code)
    response = llm.generate_completion(
        prompt=prompt_str,
        max_tokens=1000,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']

