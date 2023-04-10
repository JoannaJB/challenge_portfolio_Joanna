
### **Task 1: Konfiguracja oprogramowania**
#### **Subtask 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?**

Cześć :wave:, mam na imię Asia i mam ponad roczne doświadczenie w testowaniu manualnym i w szukaniu bugów :bug:. W mojej firmie od paru miesięcy zajmuje się również testami automatycznymi.
To było dla mnie spore wyzwanie, ale zarazem też ekscytujące, bo udało mi się przyswoić sporo wiedzy i każdy "PASSED" wywołuje uśmiech na mojej twarzy. 
Choć właśnie "FAILED" najwięcej uczą i motywują do szukania rozwiązania.

Testy piszę w jezyku Python :snake: za pomocą Selenium, więc to idealne szkolenie dla mnie :smiley:. Jestem jedynym testerem w zespole, więc nie mam z kim się skonsultować i wymienić wiedzą.
Choć współpraca z programistami też jest fajna :wink:. Chciałabym usystematyzować wiedzę np. poznać lepsze praktyki tworzenia lokatorów i dowiedzieć się nowych rzeczy, tj. raporty w testach automatycznych.
Mam nadzieję, że dzięki kursowi nauczę się pisać lepszej jakości testy, które pomogą mi w przyszłości zastąpić część testów manualnych. 
Bardzo cieszę się na ten kurs i jestem zmotywowana do zdobywania nowych informacji, jak również sprawdzenie moich dotychczasowych umiejętności :muscle::woman_student:.

#### **Subtask 2: Wynik egzaminu ISTQB**
***Wynik testu:*** *8 na 14 odpowiedzi*

### **Task 2: Selektory**
#### **Substask 2: Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na stronie logowania.**

***Przykładowe selektory XPATH***

***1. Login:***
- //*[@id='login']
- //input[@id='login']
- //input[@name='login']
- //input[@type='text'][contains(@class,'MuiInputBase-input')]
- //div[@class='MuiCardContent-root']//input[@id='login']
- /html/body/div[1]/form/div/div[1]/div[1]/div/input

***2. Hasło:***
- //*[@id='password']
- //input[@id='password']
- //input[@name='password']
- //input[@type='password'][contains(@class,'MuiInput-input')]
- //div[@class='MuiCardContent-root']//input[@id='password']

***3. Przypomnij hasło:***
- //*[@id="__next"]//a
- //a[contains(@class,'MuiTypography-root')]
- //div[@class='MuiCardContent-root']//a
- //a[text()='Remind password']

***4. Wybór języka:***
- //*[@id="__next"]//div[contains(@class,'MuiSelect-select')]
- //div[@class='MuiCardActions-root']//div[@role='button']
- //div[@class='MuiCardActions-root']//div[contains(@class,'MuiSelect-root')]
- //div[text()='Polski'] | //div[text()='English'] 

***5. Button Zaloguj:***
- //span[@class='MuiButton-label']
- //span[text()='Zaloguj'] | //span[text()='Sign in']
- //div[@class='MuiCardActions-root']//span
- //button[contains(@class,'MuiButtonBase-root')]//span

###### *Super inicjatywa :sunflower:,*
###### *Pozdrawiam,*
###### *Asia*
