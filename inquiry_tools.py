from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    return ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

@tool
def classify_inquiry_tool(inquiry: str) -> str:
    """
    Classifies a user inquiry into 'sales', 'customer_support', or 'other'.
    Use this tool first to understand the inquiry type.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0) # Use a separate LLM for classification
    prompt = f"Classify the following user inquiry into 'sales', 'customer_support', or 'other'. Respond with only the category name.\n\nInquiry:\n---\n{inquiry}\n---\nCategory:"
    response = llm.invoke(prompt)
    return response.content.strip().lower()

@tool
def draft_sales_reply_tool(inquiry: str) -> str:
    """
    Drafts a reply to a 'sales' inquiry.
    The input is the original user inquiry text.
    """
    llm = get_llm()
    prompt = f"""
    Draft a polite and professional response to the following user inquiry, which is a sales lead.
    Thank them for their interest and tell them a sales representative will contact them shortly.
    Original Inquiry: --- {inquiry} ---
    """
    response = llm.invoke(prompt)
    return response.content

@tool
def draft_support_reply_tool(inquiry: str) -> str:
    """
    Drafts a reply to a 'customer_support' inquiry.
    The input is the original user inquiry text.
    """
    llm = get_llm()
    prompt = f"""
    Draft a polite and professional response to the following user inquiry, which is a customer support issue.
    Acknowledge their issue and provide a link to the support portal: support.example.com.
    Original Inquiry: --- {inquiry} ---
    """
    response = llm.invoke(prompt)
    return response.content

@tool
def draft_other_reply_tool(inquiry: str) -> str:
    """
    Drafts a polite reply to an inquiry that is not related to sales or customer support.
    The input is the original user inquiry text.
    """
    llm = get_llm()
    prompt = f"""
    Draft a polite reply to the following user inquiry, which is not related to sales or support.
    Politely state that you cannot assist with this specific request.
    Original Inquiry: --- {inquiry} ---
    """
    response = llm.invoke(prompt)
    return response.content