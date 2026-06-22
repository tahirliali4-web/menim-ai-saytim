import google.generativeai as genai
import os

# Əgər AQ. açarını istifadə edirsənsə, bu, Service Account-dur.
# 'google-generativeai' kitabxanası bunu yox, AIza-nı istəyir.
# Amma bəlkə 'gemini-1.5-flash' yerinə 'gemini-pro' modelini yoxlayaq?

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 'gemini-1.5-flash' yerinə bunu yaz:
model = genai.GenerativeModel('gemini-pro')
