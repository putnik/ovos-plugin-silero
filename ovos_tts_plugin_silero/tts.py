# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import torch

from ovos_plugin_manager.templates.tts import TTS


class SileroTTSPlugin(TTS):
    """Interface to Silero TTS."""
    lang_config = {
        'av': {
            'v4_cyrillic': ['b_ava'],
        },
        'ba': {
            'v4_cyrillic': ['b_bashkir'],
        },
        'bn': {
            'v4_indic': ['bengali_male', 'bengali_female'],
            'v3_indic': ['bengali_male', 'bengali_female'],
        },
        'bg': {
            'v4_cyrillic': ['b_bulb', 'b_bulc'],
        },
        'ce': {
            'v4_cyrillic': ['b_che'],
        },
        'cv': {
            'v4_cyrillic': ['b_cv', 'cv_ekaterina'],
        },
        'de': {
            'v3_de': [],
        },
        'en': {
            'v3_en': ['en_1', 'en_2', 'en_3', 'en_4', 'en_5', 'en_6', 'en_7',
                      'en_8', 'en_9', 'en_10', 'en_11', 'en_12', 'en_13',
                      'en_14', 'en_15', 'en_16', 'en_17', 'en_18', 'en_19',
                      'en_20', 'en_21', 'en_22', 'en_23', 'en_24', 'en_25',
                      'en_26', 'en_27', 'en_28', 'en_29', 'en_30', 'en_31',
                      'en_32', 'en_33', 'en_34', 'en_35', 'en_36', 'en_37',
                      'en_38', 'en_39', 'en_40', 'en_41', 'en_42', 'en_43',
                      'en_44', 'en_45', 'en_46', 'en_47', 'en_48', 'en_49',
                      'en_50', 'en_51', 'en_52', 'en_53', 'en_54', 'en_55',
                      'en_56', 'en_57', 'en_58', 'en_59', 'en_60', 'en_61',
                      'en_62', 'en_63', 'en_64', 'en_65', 'en_66', 'en_67',
                      'en_68', 'en_69', 'en_70', 'en_71', 'en_72', 'en_73',
                      'en_74', 'en_75', 'en_76', 'en_77', 'en_78', 'en_79',
                      'en_80', 'en_81', 'en_82', 'en_83', 'en_84', 'en_85',
                      'en_86', 'en_87', 'en_88', 'en_89', 'en_90', 'en_91',
                      'en_92', 'en_93', 'en_94', 'en_95', 'en_96', 'en_97',
                      'en_98', 'en_99', 'en_100', 'en_101', 'en_102', 'en_103',
                      'en_104', 'en_105', 'en_106', 'en_107', 'en_108',
                      'en_109', 'en_110', 'en_111', 'en_112', 'en_113',
                      'en_114', 'en_115', 'en_116', 'en_117', 'random'],
            'v3_en_indic': ['hindi_female', 'hindi_male', 'malayalam_female',
                            'malayalam_male', 'manipuri_female',
                            'bengali_female',
                            'bengali_male', 'rajasthani_female',
                            'rajasthani_male',
                            'tamil_female', 'tamil_male', 'telugu_female',
                            'telugu_male', 'gujarati_female', 'gujarati_male',
                            'kannada_female', 'kannada_male'],
        },
        'gu': {
            'v4_indic': ['gujarati_male', 'gujarati_female'],
            'v3_indic': ['gujarati_male', 'gujarati_female'],
        },
        'hi': {
            'v4_indic': ['hindi_male', 'hindi_female'],
            'v3_indic': ['hindi_male', 'hindi_female'],
        },
        'kjh': {
            'v4_cyrillic': ['b_kjh'],
        },
        'kn': {
            'v4_indic': ['kannada_male', 'kannada_female'],
            'v3_indic': ['kannada_male', 'kannada_female'],
        },
        'kpv': {
            'v4_cyrillic': ['b_kpv'],
        },
        'krc': {
            'v4_cyrillic': ['b_krc'],
        },
        'kz': {
            'v4_cyrillic': ['kz_M1', 'kz_M2', 'kz_F3', 'kz_F1', 'kz_F2'],
        },
        'lez': {
            'v4_cyrillic': ['b_lez'],
        },
        'mhr': {
            'v4_cyrillic': ['b_mhr'],
        },
        'ml': {
            'v4_indic': ['malayalam_male', 'malayalam_female'],
            'v3_indic': ['malayalam_male', 'malayalam_female'],
        },
        'mni': {
            'v4_indic': ['manipuri_male', 'manipuri_female'],
            'v3_indic': ['manipuri_male', 'manipuri_female'],
        },
        'mrj': {
            'v4_cyrillic': ['b_mrj'],
        },
        'myv': {
            'v4_cyrillic': ['b_myv'],
        },
        'nog': {
            'v4_cyrillic': ['b_nog'],
        },
        'ru': {
            'v4_ru': ['eugene', 'aidar', 'baya', 'kseniya', 'xenia', 'random'],
            'v4_cyrillic': ['b_ru'],
        },
        'os': {
            'v4_cyrillic': ['b_oss'],
        },
        'raj': {
            'v4_indic': ['rajasthani_male', 'rajasthani_female'],
            'v3_indic': ['rajasthani_male', 'rajasthani_female'],
        },
        'sah': {
            'v4_cyrillic': ['b_sah'],
        },
        'ta': {
            'v4_indic': ['tamil_male', 'tamil_female'],
            'v3_indic': ['tamil_male', 'tamil_female'],
        },
        'te': {
            'v4_indic': ['telugu_male', 'telugu_female'],
            'v3_indic': ['telugu_male', 'telugu_female'],
        },
        'tt': {
            'v4_cyrillic': ['b_tat', 'marat_tt'],
        },
        'tyv': {
            'v4_cyrillic': ['b_tyv'],
        },
        'ua': {
            'v4_ua': ['mykyta', 'random'],
        },
        'udm': {
            'v4_cyrillic': ['b_udm'],
        },
        'uz': {
            'v4_uz': ['dilnavoz'],
            'v4_cyrillic': ['b_uzb'],
        },
        'xal': {
            'v4_cyrillic': ['b_kalmyk', 'kalmyk_erdni', 'kalmyk_delghir'],
        },
    }
    model_url = {
        'v4_cyrillic': 'https://models.silero.ai/models/tts/cyr/v4_cyrillic.pt',
        'v3_de': 'https://models.silero.ai/models/tts/de/v3_de.pt',
        'v3_en': 'https://models.silero.ai/models/tts/en/v3_en.pt',
        'v3_en_indic': 'https://models.silero.ai/models/tts/en/v3_en_indic.pt',
        'v3_es': 'https://models.silero.ai/models/tts/es/v3_es.pt',
        'v3_fr': 'https://models.silero.ai/models/tts/fr/v3_fr.pt',
        'v3_indic': 'https://models.silero.ai/models/tts/indic/v3_indic.pt',
        'v4_indic': 'https://models.silero.ai/models/tts/indic/v4_indic.pt',
        'ru_v3': 'https://models.silero.ai/models/tts/ru/ru_v3.pt',
        'v3_1_ru': 'https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
        'v4_ru': 'https://models.silero.ai/models/tts/ru/v4_ru.pt',
        'v3_tt': 'https://models.silero.ai/models/tts/tt/v3_tt.pt',
        'v3_ua': 'https://models.silero.ai/models/tts/ua/v3_ua.pt',
        'v4_ua': 'https://models.silero.ai/models/tts/ua/v4_ua.pt',
        'v3_uz': 'https://models.silero.ai/models/tts/uz/v3_uz.pt',
        'v4_uz': 'https://models.silero.ai/models/tts/uz/v4_uz.pt',
        'v3_xal': 'https://models.silero.ai/models/tts/xal/v3_xal.pt',
    }

    def __init__(self, lang="en-us", config=None):
        super(SileroTTSPlugin, self).__init__(lang, config)

        lang = lang.split('-')[0]
        self.model = self.config.get("model") or next(iter(self.lang_config[lang]))
        self.voice = self.config.get("voice") or next(
            iter(self.lang_config[lang][self.model]))
        self.sample_rate = self.config.get("sample_rate") or 24000

        # download and load model
        # self.preload_models()

    def get_tts(self, sentence, wav_file, lang=None, speaker=None):
        """Generate WAV and phonemes.

        Arguments:
            sentence (str): sentence to generate audio for
            wav_file (str): output file
            lang (str): optional lang override
            speaker (int): optional speaker override

        Returns:
            tuple ((str) file location, (str) generated phonemes)
        """
        lang = lang or self.lang

        device = torch.device('cpu')
        torch.set_num_threads(4)
        local_file = f'{self.model}.pt'

        if not os.path.isfile(local_file):
            torch.hub.download_url_to_file(self.model_url[self.model],
                                           local_file)

        model = torch.package.PackageImporter(local_file).load_pickle(
            'tts_models', 'model')
        model.to(device)

        audio_path = model.save_wav(text=sentence,
                                    speaker=self.voice,
                                    sample_rate=self.sample_rate)

        os.replace(audio_path, wav_file)

        return wav_file, None

    def available_languages(self) -> set:
        return set(self.lang_config.keys())


SileroTTSPluginConfig = {
    lang: [
        {model + ' / ' + voice: {
            "model": model,
            "voice": voice,
            "gender": "female" if voice.endswith('_female') else "male",
            "offline": True,
        }}
        for model, voices in SileroTTSPlugin.lang_config[lang].items()
        for voice in voices
    ]
    for lang in SileroTTSPlugin.lang_config.keys()
}

if __name__ == "__main__":
    config = {
        'model': 'v4_ru',
        'voice': 'eugene',
    }

    # print(SileroTTSPluginConfig["ru"])
    e = SileroTTSPlugin('ru-ru', config)
    e.get_tts("кто хороший мальчик?", "hello.wav")
