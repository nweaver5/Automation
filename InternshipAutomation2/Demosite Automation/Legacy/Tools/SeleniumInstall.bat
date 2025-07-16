copy "chromedriver.exe" "C:\Python34\Scripts\"
copy "IEDriverServer.exe" "C:\Python34\Scripts\"
copy "selenium-server-standalone-2.46.0.jar" "C:\Python34\Scripts\"
cd C:\Python34\Scripts\
pip install --upgrade pip
pip install selenium
pip install tabulate
set path=%PATH%;C:\Python34\Scripts;
