# tools.py

def add(a: int, b: int):
    return a + b


def multiply(a: int, b: int):
    return a * b


def get_weather(city: str):
    return f"Weather in {city}: Sunny, 28°C"


# TOOL REGISTRY (VERY IMPORTANT)
TOOLS = {
    "add": add,
    "multiply": multiply,
    "get_weather": get_weather,
}