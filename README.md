# VK Cloud STT/TTS plugin for Mycroft

VK Group (ex-Mail.ru group) is a big Russian company that has their own personal assistant [Marusia](https://marusia.mail.ru/). They allow to use same technologies in their cloud services.

VK Cloud supports two authorisation methods: one time tokens and service tokens without expiration. For now there is only service tokens support.

I don't really like the response time of the TTS service, but STT works very well. For now, VK Cloud supports only Russian language.

## How to use
1. Register a new VK Cloud account: https://mcs.mail.ru/
2. Confirm your email and phone number.
3. You will get 100 free roubles.
4. Create service token for Cloud Voice.
5. `mycroft-pip install mycroft-plugin-vk-cloud`
6. Edit `mycroft.conf` (`mycroft-config edit user`):
```json
"tts": {
  "module": "vk",
  "vk": {
    "service_token": "YOUR_SERVICE_TOKEN",
    "tempo": 1.15
  }
},
"stt": {
  "module": "vk",
  "vk": {
    "credential": {
      "service_token": "YOUR_SERVICE_TOKEN"
    }
  }
}
```
`tempo` is optional. Possible values from 0.75 to 1.75, default id 1.0.