import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class TestGoToGmail:
    @pytest.mark.send_mail_test
    def test_send_mail(self, browsers: Chrome):
        my_username = 'workworkwork123'
        my_password = 'Qwerty123123123'
        to_username = 'workworkwork123@ukr.net'
        topic = 'Hello world123'
        message = 'How are you? 123'

        login_email = browsers.find_element(By.XPATH, "//*[@name='login']").send_keys(my_username)
        login_password = browsers.find_element(By.XPATH, "//*[@name='password']").send_keys(my_password)
        btn_next = browsers.find_element(By.XPATH, "//*[@class='Ol0-ktls jY4tHruE _2Qy_WiMj']").click()

        sleep(5)

        write_letter_xpath = browsers.find_element(By.XPATH, '//*[contains(text(),"Написати листа")]').click()
        letter_to = browsers.find_element(By.XPATH, "//*[@name='toFieldInput']").send_keys(to_username)
        topic_letter = browsers.find_element(By.XPATH, "//*[@name='subject']").send_keys(topic)
        message_letter = browsers.find_element(By.XPATH, "//*[@id='mce_0_ifr']").send_keys(message)
        btn_send = browsers.find_element(By.XPATH, "//*[@id='screens']//div[@class='controls']/button[@class='button primary send']").click()


        found_message = browsers.find_element(By.XPATH, "//*[@id='0'][span]").click()
        sleep(5)
        try:
            serch_name = browsers.find_element(By.XPATH, "//*[text()='Hello world123']")
            return True
        except NoSuchElementException:
            print('Zero element for you')
            return False



#        found_message = browsers.find_elements(By.XPATH, "//*[@id='0'][span]")
#        assert len(found_message) > 0, "No message found. Bad job"

#        for item in found_message:
#           assert item.is_displayed(), "Message item is not show on the page"
#           assert item.is_enabled(), "Found item is disabled. We cant see it"



