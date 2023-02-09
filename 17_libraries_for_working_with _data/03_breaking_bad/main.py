import requests
import json
from typing import Dict, Union, List


def finder(data: List[Dict[str, Union[str, int]]]) -> Dict[str, Union[str, int]]:
    max_death = 0
    for el in data:
        if el['number_of_deaths'] > max_death:
            max_death = el['number_of_deaths']
            id_death = el
    return id_death


death_req = requests.get('https://www.breakingbadapi.com/api/deaths')
death_data = json.loads(death_req.text)

result = finder(death_data)
print(result)

with open('death_test.json', 'w') as file:
    json.dump(result, file, indent=4)
