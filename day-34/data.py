import requests

def get_questions():
    params = {"amount":10,"type":"boolean"}
    response = requests.get("https://opentdb.com/api.php", params= params)
    data = response.json()['results']
    return data

question_data = get_questions()
