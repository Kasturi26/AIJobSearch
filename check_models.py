import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

print("=" * 80)
print("AVAILABLE GEMINI MODELS")
print("=" * 80 + "\n")

try:
    models = genai.list_models()
    
    for idx, model in enumerate(models, 1):
        print(f"{idx}. Model Name: {model.name}")
        print(f"   Display Name: {model.display_name}")
        print(f"   Description: {model.description}")
        print(f"   Input Token Limit: {model.input_token_limit}")
        print(f"   Output Token Limit: {model.output_token_limit}")
        print(f"   Supported Methods: {model.supported_generation_methods}")
        print()
        
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("\nMake sure your GEMINI_API_KEY is set correctly in .env file")
