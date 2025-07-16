from selenium.common import exceptions


class reader(object):

    """docstring for Logger"""

    def __init__(self, e):
        super(reader, self).__init__()
        self.e = e

    def error_lookup(e):
        if e.__class__ is exceptions.ElementNotSelectableException:
            msg = ("ElementNotSelectableException -"
                   " Thrown when trying to select an unselectable element."
                   " For example, selecting a ‘script’ element.")
        elif e.__class__ is exceptions.ElementNotVisibleException:
            msg = ("ElementNotVisibleException -"
                   " Thrown when an element is present on the DOM,"
                   " but it is not visible,"
                   " and so is not able to be interacted with.")
        elif e.__class__ is exceptions.ErrorInResponseException:
            msg = e.msg
        elif e.__class__ is exceptions.ImeActivationFailedException:
            msg = ("ImeActivationFailedException -"
                   " Thrown when activating an IME engine has failed.")
        elif e.__class__ is exceptions.ImeNotAvailableException:
            msg = ("ImeNotAvailableException -"
                   " Thrown when IME support is not available."
                   " This exception is thrown for every IME-related method"
                   " call if IME support is not available on the machine.")
        elif e.__class__ is exceptions.InvalidCookieDomainException:
            msg = ("Thrown when attempting to add a cookie under"
                   " a different domain than the current URL.")
        elif e.__class__ is exceptions.InvalidElementStateException:
            msg = "Invalid Element State"
        elif e.__class__ is exceptions.InvalidSelectorException:
            msg = ("InvalidSelectorException -"
                   " Thrown when the selector which is used to find an element"
                   " does not return a WebElement. Currently this only happens"
                   " when the selector is an xpath expression and it is either"
                   " syntactically invalid (i.e. it is not a xpath expression)"
                   " or the expression does not select WebElements"
                   " (e.g. “count(//input)”).")
        elif e.__class__ is exceptions.InvalidSwitchToTargetException:
            msg = ("InvalidSwitchToTargetException -"
                   " Thrown when frame or window target"
                   " to be switched doesn’t exist.")
        elif e.__class__ is exceptions.MoveTargetOutOfBoundsException:
            msg = ("MoveTargetOutOfBoundsException -"
                   " Thrown when the target provided to the"
                   " ActionsChains move() method is invalid,"
                   " i.e. out of document.")
        elif e.__class__ is exceptions.NoAlertPresentException:
            msg = ("NoAlertPresentException -"
                   " Thrown when switching to no presented alert."
                   " This can be caused by calling an operation on the Alert()"
                   " class when an alert is not yet on the screen.")
        elif e.__class__ is exceptions.NoSuchAttributeException:
            msg = ("NoSuchAttributeException -"
                   " Thrown when the attribute of element could not be found."
                   " You may want to check if the attribute exists in the"
                   " particular browser you are testing against."
                   " Some browsers may have different"
                   " property names for the same property."
                   " (IE8’s .innerText vs. Firefox .textContent)")
        elif e.__class__ is exceptions.NoSuchElementException:
            msg = ("NoSuchElementException -"
                   " Thrown when element could not be found.")
        elif e.__class__ is exceptions.NoSuchFrameException:
            msg = ("NoSuchFrameException -"
                   " Thrown when frame target to be switched doesn’t exist.")
        elif e.__class__ is exceptions.NoSuchWindowException:
            msg = ("NoSuchWindowException -"
                   " Thrown when window target to be switched doesn’t exist.")
        elif e.__class__ is exceptions.RemoteDriverServerException:
            msg = "Remote Driver Server Exception"
        elif e.__class__ is exceptions.StaleElementReferenceException:
            msg = ("StaleElementReferenceException -"
                   " Thrown when a reference to an element is now “stale”."
                   " Stale means the element no longer appears on"
                   " the DOM of the page.")
        elif e.__class__ is exceptions.TimeoutException:
            msg = ("TimeoutException -"
                   " Thrown when a command does not"
                   " complete in enough time.")
        elif e.__class__ is exceptions.UnableToSetCookieException:
            msg = ("UnableToSetCookieException -"
                   " Thrown when a driver fails to set a cookie.")
        elif e.__class__ is exceptions.UnexpectedAlertPresentException:
            msg = ("UnexpectedAlertPresentException -"
                   " Thrown when an unexpected alert is appeared."
                   " Usually raised when when an expected modal is blocking"
                   " webdriver form executing any more commands.")
        elif e.__class__ is exceptions.UnexpectedTagNameException:
            msg = ("UnexpectedTagNameException -"
                   " Thrown when a support class did not get"
                   " an expected web element.")
        elif e.__class__ is exceptions.WebDriverException:
            msg = "Base webdriver exception."
        else:
            msg = "Unknown error."

        return msg
