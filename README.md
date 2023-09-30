## Description

OVOS TTS plugin for [Silero Models](https://github.com/snakers4/silero-models)

This plugin supports only V3 and V4 models. All models available only for non-commercial usage.

## Install

`pip install ovos-tts-plugin-silero`

## Configuration

### Basic

Will be used default model for your language and a first available voice for that model.
Default sample rate is 24000.

```json
  "tts": {
    "module": "ovos-tts-plugin-silero"
  }
```

### Advanced
See [models and voices in Silero Models repository](https://github.com/snakers4/silero-models#models-and-speakers)

```json
  "tts": {
    "module": "ovos-tts-plugin-silero",
    "ovos-tts-plugin-silero": {
      "model": "v4_ru",
      "voice": "xenia",
      "sample_rate": 24000
    }
  }
```