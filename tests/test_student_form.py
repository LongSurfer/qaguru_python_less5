from selene import command
from selene.support.conditions import have, be
from selene.support.shared import browser

from demoqa_tests.utils import resource


def test_register_student():
    # Act
    browser.open('automation-practice-form')
    # input student data
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Evans')
    browser.element('#userEmail').type('my@mail.net')
    browser.all('.custom-radio').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('0001230067')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element(f'[value="{2000}"]').click()
    browser.element('.react-datepicker__month-select').element(f'[value="{0}"]').click()
    browser.element('.react-datepicker__day--001').click()
    """
    # Alternative method:
    browser.element('#dateOfBirthInput').perform(command.js.set_value('01 January 2000'))
    """
    # hobby
    browser.element('#subjectsInput').type('Computer').press_enter()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Music')).click()
    # upload file
    browser.element('#uploadPicture').send_keys(resource('dev_godzillas.png'))
    # address
    browser.element('#currentAddress').type('Indonesia, Bali, Kuta')
    browser.element('#state').element('input').type('NCR').press_tab()
    browser.element('#city').element('input').type('Delhi').press_tab()
    # submit
    browser.element('#submit').perform(command.js.click)

    # Assert
    def table_data(index):
        return browser.element('.modal-dialog').all("table tr").all('td')[index]

    table_data(1).should(have.exact_text("Alex Evans"))
    table_data(3).should(have.exact_text("my@mail.net"))
    table_data(5).should(have.exact_text("Male"))
    table_data(7).should(have.exact_text("0001230067"))
    table_data(9).should(have.exact_text("01 January,2000"))
    table_data(11).should(have.exact_text("Computer Science, English"))
    table_data(13).should(have.exact_text("Sports, Reading, Music"))
    table_data(15).should(have.exact_text("dev_godzillas.png"))
    table_data(17).should(have.exact_text("Indonesia, Bali, Kuta"))
    table_data(19).should(have.exact_text("NCR Delhi"))
    # browser.element('.modal-dialog').all("table tr").all('td')[1].should(have.exact_text("Alex Evans"))


