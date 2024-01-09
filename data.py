class Urls:
    server = 'https://stellarburgers.nomoreparties.site'
    main_page = 'https://stellarburgers.nomoreparties.site/'
    login_page = 'https://stellarburgers.nomoreparties.site/login'
    forgot_password_page = 'https://stellarburgers.nomoreparties.site/forgot-password'
    feed_page = 'https://stellarburgers.nomoreparties.site/feed'


class Api:
    register_user = '/api/auth/register'
    user = '/api/auth/user'
    login = '/api/auth/login'
    ingredients = '/api/ingredients'
    orders = '/api/orders'


class ResetPasswordPageTestData:
    active_field_border = '2px solid'
    active_field_class = 'input_status_active'
