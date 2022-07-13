import torch
from requests import get
get_parse_link = lambda x : f"https://sheets.googleapis.com/v4/spreadsheets/1ip5oqSH5nOld9-bbYl60xy1Rioc59I4VjMCIQDLBVOc/values/{x}?key=AIzaSyC3oDxd0Bbck8jOM-lEjH-3my3zgeLFd4U"

place_list = [-1, 0, 1, 2]

def get_question():
    question = []
    for i in place_list:
        datas = get(get_parse_link(i)).json()["values"]
        for data in datas[1:]:
            if(data[0] == ""):
                break
            question.append([data[0], data[1], torch.rand(768, dtype=torch.float), data[2]])
    return question

