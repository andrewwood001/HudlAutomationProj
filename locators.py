LOGOUT_CSS_SELECTOR = 'a[href="/logout"]'
LOGIN_XPATH = '(//a[@href="/login"])[1]'
PASSWORD_XPATH = "//input[@id='password']"
EMAIL_XPATH = "//input[@id='email']"
PASSWORD_ID = 'password'
LOGIN_ID = 'logIn'
REMEMBER_ME_XPATH = '//input[@data-qa-id="remember-me-checkbox"]'
NEED_HELP_XPATH = '//a[@data-qa-id="need-help-link"]'
LOGIN_HELP_HEADLINE_XPATH = '//h2[@data-qa-id="login-help-headline"]'
PASSWORD_RESET_INPUT_XPATH = '//input[@data-qa-id="password-reset-input"]'
ACTIVE_PASSWORD_RESET_SUBMIT_BUTTON = '//button[@data-qa-id="password-reset-submit-btn" and not(@disabled)]'
DISABLED_PASSWORD_RESET_SUBMIT_BUTTON = '//button[@data-qa-id="password-reset-submit-btn" and @disabled]'
