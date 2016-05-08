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
    scrape_fields = raw_input("Class of fields to scrape: ")

    # Add info to site tables
    add_to_table("Pages", fields=("PageName", "PageURL", "UserElement",
                                  "UserName", "PasswordElement", "Password", "SubmitElement",
                                  "ScrapeFields"),
                 values=(page_name, page_url, user_element, password_element,
                         user_name, password, submit_element, scrape_fields))


def login_to_page(driver, row):
    """Login to page using page info from page specific db entry"""

    # Open page in browser
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


def scrape_elements(driver, row):
    """Select and scrape page elements from page"""

    # initialize list for scraped data
    scrape_list = []


    scrape_list.append(driver.find_elements_by_class_name("bodytext"))
    print "scrape_list= "
    print scrape_list
    return scrape_list


def scrape_all_pages():
    """Iterate through pages and scrape all fields"""

    # initialize driver
    driver = webdriver.Firefox()

    # connect to db and read site info
    with conn as c:

        # dynamically scrape elements based on page data
        for row in select_from_table("Pages", "*"):
            login_to_page(driver, row)
            data = scrape_elements(driver, row)

    driver.close()
    driver.quit()
    return data

if __name__ == "__main__":
    #add_page_to_db()
    print scrape_all_pages()