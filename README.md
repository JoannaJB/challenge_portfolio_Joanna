### **Task 1: Konfiguracja oprogramowania**

#### **Subtask 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?**

Cześć :wave:, mam na imię Asia i mam ponad roczne doświadczenie w testowaniu manualnym i w szukaniu bugów :bug:. W mojej
firmie od paru miesięcy zajmuje się również testami automatycznymi.
To było dla mnie spore wyzwanie, ale zarazem też ekscytujące, bo udało mi się przyswoić sporo wiedzy i każdy "PASSED"
wywołuje uśmiech na mojej twarzy.
Choć właśnie "FAILED" najwięcej uczą i motywują do szukania rozwiązania.

Testy piszę w jezyku Python :snake: za pomocą Selenium, więc to idealne szkolenie dla mnie :smiley:. Jestem jedynym
testerem w zespole, więc nie mam z kim się skonsultować i wymienić wiedzą.
Choć współpraca z programistami też jest fajna :wink:. Chciałabym usystematyzować wiedzę np. poznać lepsze praktyki
tworzenia lokatorów i dowiedzieć się nowych rzeczy, tj. raporty w testach automatycznych.
Mam nadzieję, że dzięki kursowi nauczę się pisać lepszej jakości testy, które pomogą mi w przyszłości zastąpić część
testów manualnych.
Bardzo cieszę się na ten kurs i jestem zmotywowana do zdobywania nowych informacji, jak również sprawdzenie moich
dotychczasowych umiejętności :muscle::woman_student:.

### **Task 2: Selektory**

#### **Substask 2: Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na
stronie logowania.**

***Przykładowe selektory XPATH***

***:construction:1. Login::construction:***

- //*[@id='login']
- //input[@id='login']
- //input[@name='login']
- //input[@type='text'][contains(@class,'MuiInputBase-input')]
- //div[@class='MuiCardContent-root']//input[@id='login']
- /html/body/div[1]/form/div/div[1]/div[1]/div/input

***:construction:2. Hasło::construction:***

- //*[@id='password']
- //input[@id='password']
- //input[@name='password']
- //input[@type='password'][contains(@class,'MuiInput-input')]
- //div[@class='MuiCardContent-root']//input[@id='password']

***:construction:3. Przypomnij hasło::construction:***

- //*[@id="__next"]//a
- //a[contains(@class,'MuiTypography-root')]
- //div[@class='MuiCardContent-root']//a
- //a[text()='Remind password']

***:construction:4. Wybór języka::construction:***

- //div[@role='button']
- //*[@id="__next"]//div[contains(@class,'MuiSelect-select')]
- //div[@class='MuiCardActions-root']//div[@role='button']
- //div[@class='MuiCardActions-root']//div[contains(@class,'MuiSelect-root')]
- //div[text()='Polski'] | //div[text()='English']

***:construction:5. Button Zaloguj::construction:***

- //span[@class='MuiButton-label']
- //span[text()='Zaloguj'] | //span[text()='Sign in']
- //div[@class='MuiCardActions-root']//span
- //button[contains(@class,'MuiButtonBase-root')]//span

### **Task 3: Pierwszy test automatyczny i asserty**

Umiejętności nabyte, dzięki zadaniu:\
✅ lepsze poznanie frameworka Selenium,\
✅ klikanie w elementy na stronie,\
✅ wypełnianie pola tekstem,\
✅ wykorzystanie assert title,\
✅ uruchomienie testu.

### **Task 4: Refactor, debugger i przypadki testowe**

Umiejętności nabyte, dzięki zadaniu:\
✅ wykonanie refactoru naszego kodu,\
✅ poznanie debuggera,\
✅ poznanie dobrych praktyk w pisaniu przypadków testowych,\
✅ zautomatyzowanie strony internetowej na podstawie swoich TC.

### **Task 5: Robot framework**

Umiejętności nabyte, dzięki zadaniu:\
✅ poznanie Smoke Tests,\
✅ konfigurowanie Suite Test,\
✅ poznanie nowego framework RobotFramework,\
✅ wygenerowanie automatycznego raportu z testów

---

### Opis projektu

Strona, którą testuje to: https://scouts-test.futbolkolektyw.pl/en/login?redirected=true. Jest to platforma do
zarządzania szkółką piłkarską. W moich przypadkach testowych sprawdzam funkcjonalność logowania, wylogowywania,
sprawdzania tytułów, nagłówków, dodawanie i edytowanie graczy, dodawanie meczy.

### Wymagania

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white)![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Testy automatyczne napisane są w języku Python wykorzystują framework Selenium. Selenium to popularny zestaw narzędzi do
testowania aplikacji internetowych. Biblioteka pozwala na automatyzację przeglądarek internetowych, takich jak Chrome,
Firefox czy Edge, umożliwiając symulację akcji użytkownika i weryfikację stanu aplikacji. W języku Python, do
automatyzacji przeglądarek używam biblioteki selenium.webdriver.
Aby rozpocząć testowanie z użyciem Selenium, należy mieć zainstalowany sterownik przeglądarki internetowej, na przykład
ChromeDriver dla przeglądarki Google Chrome. Sterownik ten umożliwia Selenium interakcję z przeglądarką internetową.
Używam oprogramowania Linux, w wersji Ubuntu 20.04, przedstawiona instalacja jest, dla tego oprogramowania.

### Instalacja

Projekt wymaga wersji Pythona 3.11.3. Jeśli nie masz zainstalowanej wersji Pythona, możesz ją zainstalować za pomocą
menedżera pakietów apt-get:

```python
$ sudo apt-get update
$ sudo apt-get install python3.11
```

Zainstalowanie Selenium z wykorzystaniem polecenia pip:

```python
$ pip install Selenium
```

Projekt wykorzystuje framework Pytest do uruchamiania testów automatycznych. Aby zainstalować Pytest, użyj polecenia
pip:

```python
$ pip install pytest
```

Projekt wymaga ChromeDriverManager, który jest menedżerem sterowników przeglądarek dla biblioteki Selenium. Aby
zainstalować ChromeDriverManager, użyj polecenia pip:

```python
$ pip install webdriver-manager
```

Projekt wykorzystuje plugin pytest-html do generowania raportów HTML z wynikami testów. Aby zainstalować pytest-html,
użyj polecenia pip:

```python
$ pip install pytest-html
```

### Uruchomienie testów

Uruchomienie scenariuszy w terminalu:

```python
$ pytest test_cases
```

Aby uzyskać raport z testów:

```python
$ pytest test_cases --html=reports/<nazwa raportu>.html --self-contained-html
```

Raport można otworzyć w przeglądarce internetowej

---
Link do Dysku Google:
https://drive.google.com/drive/folders/12hQqeokJdSm8Ql3apCYTgB7WJDWz-Yzp?usp=sharing
