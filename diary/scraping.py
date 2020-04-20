from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

# ブラウザのオプションを格納する変数をもらってきます。
options = Options()

options.add_argument('--headless')

# ブラウザを起動する
driver = webdriver.Chrome(chrome_options=options)

# ブラウザでアクセスする
try:
    driver.get("https://ja-jp.facebook.com/ads/library/?active_status=all&ad_type=all&country=JP&impression_search_field=has_impressions_lifetime&view_all_page_id=146309392069492")

    driver.implicitly_wait(10)

    height = driver.execute_script("return document.body.scrollHeight")

    # ループ処理で少しづつ移動
    for x in range(1, height):
        driver.execute_script("window.scrollTo(0, " + str(50*x) + ");")

    name = driver.find_element_by_css_selector('._8wh_').text
    date1 = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]').text
    date2 = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]').text

    print(name)
    print(date1)
    print(date2)

    if len(driver.find_elements_by_css_selector('._7gn2')) > 0:
        print(driver.find_element_by_css_selector('._7gn2').text)
        t = driver.find_elements_by_css_selector(('._7owt'))
        Lists = []
        for s in t:
            if len(s.find_elements_by_css_selector('._7jys')) > 0:
                image = s.find_element_by_css_selector('._7jys')
                text = s.find_element_by_css_selector('._7jyr')
                k_id = s.find_element_by_css_selector('._4rhp')
                day = s.find_element_by_css_selector('._7jwu')
                print(k_id.text)
                print(day.text)
                print(text.text)
                print(image.get_attribute('src'))
                list = {
                    "k_id": k_id.text,
                    "day": day.text,
                    "text": text.text,
                    "image": image.get_attribute('src'),
                }
                Lists.append(list)
            else:
                print('なし')



    else:
        print('なし')


finally:
    driver.quit()
    print(Lists)


