Installing Polyglot on Windows
---
1. ICU
- Download ICU from ```https://github.com/unicode-org/icu/releases``` in the Assets dropdown of the selected release. Preferably choose a mature release, not the latest (2nd/3rd latest)
- Download filename similar to `icu4c-74_2rc-WinARM64-MSVC2022.zip`. Here, substitute `74_2` with the version ypu are downloading and `ARM64` with your system specification.
- Extract your zip file into any folder, preferably 'Program Files/ICU'
- Edit your system environment variables to add another path variable: `path/to/icu4c/bin` (or bin64)
- Confirm success by running command `icuinfo` in any folder

2. PyICU
- Download PyICU from ```https://github.com/cgohlke/pyicu-build/releases``` in the Assets dropdown of the selected release. Preferably choose a mature release, not the latest (2nd/3rd latest)
- Download filename similar to: `PyICU-2.13-cp311-cp311-win_amd64.whl` into `arabic-eval/downloads`. Here, substitute `2.13` with the version you are downloading, `311` with the version of Python you are using and `amd64` with your processor.
- Run this set of commands in the terminal of arabic-eval:
```
pip install /downloads/your_pyicu_filename.whl
```
- Confirm success by running command `pip show pyicu`

3. PyCLD2
- Download PyCLD2 in your terminal via the command set
```
git clone https://github.com/aboSamoor/pycld2/ /arabic-eval/downloads
cd /download/pycld2
pip install .
cd ..
cd ..
```
- Confirm success by running command `pip show pycld2`

4. Polyglot
- Download PyCLD2 in your terminal via the command set 
```
git clone https://github.com/aboSamoor/polyglot/ /arabic-eval/downloads
cd /downloads/polyglot
pip install .
cd ..
cd ..
```
- Confirm success by running command `pip show polyglot`

Your final directory should look like this:
```
arabic-eval/
  |-downloads/
  |  |-polyglot/
  |  |-pycld2/
  |  L-your_pyicu_filename.whl
  |-env/
  |-metrics/
  |  |-__init__.py
  |  |-character_metrics.py
  |  |-io_metrics.py
  |  |-paragraph_metrics.py
  |  |-response_metrics.py
  |  |-sentence_metrics.py
  |  L-word_metrics.py
  |-__init__.py
  |-.env
  |-.env-sample
  |-.gitignore
  |-app.log
  |-architecture.md
  |-async_scheduler.py
  |-evaluator.py
  |-input_handler.py
  |-main.py
  |-README.md
  |-requirements.txt
  |-settings.py
  |-setup.sh
  L-utils.py
```