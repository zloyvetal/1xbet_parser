from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://ua1xbet.com/en/live/Football/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)


game_content = driver.find_element_by_id("games_content")


items = driver.find_element_by_id("games_content")

data_list = []


for scoreboard in items.find_elements_by_xpath('//*[@class="c-events__item c-events__item_game c-events-scoreboard__wrap"]'):

    command_names = [command.text for command in scoreboard.find_elements_by_class_name("c-events__team")]

    score = [sc.text.split('\n') for sc in scoreboard.find_elements_by_class_name("c-events-scoreboard__line")]
    bets = [bet.text.split('\n') for bet in scoreboard.find_elements_by_class_name("c-bets")]

    data = {
        'home': command_names[0],
        'away': command_names[1],
        'current_score': f'{score[0][0]}:{score[1][0]}'

    }
    data_list.append(data)

print(data_list)
