from pprint import pprint

import requests
import pandas as pd

headers = {
    'X-KL-Ajax-Request': 'Ajax_Request',
    'Referer': 'https://www.ebooks.com/en-ru/subjects/archaeology/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
    'sec-ch-ua-platform': '"Windows"',
    'Content-Type': 'application/json',
}

params = (
    ('subjectId', '452'),
    ('pageNumber', '1'),
    ('countryCode', 'RU'),
)

response = requests.get('https://www.ebooks.com/api/search/subject/', headers=headers, params=params)

pprint(response.json().keys())