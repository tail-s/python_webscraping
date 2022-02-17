from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

# # 가는 날 선택 클릭
# # browser.find_element_by_css_selector("#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div:nth-child(2) > button:nth-child(1)").click()
# browser.find_element_by_xpath("//div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 여행 갈 나라 클릭
travel_country = browser.find_elements_by_css_selector('div.tabContent_routes__laamB button')
travel_country[1].click()

# 여행 갈 나라 카테고리 클릭
category_all = browser.find_elements_by_css_selector('div.autocomplete_content__3RhAZ > section.section  button')
category_all[1].click()

# 여행 갈 나라 카테고리 안 서브 카테고리 클릭
subcategory_all = browser.find_elements_by_css_selector('div.autocomplete_list__de1dI button')
subcategory_all[0].click()

# 가는 날 클릭
browser.find_element_by_class_name('tabContent_option__2y4c6').click()
month = browser.find_elements_by_css_selector(
    'div.sc-jrsJWt.dJdFwe.awesome-calendar div.sc-kEqXSa.bAVzgZ.month')  # 11월 ~ 2022년 12월까지의 month 데이터 추출[12월추출[]]
go_weeks = month[1].find_elements_by_css_selector('table tbody tr')  # 각 주차 별 데이터  [12월 데이터 추출]
go_days = go_weeks[3].find_elements_by_css_selector('td')  # 각 일 별 데이터 추출(2주차의 일요일 ~ 월요일 데이터추출)
go_days[4].click()  # 2주차의 3번째 일 클릭
# day=days[1].find_element_by_css_selector('button')

# 오는 날 클릭
back_weeks = month[1].find_elements_by_css_selector('table tbody tr')  # 2022년 1월 1주 ~ 5주차 데이터 추출
back_days = back_weeks[4].find_elements_by_css_selector('td')  # 2022년 5주차의 일요일~월요일 데이터 추출
back_days[1].click()

# 항공권 검색하기
Filght_click = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button')
Filght_click.click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div[3]/div[1]/div")))
    # 첫 번째 결과 출력
    print(elem.text)
finally:
    browser.quit()
