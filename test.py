# tests
from playwright.sync_api import sync_playwright
from lib import Config

google_url = Config.urls['google_auth']
domain = Config.user_domain
username = '1001092'+domain
password = '22170490'
login_button = 'Go to your Google Account'
playwright = sync_playwright().start()

browser = playwright.firefox.launch(headless=False)
page = browser.new_page()
#google
page.goto(google_url)
page.get_by_label("email").fill(username)
# page.get_by_role("button", name="next").click()
page.keyboard.press('Enter')

#azure

page.get_by_placeholder("username@district65.net").fill(username)
page.keyboard.press('Enter')
# page.locator('input:has(type="email")').fill(username)
# page.locator('input:has-text("email")').fill(username)

page.get_by_label("password").fill(password)
page.keyboard.press('Enter')
try:
    page.get_by_role("button", name="No").click()
except:
    page.pause()



# <input type="email" name="loginfmt" id="i0116" maxlength="113" class="form-control ltr_override input ext-input text-box ext-text-box" aria-required="true" data-report-event="Signin_Email_Phone_Skype" data-report-trigger="click" data-report-value="Email_Phone_Skype_Entry" data-bind="
#                     attr: { lang: svr.fApplyAsciiRegexOnInput ? null : 'en' },
#                     externalCss: {
#                         'input': true,
#                         'text-box': true,
#                         'has-error': usernameTextbox.error },
#                     ariaLabel: tenantBranding.unsafe_userIdLabel || str['CT_PWD_STR_Username_AriaLabel'],
#                     ariaDescribedBy: 'loginHeader' + (pageDescription &amp;&amp; !svr.fHideLoginDesc ? ' loginDescription usernameError' : ' usernameError'),
#                     textInput: usernameTextbox.value,
#                     hasFocusEx: usernameTextbox.focused,
#                     placeholder: $placeholderText,
#                     autocomplete: svr.fIsUpdatedAutocompleteEnabled ? 'username' : null," aria-label="username@district65.net" aria-describedby="loginHeader usernameError" placeholder="username@district65.net">

