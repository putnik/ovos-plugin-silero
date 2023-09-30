#!/usr/bin/env python3
import os

from setuptools import setup

TTS_ENTRY_POINT = 'ovos-tts-plugin-silero = ovos_tts_plugin_silero:SileroTTSPlugin'
SAMPLE_CONFIGS = 'ovos-tts-plugin-silero.config = ovos_tts_plugin_silero:SileroTTSPluginConfig'
BASEDIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    """ Find the version of the package"""
    version_file = os.path.join(BASEDIR, 'ovos_tts_plugin_silero', 'version.py')
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if alpha and int(alpha) > 0:
        version += f"a{alpha}"
    return version


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(BASEDIR, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        if 'MYCROFT_LOOSE_REQUIREMENTS' in os.environ:
            print('USING LOOSE REQUIREMENTS!')
            requirements = [r.replace('==', '>=').replace('~=', '>=') for r in requirements]
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]


setup(
    name='ovos-tts-plugin-silero',
    version=get_version(),
    description='Silero TTS plugin for OpenVoiceOS',
    url='https://github.com/putnik/ovos-plugin-silero',
    author='Sergei Leshchina',
    author_email='mail@putnik.tech',
    license='Apache-2.0',
    packages=['ovos_tts_plugin_silero'],
    install_requires=required("requirements.txt"),
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Russian',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='mycroft plugin tts OVOS OpenVoiceOS silero',
    entry_points={
        'mycroft.plugin.tts': TTS_ENTRY_POINT,
        'mycroft.plugin.tts.config': SAMPLE_CONFIGS
    }
)
