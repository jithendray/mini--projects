import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'GRE Score':2, 'TOEFL Score':9, 'University Rating' : 4, 'SOP' : 4, 'LOR ' : 4, 'CGPA' : 9.5, 'Research' : 1})

print(r.json())