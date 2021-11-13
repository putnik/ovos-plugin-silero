#!/usr/bin/env python3
from setuptools import setup

TTS_ENTRY_POINT = 'silero = mycroft_plugin_silero:SileroTTSPlugin'

setup(
    name='mycroft-plugin-silero',
    version='0.1.0-alpha2',
    description='Silero TTS/STT plugin for Mycroft',
    long_description='file: README.md',
    long_description_content_type='text/markdown',
    url='https://github.com/putnik/mycroft-plugin-silero',
    author='Sergey Leschina',
    author_email='mail@putnik.tech',
    license='Apache-2.0',
    packages=['mycroft_plugin_silero'],
    install_requires=['numpy', 'torch'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Russian',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='mycroft plugin tts stt silero',
    entry_points={
        'mycroft.plugin.tts': TTS_ENTRY_POINT,
    }
)
