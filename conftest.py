import pytest
from selenium import webdriver

# Фикстура для добавления опций командной строки
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help='select language i.e. ru/en/es/ etc')

# Фикстура для запуска браузера
@pytest.fixture(scope="function")
def browser(request):
    # Выводим сообщение о запуске браузера
    print("\nstart browser for test..")
    # Получаем значения параметров командной строки
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    # Устанавливаем опции браузера Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Максимизируем окно браузера
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # Устанавливаем языковые настройки
    # Создаем профиль для браузера Firefox и устанавливаем языковые настройки
    ff_profile = webdriver.FirefoxProfile()
    ff_profile.set_preference("intl.accept_languages", user_language)
    browser = None
    # В зависимости от выбранного браузера запускаем соответствующий браузер
    if browser_name in ('Chrome', 'chrome'):
        print('Launch Chrome browser ..........')
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name in ('Firefox', 'firefox'):
        print('Launch Firefox browser ..........')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser  # Предоставляем объект браузера в тестовую функцию
    # Выводим сообщение о закрытии браузера
    print("\nquit browser..")
    browser.quit()  # Закрываем браузер после завершения выполнения тестовой функции




  ### Вызов в командной стоке: pytest -v --tb=line --reruns 1 --browser_name=firefox --language=ru file_name.py