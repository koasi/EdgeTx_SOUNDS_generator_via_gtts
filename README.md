# EdgeTx SOUNDS 資料夾產生器 (使用 Google 文字轉語音)

這是一個使用 Google TTS 產生 EdgeTx SOUNDS 檔案的專案。

如果您熟悉 Python，您會發現它很容易使用。

---

## 準備環境

### 設置 ffmpeg 並配置環境變數

安裝 ffmpeg：

如果您還沒有安裝 ffmpeg，需要先安裝它。在 Windows 上，請按照以下步驟操作：

1. 下載 ffmpeg：
   - 訪問 https://ffmpeg.org/download.html#build-windows 並下載適合您系統的版本。

2. 將下載的檔案解壓到一個方便的位置，例如：
   ```
   C:\ffmpeg
   ```

3. 將 ffmpeg 的 bin 目錄添加到系統路徑：
   - 右鍵點擊「這台電腦」或「我的電腦」，選擇「內容」。
   - 點擊「進階系統設定」。
   - 點擊「環境變數」。
   - 在「系統變數」下，找到「Path」並點擊「編輯」。
   - 點擊「新增」，加入 ffmpeg bin 目錄的路徑，例如 `C:\ffmpeg\bin`。
   - 點擊「確定」保存所有更改。

### 下載並安裝 Python 3.10

下載路徑：https://www.python.org/downloads/windows/

**注意：** 安裝時請點選「將 Python 加入環境變數」。

### 安裝 Poetry

1. 首先，如果您還沒有安裝 pipx，請先安裝：
   ```bash
   python -m pip install --user pipx
   python -m pipx ensurepath
   ```
   完成這一步後，請關閉並重新打開您的終端。

2. 使用 pipx 安裝 Poetry：
   ```bash
   pipx install poetry
   ```

3. 驗證安裝：
   ```bash
   poetry --version
   ```
   如果安裝正確，您應該能看到 Poetry 的版本號。

4. 自動設置：
   ```bash
   poetry install 
   ```

---

## 配置您的自定義語音 wav 檔案

1. 編輯 `edgetx_audio_file_map.csv` 的 `new_wording` 欄位

2. 編輯 `config.json`：
   - `"language": "zh-tw"`
     可用語言請請參考：https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang
   - `"map_file": "edgetx_audio_files_map.csv"`
     映射的配置檔案名稱
   - `"speech_speed": 1.4`
     數字越大，語音速度越快。建議值範圍：0.5 - 2

---

## 執行

- CMD 或 Power Shell：
  ```bash
  python execute.py
  ```

- 使用 jupyter-notebook 或 jupyter-lab：
  使用 IDE 開啟 `execute.ipynb`

- 執行成功後，將會生成一個 `EdgeTx_Audio_Package\YourLanguage` 資料夾

- 將所有檔案和 SYSTEM 資料夾複製到您的 SD 卡的 `SOUNDS\en\` 目錄下，請確保 EdgeTx 語言設置為英文

---

## 注意事項

您的防毒軟體可能不信任 ffmpeg 並封鎖它。您可以選擇信任它或暫時關閉防毒軟體。





# EdgeTx SOUNDS Folder Generator by gtts (Google Text To Sound)

This is a project for generating EdgeTx SOUNDS files via Google TTS.

If you are familiar with Python, you will find it easy to use.

---

## Preparing Environment

### Setup ffmpeg & Config Environment PATH

Installing ffmpeg:

If you haven't installed ffmpeg yet, you need to install it first. On Windows, follow these steps:

1. Download ffmpeg:
   - Visit https://ffmpeg.org/download.html#build-windows and download the version suitable for your system.

2. Extract the downloaded file to a convenient location, for example:
   ```
   C:\ffmpeg
   ```

3. Add the ffmpeg bin directory to the system path:
   - Right-click on "This PC" or "My Computer" and select "Properties".
   - Click on "Advanced system settings".
   - Click on "Environment Variables".
   - Under "System variables", find "Path" and click "Edit".
   - Click "New" and add the path to the ffmpeg bin directory, for example `C:\ffmpeg\bin`.
   - Click "OK" to save all changes.

### Download and install Python 3.10

Download Path: https://www.python.org/downloads/windows/

**Notice:** Click "Add Python to environment variables" during installation.

### Install Poetry

1. First, install pipx if you haven't already:
   ```bash
   python -m pip install --user pipx
   python -m pipx ensurepath
   ```
   Close and reopen your terminal after this step.

2. Install Poetry using pipx:
   ```bash
   pipx install poetry
   ```

3. Verify the Installation:
   ```bash
   poetry --version
   ```
   You should see the version number of Poetry if it's installed correctly.

4. Auto setup:
   ```bash
   poetry install 
   ```

---

## Configure your customized speech wav files

1. Edit `edgetx_audio_file_map.csv` column `new_wording`

2. Edit `config.json`:
   - `"language": "zh-tw"`
     Supported language list ,Please refer to: https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang
   - `"map_file": "edgetx_audio_files_map.csv"`
     Config file name of mapping
   - `"speech_speed": 1.4`
     The larger number increases speech speed. Recommended value range: 0.5 - 2

---

## Execution

- CMD or Power Shell:
  ```bash
  python execute.py
  ```

- Using jupyter-notebook or jupyter-lab:
  Use IDE to open `execute.ipynb`

- After successful execution, it will generate a folder `EdgeTx_Audio_Package\YourLanguage`

- Copy all files and SYSTEM folder into your SD card `SOUNDS\en\`, kindly check that the EdgeTx Language is set to English

---

## Notice

Your antivirus software may not trust ffmpeg and may block it. You can either trust it or temporarily turn off your antivirus.
