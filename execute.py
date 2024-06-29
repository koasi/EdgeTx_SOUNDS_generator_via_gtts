from gtts import gTTS
from pydub import AudioSegment
import os
import tempfile
import pandas as pd
import json

def load_config(config_file='config.json'):
    with open(config_file, 'r') as f:
        return json.load(f)
# 載入設定
config = load_config()

# 從配置中獲取設定
language = config['language']
map_df = pd.read_csv(config['map_file'])
speech_speed = config['speech_speed']

directory = "EdgeTx_Audio_Package/"+language

if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory '{directory}' created.")
else:
    print(f"Directory '{directory}' already exists.")

directory2 = "EdgeTx_Audio_Package/"+language+"/SYSTEM"

if not os.path.exists(directory2):
    os.makedirs(directory2)
    print(f"Directory '{directory2}' created.")
else:
    print(f"Directory '{directory2}' already exists.")


map_df['org_wording'] = map_df['Translation']
map_df['new_wording'] = map_df.apply(lambda x: x['org_wording'] if pd.isnull(x['new_wording']) else x['new_wording'], axis=1)
map_df['output_path'] = map_df['path'].apply(lambda x: str(x).replace('cn',language))



def text_to_speech_with_speed(text, lang, speed , output_file):
    # 創建臨時文件
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
        temp_filename = temp_file.name

    # 使用gTTS生成語音
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(temp_filename)

    # 使用pydub加載音頻
    audio = AudioSegment.from_mp3(temp_filename)

    # 調整速度
    adjusted_audio = audio.speedup(playback_speed=speed)
    # 調整音頻為32kHz
    adjusted_audio = adjusted_audio.set_frame_rate(32000)
    # 導出調整後的音頻為WAV格式
    adjusted_audio.export(output_file, format="wav")
    

    # 刪除臨時文件
    os.unlink(temp_filename)

    print(f"生成的音頻已保存為 {output_file}")



# Iterate over each row in the DataFrame
for index, row in map_df.iterrows():
    new_wording = row['new_wording']
    output_path = row['output_path']
    
    # Perform TTS
    # tts = gTTS(new_wording, lang='zh-tw')
    
    # # Save the TTS audio as a WAV file
    # tts.save("""EdgeTx_Audio_Package\\"""+output_path)

    text_to_speech_with_speed(new_wording, lang=language, speed=speech_speed, output_file="""EdgeTx_Audio_Package\\"""+output_path)

    
    print(f"TTS audio saved for {new_wording} at {output_path}")