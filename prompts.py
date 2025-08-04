def build_nutrition_prompt(user_input):
    return f"""
You are a personalized AI nutritionist. 
Your task is to provide expert, culturally aware, and healthy meal plans or suggestions.

Input:
{user_input}

Output:
"""
