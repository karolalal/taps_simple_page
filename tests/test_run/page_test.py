import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_object import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page, \
    add_remove_page, data_picker_page, basic_auth_page, form_page, key_presses_page, drag_and_drop_page, \
    status_code_page, iFrame_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_clicked(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_data_picker_visibility(self):
        data_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(data_picker_page.date_picker_content_visible(self.driver))

    def test11_data_picker_correct_value(self):
        data_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(data_picker_page.send_correct_keys_to_input(self.driver))
        sleep(4)

    def test12_data_picker_incorrect_value(self):
        data_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(data_picker_page.send_incorrect_keys_to_input(self.driver))

    def test13_basic_auth_correct(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.send_correct_data(self.driver))
        self.assertTrue(users_page.logged_in_message_displayed(self.driver))

    def test14_basic_auth_incorrect(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.send_incorrect_data(self.driver))
        self.assertTrue(basic_auth_page.message_visible(self.driver))

    def test15_basic_auth_correct_with_return(self):
        basic_auth_page.click_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.send_correct_data(self.driver))
        self.assertTrue(users_page.logged_in_message_displayed(self.driver))
        users_page.return_main_page(self.driver)
        self.assertTrue(main_page.content_visible(self.driver))

    def test16_form_correct(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        self.assertTrue(form_page.send_correct_data(self.driver))

    def test17_form_correct_accept_alert(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        self.assertTrue(form_page.send_correct_data(self.driver))
        form_page.accept_alert(self.driver)

    def test18_form_incorrect(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        self.assertTrue(form_page.send_incorrect_data(self.driver))

    def test19_key_presses_correct_value(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visible(self.driver))
        self.assertTrue(key_presses_page.key_presses_input(self.driver))

    def test20_drag_and_drop(self):
        drag_and_drop_page.click_drag_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_content_visible(self.driver))
        self.assertTrue(drag_and_drop_page.check_drag_and_drop(self.driver))

    def test21_status_code_200(self):
        status_code_page.click_status_code_tab(self.driver)
        self.assertTrue(status_code_page.status_code_content_visible(self.driver))
        self.assertTrue(status_code_page.code_200_click(self.driver))

    def test22_status_code_305(self):
        status_code_page.click_status_code_tab(self.driver)
        self.assertTrue(status_code_page.status_code_content_visible(self.driver))
        self.assertTrue(status_code_page.code_305_click(self.driver))

    def test23_status_code_404(self):
        status_code_page.click_status_code_tab(self.driver)
        self.assertTrue(status_code_page.status_code_content_visible(self.driver))
        self.assertTrue(status_code_page.code_404_click(self.driver))

    def test24_status_code_500(self):
        status_code_page.click_status_code_tab(self.driver)
        self.assertTrue(status_code_page.status_code_content_visible(self.driver))
        self.assertTrue(status_code_page.code_500_click(self.driver))

    def test25_iframe_click_button1(self):
        iFrame_page.click_iframe_tab(self.driver)
        self.assertTrue(iFrame_page.hover_content_displayed(self.driver))
        self.assertTrue(iFrame_page.click_button1_inside_iframe(self.driver))

    def test26_iframe_click_button2(self):
        iFrame_page.click_iframe_tab(self.driver)
        self.assertTrue(iFrame_page.hover_content_displayed(self.driver))
        self.assertTrue(iFrame_page.click_button2_inside_iframe(self.driver))


if __name__ == '__main__':
    unittest.main()
