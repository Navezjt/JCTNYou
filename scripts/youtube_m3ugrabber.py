#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                  >> https://github.com/Navezjt     #
#########################################################################
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/Navezjt/JCTNYou/main/assets/moose_na.m3u')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/Navezjt/JCTNYou/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/bein.com.xml.gz, https://iptv-org.github.io/epg/guides/ar/i24news.tv.xml.gz, https://iptv-org.github.io/epg/guides/ar/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/az/tv.mail.ru.xml.gz, https://iptv-org.github.io/epg/guides/bg/tv.dir.bg.xml.gz, https://iptv-org.github.io/epg/guides/bg/tvprofil.com.xml.gz, https://iptv-org.github.io/epg/guides/bn/sky.com.xml.gz, https://iptv-org.github.io/epg/guides/bs/mtel.ba.xml.gz, https://iptv-org.github.io/epg/guides/ca/andorradifusio.ad.xml.gz, https://iptv-org.github.io/epg/guides/cs/m.tv.sms.cz.xml.gz, https://iptv-org.github.io/epg/guides/cs/mujtvprogram.cz.xml.gz, https://iptv-org.github.io/epg/guides/de/hd-plus.de.xml.gz, https://iptv-org.github.io/epg/guides/de/magentatv.at.xml.gz, https://iptv-org.github.io/epg/guides/de/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/de/tvheute.at.xml.gz, https://iptv-org.github.io/epg/guides/el/cosmote.gr.xml.gz, https://iptv-org.github.io/epg/guides/el/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/en/abc.net.au.xml.gz, https://iptv-org.github.io/epg/guides/en/arianaafgtv.com.xml.gz, https://iptv-org.github.io/epg/guides/en/arianatelevision.com.xml.gz, https://iptv-org.github.io/epg/guides/en/bein.com.xml.gz, https://iptv-org.github.io/epg/guides/en/bt.com.xml.gz, https://iptv-org.github.io/epg/guides/en/directv.com.xml.gz, https://iptv-org.github.io/epg/guides/en/dishtv.in.xml.gz, https://iptv-org.github.io/epg/guides/en/dstv.com.xml.gz, https://iptv-org.github.io/epg/guides/en/epg.i-cable.com.xml.gz, https://iptv-org.github.io/epg/guides/en/flixed.io.xml.gz, https://iptv-org.github.io/epg/guides/en/i.mjh.nz.xml.gz, https://iptv-org.github.io/epg/guides/en/m.tv.sms.cz.xml.gz, https://iptv-org.github.io/epg/guides/en/melita.com.xml.gz, https://iptv-org.github.io/epg/guides/en/mewatch.sg.xml.gz, https://iptv-org.github.io/epg/guides/en/mytvsuper.com.xml.gz, https://iptv-org.github.io/epg/guides/en/nowplayer.now.com.xml.gz, https://iptv-org.github.io/epg/guides/en/ontvtonight.com.xml.gz, https://iptv-org.github.io/epg/guides/en/plex.tv.xml.gz, https://iptv-org.github.io/epg/guides/en/rev.bs.xml.gz, https://iptv-org.github.io/epg/guides/en/singtel.com.xml.gz, https://iptv-org.github.io/epg/guides/en/sky.com.xml.gz, https://iptv-org.github.io/epg/guides/en/starhubtvplus.com.xml.gz, https://iptv-org.github.io/epg/guides/en/startimestv.com.xml.gz, https://iptv-org.github.io/epg/guides/en/tapdmv.com.xml.gz, https://iptv-org.github.io/epg/guides/en/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/en/tv.post.lu.xml.gz, https://iptv-org.github.io/epg/guides/en/tvpassport.com.xml.gz, https://iptv-org.github.io/epg/guides/en/unifi.com.my.xml.gz, https://iptv-org.github.io/epg/guides/en/virginmedia.com.xml.gz, https://iptv-org.github.io/epg/guides/en/watchyour.tv.xml.gz, https://iptv-org.github.io/epg/guides/en/xumo.tv.xml.gz, https://iptv-org.github.io/epg/guides/es/cablego.com.pe.xml.gz, https://iptv-org.github.io/epg/guides/es/cableplus.com.uy.xml.gz, https://iptv-org.github.io/epg/guides/es/compulms.com.xml.gz, https://iptv-org.github.io/epg/guides/es/comteco.com.bo.xml.gz, https://iptv-org.github.io/epg/guides/es/directv.com.ar.xml.gz, https://iptv-org.github.io/epg/guides/es/directv.com.uy.xml.gz, https://iptv-org.github.io/epg/guides/es/directv.com.xml.gz, https://iptv-org.github.io/epg/guides/es/flixed.io.xml.gz, https://iptv-org.github.io/epg/guides/es/gatotv.com.xml.gz, https://iptv-org.github.io/epg/guides/es/mi.tv.xml.gz, https://iptv-org.github.io/epg/guides/es/movistarplus.es.xml.gz, https://iptv-org.github.io/epg/guides/es/ontvtonight.com.xml.gz, https://iptv-org.github.io/epg/guides/es/programacion-tv.elpais.com.xml.gz, https://iptv-org.github.io/epg/guides/es/reportv.com.ar.xml.gz, https://iptv-org.github.io/epg/guides/es/siba.com.co.xml.gz, https://iptv-org.github.io/epg/guides/es/tv.movistar.com.pe.xml.gz, https://iptv-org.github.io/epg/guides/es/tvpassport.com.xml.gz, https://iptv-org.github.io/epg/guides/et/teliatv.ee.xml.gz, https://iptv-org.github.io/epg/guides/fi/telkku.com.xml.gz, https://iptv-org.github.io/epg/guides/fi/telsu.fi.xml.gz, https://iptv-org.github.io/epg/guides/fo/kvf.fo.xml.gz, https://iptv-org.github.io/epg/guides/fr/canalplus-caraibes.com.xml.gz, https://iptv-org.github.io/epg/guides/fr/canalplus.com.xml.gz, https://iptv-org.github.io/epg/guides/fr/chaines-tv.orange.fr.xml.gz, https://iptv-org.github.io/epg/guides/fr/mon-programme-tv.be.xml.gz, https://iptv-org.github.io/epg/guides/fr/programme-tv.net.xml.gz, https://iptv-org.github.io/epg/guides/fr/programme-tv.vini.pf.xml.gz, https://iptv-org.github.io/epg/guides/fr/telecablesat.fr.xml.gz, https://iptv-org.github.io/epg/guides/fr/telenet.tv.xml.gz, https://iptv-org.github.io/epg/guides/fr/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/fr/tvhebdo.com.xml.gz, https://iptv-org.github.io/epg/guides/hi/sky.com.xml.gz, https://iptv-org.github.io/epg/guides/hr/maxtv.hrvatskitelekom.hr.xml.gz, https://iptv-org.github.io/epg/guides/hr/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/hr/tvprofil.com.xml.gz, https://iptv-org.github.io/epg/guides/hu/musor.tv.xml.gz, https://iptv-org.github.io/epg/guides/hy/tv.mail.ru.xml.gz, https://iptv-org.github.io/epg/guides/id/indihometv.com.xml.gz, https://iptv-org.github.io/epg/guides/id/mncvision.id.xml.gz, https://iptv-org.github.io/epg/guides/id/vidio.com.xml.gz, https://iptv-org.github.io/epg/guides/is/ruv.is.xml.gz, https://iptv-org.github.io/epg/guides/it/guidatv.sky.it.xml.gz, https://iptv-org.github.io/epg/guides/it/superguidatv.it.xml.gz, https://iptv-org.github.io/epg/guides/it/tivu.tv.xml.gz, https://iptv-org.github.io/epg/guides/it/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/ja/tvguide.myjcom.jp.xml.gz, https://iptv-org.github.io/epg/guides/ka/magticom.ge.xml.gz, https://iptv-org.github.io/epg/guides/ko/wavve.com.xml.gz, https://iptv-org.github.io/epg/guides/ku/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/lb/tv.post.lu.xml.gz, https://iptv-org.github.io/epg/guides/lt/cgates.lt.xml.gz, https://iptv-org.github.io/epg/guides/mk/maxtvgo.mk.xml.gz, https://iptv-org.github.io/epg/guides/mn/zuragt.mn.xml.gz, https://iptv-org.github.io/epg/guides/ms/astro.com.my.xml.gz, https://iptv-org.github.io/epg/guides/ms/rtmklik.rtm.gov.my.xml.gz, https://iptv-org.github.io/epg/guides/my/unifi.com.my.xml.gz, https://iptv-org.github.io/epg/guides/nl/delta.nl.xml.gz, https://iptv-org.github.io/epg/guides/nl/telenet.tv.xml.gz, https://iptv-org.github.io/epg/guides/nl/tvgids.nl.xml.gz, https://iptv-org.github.io/epg/guides/nl/ziggogo.tv.xml.gz, https://iptv-org.github.io/epg/guides/no/allente.se.xml.gz, https://iptv-org.github.io/epg/guides/no/frikanalen.no.xml.gz, https://iptv-org.github.io/epg/guides/pl/programtv.onet.pl.xml.gz, https://iptv-org.github.io/epg/guides/pt/meo.pt.xml.gz, https://iptv-org.github.io/epg/guides/pt/mi.tv.xml.gz, https://iptv-org.github.io/epg/guides/pt/nos.pt.xml.gz, https://iptv-org.github.io/epg/guides/pt/rtp.pt.xml.gz, https://iptv-org.github.io/epg/guides/ro/programetv.ro.xml.gz, https://iptv-org.github.io/epg/guides/ru/9tv.co.il.xml.gz, https://iptv-org.github.io/epg/guides/ru/magticom.ge.xml.gz, https://iptv-org.github.io/epg/guides/ru/teliatv.ee.xml.gz, https://iptv-org.github.io/epg/guides/ru/tv.mail.ru.xml.gz, https://iptv-org.github.io/epg/guides/ru/tv.yandex.ru.xml.gz, https://iptv-org.github.io/epg/guides/sk/horizon.tv.xml.gz, https://iptv-org.github.io/epg/guides/sl/tv2go.t-2.net.xml.gz, https://iptv-org.github.io/epg/guides/sq/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/sr/mts.rs.xml.gz, https://iptv-org.github.io/epg/guides/sv/tv.nu.xml.gz, https://iptv-org.github.io/epg/guides/sv/tv24.se.xml.gz, https://iptv-org.github.io/epg/guides/th/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/th/tv.trueid.net.xml.gz, https://iptv-org.github.io/epg/guides/tr/digiturk.com.tr.xml.gz, https://iptv-org.github.io/epg/guides/tr/dsmart.com.tr.xml.gz, https://iptv-org.github.io/epg/guides/tr/tv.blue.ch.xml.gz, https://iptv-org.github.io/epg/guides/tr/tvplus.com.tr.xml.gz, https://iptv-org.github.io/epg/guides/tr/ziggogo.tv.xml.gz, https://iptv-org.github.io/epg/guides/zh/rthk.hk.xml.gz, https://iptv-org.github.io/epg/guides/zh/tv.cctv.com.xml.gz"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
