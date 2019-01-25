from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome
import time


def get_adreses():
    URL = 'https://www.myscore.ru/khl/results/'
    browser = Chrome()
    browser.get(URL)
    time.sleep(10)
    browser.find_element_by_id('tournament-page-results-more').click()
    time.sleep(3)
    browser.find_element_by_id('tournament-page-results-more').click()
    time.sleep(3)
    browser.find_element_by_id('tournament-page-results-more').click()
    time.sleep(3)
    browser.find_element_by_id('tournament-page-results-more').click()
    time.sleep(3)
    browser.find_element_by_id('tournament-page-results-more').click()
    time.sleep(3)
    html = browser.page_source
    soup = str(BeautifulSoup(html, 'html.parser'))
    #print(soup.prettify())
    browser.close()
    return soup

#get_adreses()


def get_html():
    html = get_adreses()
    soup = BeautifulSoup(html)
    table = soup.find('table', {'class': 'hockey'})
    ids = table.findAll('tr')
    result = []
    for id in ids:
        result.append(id.get('id'))
    result = result[1:]
    links = []
    for word in result:
        links.append(word[4:])
    return links



def get_teams():
    links = get_html()
    my_file = open("/home/mikhail/PycharmProjects/hokk/teams.txt", "w")
    for link in links:
        url = 'https://www.myscore.ru/match/' + link + '/#match--statistics;0'
        request = requests.get(url)
        soup = BeautifulSoup(request.text)
        teams = soup.find_all('div', {'class': 'tname__text'})
        teams_list = []
        for team in teams:
            teams_list.append((team.text).strip())
        my_file.write(str(teams_list) + '\n')
    my_file.close()

get_teams()

"""

def get_statistics(links):
    #links = get_html()
    with    open("/home/mikhail/PycharmProjects/hokk/first_team_shots.txt", "a") as first_team_shots_file, \
            open("/home/mikhail/PycharmProjects/hokk/first_team_rejects.txt", "a") as first_team_rejects_file, \
            open("/home/mikhail/PycharmProjects/hokk/second_team_shots.txt", "a") as second_team_shots_file, \
            open("/home/mikhail/PycharmProjects/hokk/second_team_rejects.txt", "a") as second_team_rejects_file, \
            open("/home/mikhail/PycharmProjects/hokk/data.txt", "a") as data_file:
        for link in links:
            url = 'https://www.myscore.ru/match/' + link + '/#match--statistics;0'
            browser = Chrome()
            browser.get(url)
            time.sleep(5)
            browser.find_element_by_id('a-match-statistics').click()
            time.sleep(3)
            html = browser.page_source
            soup = BeautifulSoup(html)
            first_team = soup.find_all('div', {'class': 'statText statText--homeValue'})
            first_team_list = []
            for num in first_team:
                #print(num.text)
                first_team_list.append((num.text).strip())
            first_team_result_shot_list = []
            first_team_result_shot_list.append(first_team_list[15])
            first_team_result_shot_list.append(first_team_list[30])
            first_team_result_shot_list.append(first_team_list[45])
            first_team_shots_file.write(str(first_team_result_shot_list) + '\n')
            first_team_result_reject_list = []
            first_team_result_reject_list.append(first_team_list[18])
            first_team_result_reject_list.append(first_team_list[33])
            first_team_result_reject_list.append(first_team_list[48])
            first_team_rejects_file.write(str(first_team_result_reject_list) + '\n')

            second_team = soup.find_all('div', {'class': 'statText statText--awayValue'})
            second_team_list = []
            for num2 in second_team:
                #print(num2.text)
                second_team_list.append((num2.text).strip())
            second_team_result_shot_list = []
            second_team_result_shot_list.append(second_team_list[15])
            second_team_result_shot_list.append(second_team_list[30])
            second_team_result_shot_list.append(second_team_list[45])
            second_team_shots_file.write(str(second_team_result_shot_list) + '\n')
            second_team_result_reject_list = []
            second_team_result_reject_list.append(second_team_list[18])
            second_team_result_reject_list.append(second_team_list[33])
            second_team_result_reject_list.append(second_team_list[48])
            second_team_rejects_file.write(str(second_team_result_reject_list) + '\n')

            dates = soup.find_all('div', {'class': 'info-time mstat-date'})
            data_list = []
            for date in dates:
                # print(shot.text)
                data_list.append((date.text).strip())
                #print(data_list)
            data_file.write(str(data_list) + '\n')
            browser.close()


get_statistics(get_html())

"""