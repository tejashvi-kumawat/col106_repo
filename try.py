import google.generativeai as genai
from PIL import Image
import base64

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        raise Exception(f"Error encoding image: {str(e)}")

def analyze_image(api_key, image_path, prompt):
    try:
        genai.configure(api_key=api_key)
        encoded_image = encode_image(image_path)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([
            {
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/png",
                            "data": encoded_image
                        }
                    },
                    {
                        "text": prompt
                    }
                ]
            }
        ])
        return response.text, model
    except Exception as e:
        raise Exception(f"Error analyzing image: {str(e)}")

if __name__ == "__main__":
    api_key = "AIzaSyCRBXjU-Gm1yWcYFtxYWO2DYGv9y_XYXlk"
    prompt = "Solve this Physics Question which is in image, and give me correct option with step by step solution"
    
    for i in range(0, 45):
        try:
            image_path = f"Screenshot ({13464+i}).png"
            print(f"\nAnalyzing image {i}...")
            
            result, model = analyze_image(api_key, image_path, prompt)
            chat_session = model.start_chat(history=[
                {
                    "role": "user",
                    "parts": ["hii\n"]
                },
                {
                    "role": "model",
                    "parts": ["Hi there! How can I help you today?\n"]
                }
            ])
            
            final_response = chat_session.send_message(
                f"analyse the {result} and then return only correct option and final answer in the format [correction option: correct Answer] and don't write anything from your side"
            )
            print(f"Question {i} Answer: {final_response.text}")
            
        except Exception as e:
            print(f"Error processing image {i}: {str(e)}")
            continue