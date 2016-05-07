from selenium import webdriver
import time
from data import *


def wait_function():
    """Allow page to load. Refactor as needed"""
    time.sleep(5)


def add_page_to_db():
    """configure data for new site to scrape"""

    # Get site info from raw input
    page_name = raw_input("Name of page: ")
    page_url = raw_input("Url of page: ")
    user_element = raw_input("Element ID of username field: ")
    user_name = raw_input("Username for {0}: ".format(page_name))
    password_element = raw_input("Element ID of password field: ")
    password = raw_input("Password for {0}: ".format(page_name))
    submit_element = raw_input("Submit element for {0}: ".format(page_name))

    # Add info to site tables
    add_to_table("Pages", fields=("PageName", "PageURL", "UserElement",
                                  "UserName", "PasswordElement", "Password", "SubmitElement"),
                 values=(page_name, page_url, user_element, password_element,
                         user_name, password, submit_element))


def return_page_driver():
    """Login to page using page info from page specific db"""

    for row in select_from_table("Pages", "*"):
        # Open page in browser
        driver = webdriver.Firefox()
        driver.get(row[1])

        # allow page load
        wait_function()
        # wait_function()

        # enter username
        uname_element = driver.find_element_by_id(row[2])
        uname_element.send_keys(row[4])

        # enter password and submit
        pwd_element = driver.find_element_by_id(row[3])
        pwd_element.send_keys(row[5])
        submit_element = driver.find_elements_by_class_name(row[6])
        submit_element[0].click()


if __name__ == "__main__":
    add_page_to_db()
    return_page_driver()
