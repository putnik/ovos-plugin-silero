import os
import torch

from mycroft.configuration import Configuration
from mycroft.tts import TTS, TTSValidator

available_speakers = {
    'aidar_v2': 'ru',
    'baya_v2': 'ru',
    'irina_v2': 'ru',
    'kseniya_v2': 'ru',
    'natasha_v2': 'ru',
    'ruslan_v2': 'ru',
    'lj_v2': 'en',
    'thorsten_v2': 'de',
    'tux_v2': 'es',
    'gilles_v2': 'fr',
    'multi_v2': ['de', 'en', 'es', 'fr', 'ru', 'tt'],
    'aigul_v2': 'ba',
    'erdni_v2': 'xal',
    'dilyara_v2': 'tt',
    'dilnavoz_v2': 'uz',
}
device = torch.device('cpu')
torch.set_num_threads(4)


class SileroTTSPlugin(TTS):
    def __init__(self, lang, config):
        super(SileroTTSPlugin, self).__init__(lang, config,
                                              SileroTTSValidator(self), "wav")
        config = Configuration.get().get("tts", {}).get("silero", {})
        self.speaker = config.get("speaker", "multi_v2")

    def get_tts(self, sentence, wav_file):
        with open(wav_file, "wb") as f:
            for audio_content in self._synthesize(sentence):
                f.write(audio_content)
        return wav_file, None

    def _synthesize(self, text):
        local_file = self.speaker + '.pt'
        model = torch.package.PackageImporter(local_file).load_pickle(
            "tts_models", "model")
        model.to(device)

        sample_rate = 16000

        batch = str(text).split("\n")
        audio_paths = model.save_wav(texts=batch,
                                     sample_rate=sample_rate)
        for audio_path in audio_paths:
            yield audio_path


class SileroTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(SileroTTSValidator, self).__init__(tts)

    def validate_lang(self):
        available_langs = available_speakers.values()
        available_langs = set(filter(lambda l: type(l) == str, available_langs))
        lang = Configuration.get().get("lang", "en-us").split('-')[0]
        return lang in available_langs

    def validate_connection(self):
        config = Configuration.get().get("tts", {}).get("silero", {})
        speaker = str(config.get("speaker", "multi_v2"))
        local_file = speaker + '.pt'
        if not os.path.isfile(local_file):
            name, version = speaker.split('_')
            lang = available_speakers[speaker]
            if type(lang) != str:
                lang = 'multi'
            url = 'https://models.silero.ai/models/tts/%s/%s_%s.pt' % (
                lang, name, version
            )
            torch.hub.download_url_to_file(url, local_file)

    def get_tts_class(self):
        return SileroTTSPlugin
