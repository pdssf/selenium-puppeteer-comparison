from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

sessionsSiteArray = [
    {
        'site': 'https://webmedia.org.br/2020/programacao-em-html/#st1',
        'year': 2020
    },
    {
    'site': 'https://webmedia.org.br/2019/programacao-em-html/#st1',
    'year': 2019
    }
]


def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def writeToFile(data, year): 
    f = open("webmedia_{}.csv".format(year), "w")
    f.write('sessao_tecnica;cadeira;artigo;autores\n')
    f.close()
    f = open("webmedia_{}.csv".format(year), "a")
    for line in data:
        f.write('{};{};{};{};\n'.format(line['name'], line['chair'], line['title'], line['author']))
    f.close()

def getData(driver: webdriver.Chrome, year):
    sessions = driver.find_element(By.XPATH, "//p[contains(., 'ST')]")
    sessionsNum = len(sessions.find_elements(By.TAG_NAME, 'a'))
    print('temos {} sessoes'.format(sessionsNum))
    sessionsNameTemp = driver.find_elements(By.TAG_NAME, 'h4')
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    sessionsName = []
    for webElement in sessionsNameTemp:
        if "ST" in webElement.text:
            sessionsName.append(webElement.text)
    sessionsArray = []
    counter = 0
    for p in paragraphs:
        pText = p.text.replace('\n', '')
        if 'chair' in pText or 'Chair' in pText:
            if counter >= len(sessionsName):
                print('fim das sessoes tecnicas')
                break
            actualSession = sessionsName[counter]
            chair = pText.replace('Chair: ', '').replace('chair: ', '')
            counter += 1
        elif counter > 0:
            title = ''
            for e in p.find_elements(By.TAG_NAME, 'strong'):
                title += e.text.replace('\n', '')
            author = pText.replace(title, '')
            sessionsArray.append({
                'name': actualSession,
                'chair': chair,
                'title': title,
                'author': author
            })
    print(sessionsArray)
    # writeToFile(sessionsArray, year)


def main():
    driver = webdriver.Chrome(options=set_chrome_options()) 
    #   driver.maximize_window()
    # driver.implicitly_wait(15)
    # for session in sessionsSiteArray:
    driver.get('https://webmedia.org.br/2019/programacao-em-html/#st1')
    getData(driver, '2019')
    exit(0)
    # driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')


if __name__ == "__main__":
    main()