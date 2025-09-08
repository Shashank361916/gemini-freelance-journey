from langchain_core.tools import tool
from datetime import date

# The @tool decorator turns this Python function into a usable tool.
@tool
def get_current_date() -> str:
    """
    Returns the current date.
    Use this tool whenever you are asked about today's date.
    """
    return str(date.today())

# Test the tool
if __name__ == "__main__":
    print("Tool Name:", get_current_date.name)
    print("Tool Description:", get_current_date.description)
    result = get_current_date.invoke({})
    print("Result:", result)