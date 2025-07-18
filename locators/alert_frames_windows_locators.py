from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    RESULT_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')

class AlertsPageLocators:

    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')

    SEE_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')

    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_BOX_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')

    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_BOX_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')

class FramesPageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')

    FRAME_TITLE = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class NestedFramePageLocators:

    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')

class ModalDialogsPageLocators:

    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, 'p')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')