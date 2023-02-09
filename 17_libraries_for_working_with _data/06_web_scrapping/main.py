import requests
import re


web_code_req = requests.get('http://www.columbia.edu/~fdc/sample.html')

subtitles_codes = re.findall(r'<h3 id=\".{0,30}\">.{0,100}</h3>', web_code_req.text)

cut_subtitles_codes = [re.sub(r'<h3 id=\".{0,30}\">', '', i_sub_code) for i_sub_code in subtitles_codes]

subtitles = [re.sub(r'</h3>', '', i_sub) for i_sub in cut_subtitles_codes]
print(subtitles)
