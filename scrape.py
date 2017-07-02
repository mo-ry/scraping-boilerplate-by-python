import os
import time
import settings
import MySQLdb
import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

def scrape():
    user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36")

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = user_agent
    dcap["phantomjs.page.settings.javascriptEnabled"] = True

    driver = webdriver.PhantomJS(
                service_log_path=os.path.devnull,
                executable_path="./phantomjs",
                service_args=['--ignore-ssl-errors=true', '--load-images=no', '--ssl-protocol=any'],
                desired_capabilities=dcap
              )

    driver.get(settings.LOGIN_URL)

    input_username = driver.find_element_by_xpath(settings.LOGIN_XPATH)
    input_username.clear()
    input_username.send_keys(settings.USERNAME)

    input_password = driver.find_element_by_xpath(settings.PASSWORD_XPATH)
    input_password.clear()
    input_password.send_keys(settings.PASSWORD)

    login_form = driver.find_element_by_xpath(settings.FORM_XPATH)
    login_form.submit()

    driver.get(settings.TARGET_URL)
    time.sleep(5)

    next_page_link = driver.find_element_by_xpath(settings.NEXT_PAGE_LINK_XPATH)

    items = []
    while next_page_link:
        next_page_link = driver.find_element_by_xpath(settings.NEXT_PAGE_LINK_XPATH)
        targets = driver.find_elements_by_xpath(settings.TARGET_XPATH)

        if targets:
            for i in range(len(targets)):
                if targets[i].text: items.append((targets[i].text))
        else:
            print("No target element")

        next_page_link.click()
        time.sleep(10)

    driver.close()
    driver.quit()

    return items

def save(items):
    conn = MySQLdb.connect(
        user = settings.DB_USER,
        passwd = settings.DB_PASSWORD,
        host = settings.DB_HOST,
        db = settings.DB_NAME,
        use_unicode = True,
        charset = "utf8"
    )
    cursor = conn.cursor()

    sql = 'CREATE TABLE IF NOT EXISTS ' + settings.TABLE_NAME + ' (id INT PRIMARY KEY AUTO_INCREMENT, key VARCHAR(255))'
    cursor.execute(sql)

    sql = 'INSERT INTO ' + settings.TABLE_NAME + ' (key) VALUES (%s)'
    cursor.executemany(sql, items)

    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    items = scrape()
    save(items)