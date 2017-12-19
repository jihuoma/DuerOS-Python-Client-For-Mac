from snowboy import snowboydecoder

def detected_callback():
    print("hotword detected")
    
detector = snowboydecoder.HotwordDetector("/Users/nyloner/Projects/DuerOS/DuerOS-Python-Client/app/model/xiaobai.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)
