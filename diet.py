from ai_engine import ask_ai

def generate_diet(pcos_type):

    prompt = f"""
    Create a personalized daily diet chart for
    {pcos_type} PCOS.

    Include:
    Breakfast
    Lunch
    Evening Snack
    Dinner
    Water Intake
    """

    return ask_ai(prompt)