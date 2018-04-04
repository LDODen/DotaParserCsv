import json
import requests
import unicodecsv
import os

page_link = "https://api.opendota.com/api/proMatches"
m_id_link = "https://api.opendota.com/api/matches/"
page = requests.get(page_link)
print(type(page.content))

path = os.getcwd()
csv_filename = os.path.join(path, 'matches.csv')
fh = open(csv_filename, "wb")
csv_out = unicodecsv.writer(fh, delimiter=';', encoding='utf-8')

parsed_string = json.loads(page.content)

for item in parsed_string:
    csv_out.writerow(item.values())
    # m_id = item.get('match_id')
    # new_link = m_id_link + str(m_id)
    # m_id_page = requests.get(new_link)
    # parsed_m_id_page = json.loads(m_id_page.content)
    # chat = parsed_m_id_page.get('chat')
    # m_id_filename = os.path.join(path, str(m_id) + '.csv')
    # f_m_id = open(m_id_filename, "wb")
    # f_m_id_writer =  unicodecsv.writer(f_m_id, delimiter=';', encoding='utf-8')
    # for it in chat:
    #     f_m_id_writer.writerow(it.values())
    # f_m_id.close()

fh.close()
