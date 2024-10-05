import  google.generativeai as genai
import PIL.Image as Image

genai.configure(api_key='AIzaSyArqjsdlhMiOmPppbO-wzFzPwXlKJrt50s')

for i in genai.list_models():
	if 'generateContent' in i.supported_generation_methods:
		print(i.name)

# Model Configuration
model = genai.GenerativeModel('gemini-pro-vision')

img = Image.open('disease2.jpeg')
print(img)

response = model.generate_content(img)

print(response.text)