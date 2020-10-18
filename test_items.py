link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
