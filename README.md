# Configuração do setup
- JAVA: 
    1. Acessar o link e baixar do site oficial da Oracle o Java na versão 8 e em seguida instalar.
    (https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)

    2. Adicionar o path do jdk nas variáveis de ambiente.
    (JAVA_HOME = C:\Program Files\Java\jdk1.8.0_202)

    3. Adicionar diretório "C:\Program Files\Java\jdk1.8.0_202\bin" no path

- Android SDK:
    1. Acessar link com tutorial para download e instalação no android studio no windows.
    (https://developer.android.com/studio/install)

    2. Adicionar o path da pasta sdk nas variáveis de ambiente.
    (ANDROID_HOME = C:\Users\IARTES 22\AppData\Local\Android\Sdk)

    3. Abrir o Android studio e acessar o path: SDK manager> android SDK> SDK Tools

    4. Desmarcar checkbox 'Hide Obsolete Packages'

    5. Instalar os seguinte pacotes: 
    Android SDK Build-Tools, 
    Android sdk command-line Tools, 
    Android emulator,
    Android sdk platform-Tools,
    Android sdk Tools

    6. Adicionar ao path da variável de ambiente os seguintes diretórios:
    'C:\Users\IARTES 22\AppData\Local\Android\Sdk\platform-tools',
    'C:\Users\IARTES 22\AppData\Local\Android\Sdk\tools'

- Python e Nodejs:
    1. Instalar ambos e dos sites oficiais e instalar atentando para seleção dda opção para adicionar no Path
    automaticamente durante instalação, ao fim verificar se os seguinte diretórios foram adicionados no path:
    'C:\Python311\Scripts\',
    C:\Python311\,
    'C:\Program Files\nodejs\'
    
- Instalar appium globalmente pelo npm através do comando:
 "npm install -g appium"

- Instalar appium-doctor globalmente pelo npm através do comando:
 "npm install -g appium-doctor"

- Executar 'appium-doctor' no cmd para confirmar se a configuração foi concluída com sucesso

- Dentro do diretório do projeto devem ser instalados os seguintes pacotes do python, pelos comandos:
'pip install pytest',
'pip install appium-python-client'


# Execução do projeto

1- Iniciar o servidor do appium, podendo ser via interface do appium desktop ou pelo comando adequado com os endereços setados nas capabilities, no caso: 'appium -a 127.0.0.1 -p 4723'

2- Abre o emulador do android studio pelo virtual device manager ou pluga um device real com sistema operacional android

3- Instalar a APK que será testada, no device real ou emulado

4- Executar o comando "pytest budget_test.py"


# Para Projeto Final: Obter appPackage e appActivity names
    1 - Abrir emulador
    2 - Executar comando "adb shell pm list packages"
    3 - Pegar o nome completo após 'package:'
    4 - Adicionar na capabilitie de appPackage o conteúdo: 'com.blogspot.e_kanivets.moneytracker'
    5 - Executar comando 'adb logcat'
    6 - Abrir a apk no emulador
    7 - Parar o log e procurar pelo nome do appPackage
    8 - Pegar o nome que vem após a '/' 
    9 - 'com.blogspot.e_kanivets.moneytracker/.activity.record.MainActivity'
    10 - Portando o nome do appActivity será: '.activity.record.MainActivity'

# Para Execução mais eficiente dos testes:
    1 - Adicionado o marcardor para selecionar sequencia de execução pelo comando: 'pip install pytest-order'

    2 - Para executar mais de uma vez em caso de falhas desnecessárias, foi utilizado o recurso de retest pelo comando: 'pip install pytest-rerunfailures'

    3 - Os testes foram executados utilizando o comando: 'pytest TestCases.py -vv --reruns 2' para executar mais duas vezes em caso de falha.
