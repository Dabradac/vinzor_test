import time
import pytest
from selenium.webdriver.common.by import By
import pytest_check as check


@pytest.mark.usefixtures('setup')
class TestMain:

    def test_section(self):
        self.driver.get('https://mnogosna.ru/tipy-matrasov/')
        self.driver.find_element(By.XPATH, '//*[@id="page-header"]/div[2]/div/div/div[4]/div[1]/input').click()
        self.driver.find_element(By.XPATH, '//*[@id="search-input"]').send_keys('матрас аскона 160х200')
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, '//*[@id="slinks-popular-query"]/a[1]/div')
        check.equal(element.text, 'Топперы Аскона 160х200')
        element.click()
        check.equal(self.driver.current_url, 'https://mnogosna.ru/tipy-matrasov/topper/ascona/160x200/')

    def test_picture(self):
        self.driver.get('https://mnogosna.ru/tipy-matrasov/')
        self.driver.find_element(By.XPATH, '//*[@id="page-header"]/div[2]/div/div/div[4]/div[1]/input').click()
        self.driver.find_element(By.XPATH, '//*[@id="search-input"]').send_keys('матрас аскона 160х200')
        picture = self.driver.find_element(By.XPATH,
                                           '//*[@id="slinks-popular-goods"]/div/div/div[1]/div/a[1]/picture/img')
        check.equal(picture.get_attribute('src'),
                    'https://mnogosna.ru/upload/iblock/afe/zqj01rmc90p1v2qk05f8m0dnxorou6lk/thumbs/1x/product_img_163.jpg')
        name = self.driver.find_element(By.XPATH, '//*[@id="slinks-popular-goods"]/div/div/div[1]/div/a[2]')
        check.equal(name.text, 'Матрас Аскона Фитнес Формула 160x200')
