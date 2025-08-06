from bs4 import BeautifulSoup as bs
import requests
import time
print("At least how many wins a team should have")
wins = int(input())
print("At most how many losses a team should have")
losses = int(input())
print(f"Filtering the data for teams with at least {wins} wins and at most {losses} losses")
def find_team():
    html_text = requests.get('https://www.scrapethissite.com/pages/forms/').text
    soup = bs(html_text, 'lxml')
    teams = soup.find_all('tr', class_='team')
    for team in teams:
            team_wins = team.find('td', class_='wins').text.strip()
            if int(team_wins) >= wins:
                team_losses = team.find('td', class_='losses').text.strip()
                team_name = team.find('td', class_='name').text.strip()
                if int(team_losses) <= losses:
                    with open(f'work/{team_name}.txt','w') as f:
                        f.write(f"{team_name}\n")
                        f.write(f"{team_wins}\n")
                        f.write(f"{team_losses}\n")
                    print(f"File saved: {team_name}")
if __name__ == '__main__':
    while True:
        find_team()
        wait = 10
        print("Waiting for 10 minutes...")   
        time.sleep(wait * 60)              