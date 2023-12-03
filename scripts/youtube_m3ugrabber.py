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

print('#EXTM3U x-tvg-url="https://xmltv.tvkaista.net/guides/default.xml, http://lichphatsong.xyz/schedule/vthanhtivi_epg.xml, https://xmltv.tvkaista.net/guides/abc.net.au.xml, http://lichphatsong.xyz/schedule/vthanhtivi_epg.xml, https://xmltv.tvkaista.net/guides/allente.dk.xml, https://xmltv.tvkaista.net/guides/allente.fi.xml, https://xmltv.tvkaista.net/guides/allente.no.xml, https://xmltv.tvkaista.net/guides/allente.se.xml, https://xmltv.tvkaista.net/guides/andorradifusio.ad.xml, https://xmltv.tvkaista.net/guides/anteltv.com.uy.xml, https://xmltv.tvkaista.net/guides/arianaafgtv.com.xml, https://xmltv.tvkaista.net/guides/arianatelevision.com.xml, https://xmltv.tvkaista.net/guides/arirang.com.xml, https://xmltv.tvkaista.net/guides/artonline.tv.xml, https://xmltv.tvkaista.net/guides/bein.com.xml, https://xmltv.tvkaista.net/guides/beinsports.com.xml, https://xmltv.tvkaista.net/guides/berrymedia.co.kr.xml, https://xmltv.tvkaista.net/guides/cablego.com.pe.xml, https://xmltv.tvkaista.net/guides/cableplus.com.uy.xml, https://xmltv.tvkaista.net/guides/canalplus.com.xml, https://xmltv.tvkaista.net/guides/cgates.lt.xml, https://xmltv.tvkaista.net/guides/chaines-tv.orange.fr.xml, https://xmltv.tvkaista.net/guides/clickthecity.com.xml, https://xmltv.tvkaista.net/guides/compulms.com.xml, https://xmltv.tvkaista.net/guides/content.astro.com.my.xml, https://xmltv.tvkaista.net/guides/cosmote.gr.xml, https://xmltv.tvkaista.net/guides/cubmu.com.xml, https://xmltv.tvkaista.net/guides/dens.tv.xml, https://xmltv.tvkaista.net/guides/digiturk.com.tr.xml, https://xmltv.tvkaista.net/guides/directv.com.uy.xml, https://xmltv.tvkaista.net/guides/dishtv.in.xml, https://xmltv.tvkaista.net/guides/disneystar.com.xml, https://xmltv.tvkaista.net/guides/dsmart.com.tr.xml, https://xmltv.tvkaista.net/guides/dstv.com.xml, https://xmltv.tvkaista.net/guides/elcinema.com.xml, https://xmltv.tvkaista.net/guides/ena.skylifetv.co.kr.xml, https://xmltv.tvkaista.net/guides/entertainment.ie.xml, https://xmltv.tvkaista.net/guides/firstmedia.com.xml, https://xmltv.tvkaista.net/guides/flixed.io.xml, https://xmltv.tvkaista.net/guides/foxsports.com.au.xml, https://xmltv.tvkaista.net/guides/foxtel.com.au.xml, https://xmltv.tvkaista.net/guides/frikanalen.no.xml, https://xmltv.tvkaista.net/guides/gatotv.com.xml, https://xmltv.tvkaista.net/guides/getafteritmedia.com.xml, https://xmltv.tvkaista.net/guides/guida.tv.xml, https://xmltv.tvkaista.net/guides/guidatv.sky.it.xml, https://xmltv.tvkaista.net/guides/horizon.tv.xml, https://xmltv.tvkaista.net/guides/i.mjh.nz.xml, https://xmltv.tvkaista.net/guides/i24news.tv.xml, https://xmltv.tvkaista.net/guides/iltalehti.fi.xml, https://xmltv.tvkaista.net/guides/indihometv.com.xml, https://xmltv.tvkaista.net/guides/ipko.com.xml, https://xmltv.tvkaista.net/guides/knr.gl.xml, https://xmltv.tvkaista.net/guides/kvf.fo.xml, https://xmltv.tvkaista.net/guides/m.tving.com.xml, https://xmltv.tvkaista.net/guides/magticom.ge.xml, https://xmltv.tvkaista.net/guides/mako.co.il.xml, https://xmltv.tvkaista.net/guides/maxtv.hrvatskitelekom.hr.xml, https://xmltv.tvkaista.net/guides/maxtvgo.mk.xml, https://xmltv.tvkaista.net/guides/mediagenie.co.kr.xml, https://xmltv.tvkaista.net/guides/mediaklikk.hu.xml, https://xmltv.tvkaista.net/guides/mediasetinfinity.mediaset.it.xml, https://xmltv.tvkaista.net/guides/melita.com.xml, https://xmltv.tvkaista.net/guides/meo.pt.xml, https://xmltv.tvkaista.net/guides/meuguia.tv.xml, https://xmltv.tvkaista.net/guides/mewatch.sg.xml, https://xmltv.tvkaista.net/guides/mi.tv.xml, https://xmltv.tvkaista.net/guides/mncvision.id.xml, https://xmltv.tvkaista.net/guides/moji.id.xml, https://xmltv.tvkaista.net/guides/mon-programme-tv.be.xml, https://xmltv.tvkaista.net/guides/movistarplus.es.xml, https://xmltv.tvkaista.net/guides/mtel.ba.xml, https://xmltv.tvkaista.net/guides/mts.rs.xml, https://xmltv.tvkaista.net/guides/mujtvprogram.cz.xml, https://xmltv.tvkaista.net/guides/musor.tv.xml, https://xmltv.tvkaista.net/guides/myafn.dodmedia.osd.mil.xml, https://xmltv.tvkaista.net/guides/mysky.com.ph.xml, https://xmltv.tvkaista.net/guides/mytelly.co.uk.xml, https://xmltv.tvkaista.net/guides/mytvsuper.com.xml, https://xmltv.tvkaista.net/guides/nhk.or.jp.xml, https://xmltv.tvkaista.net/guides/nhkworldpremium.com.xml, https://xmltv.tvkaista.net/guides/novacyprus.com.xml, https://xmltv.tvkaista.net/guides/novasports.gr.xml, https://xmltv.tvkaista.net/guides/nuevosiglo.com.uy.xml, https://xmltv.tvkaista.net/guides/nzxmltv.com.xml, https://xmltv.tvkaista.net/guides/ontvtonight.com.xml, https://xmltv.tvkaista.net/guides/osn.com.xml, https://xmltv.tvkaista.net/guides/pbsguam.org.xml, https://xmltv.tvkaista.net/guides/playtv.unifi.com.my.xml, https://xmltv.tvkaista.net/guides/plex.tv.xml, https://xmltv.tvkaista.net/guides/programacion-tv.elpais.com.xml, https://xmltv.tvkaista.net/guides/programacion.tcc.com.uy.xml, https://xmltv.tvkaista.net/guides/programetv.ro.xml, https://xmltv.tvkaista.net/guides/programme-tv.net.xml, https://xmltv.tvkaista.net/guides/programme-tv.vini.pf.xml, https://xmltv.tvkaista.net/guides/programtv.onet.pl.xml, https://xmltv.tvkaista.net/guides/raiplay.it.xml, https://xmltv.tvkaista.net/guides/reportv.com.ar.xml, https://xmltv.tvkaista.net/guides/rthk.hk.xml, https://xmltv.tvkaista.net/guides/rtmklik.rtm.gov.my.xml, https://xmltv.tvkaista.net/guides/rtp.pt.xml, https://xmltv.tvkaista.net/guides/ruv.is.xml, https://xmltv.tvkaista.net/guides/sat.tv.xml, https://xmltv.tvkaista.net/guides/shahid.mbc.net.xml, https://xmltv.tvkaista.net/guides/siba.com.co.xml, https://xmltv.tvkaista.net/guides/singtel.com.xml, https://xmltv.tvkaista.net/guides/sjonvarp.is.xml, https://xmltv.tvkaista.net/guides/sky.co.nz.xml, https://xmltv.tvkaista.net/guides/sky.com.xml, https://xmltv.tvkaista.net/guides/sky.de.xml, https://xmltv.tvkaista.net/guides/starhubtvplus.com.xml, https://xmltv.tvkaista.net/guides/startimestv.com.xml, https://xmltv.tvkaista.net/guides/streamingtvguides.com.xml, https://xmltv.tvkaista.net/guides/superguidatv.it.xml, https://xmltv.tvkaista.net/guides/taiwanplus.com.xml, https://xmltv.tvkaista.net/guides/tapdmv.com.xml, https://xmltv.tvkaista.net/guides/telenet.tv.xml, https://xmltv.tvkaista.net/guides/teliatv.ee.xml, https://xmltv.tvkaista.net/guides/telkussa.fi.xml, https://xmltv.tvkaista.net/guides/telsu.fi.xml, https://xmltv.tvkaista.net/guides/tivu.tv.xml, https://xmltv.tvkaista.net/guides/toonamiaftermath.com.xml, https://xmltv.tvkaista.net/guides/turksatkablo.com.tr.xml, https://xmltv.tvkaista.net/guides/tv-programme.telecablesat.fr.xml, https://xmltv.tvkaista.net/guides/tv.blue.ch.xml, https://xmltv.tvkaista.net/guides/tv.cctv.com.xml, https://xmltv.tvkaista.net/guides/tv.dir.bg.xml, https://xmltv.tvkaista.net/guides/tv.lv.xml, https://xmltv.tvkaista.net/guides/tv.magenta.at.xml, https://xmltv.tvkaista.net/guides/tv.mail.ru.xml, https://xmltv.tvkaista.net/guides/tv.movistar.com.pe.xml, https://xmltv.tvkaista.net/guides/tv.nu.xml, https://xmltv.tvkaista.net/guides/tv.post.lu.xml, https://xmltv.tvkaista.net/guides/tv.yandex.ru.xml, https://xmltv.tvkaista.net/guides/tv24.co.uk.xml, https://xmltv.tvkaista.net/guides/tv24.se.xml, https://xmltv.tvkaista.net/guides/tv2go.t-2.net.xml, https://xmltv.tvkaista.net/guides/tvcesoir.fr.xml, https://xmltv.tvkaista.net/guides/tvcubana.icrt.cu.xml, https://xmltv.tvkaista.net/guides/tvgids.nl.xml, https://xmltv.tvkaista.net/guides/tvguide.com.xml, https://xmltv.tvkaista.net/guides/tvguide.myjcom.jp.xml, https://xmltv.tvkaista.net/guides/tvhebdo.com.xml, https://xmltv.tvkaista.net/guides/tvheute.at.xml, https://xmltv.tvkaista.net/guides/tvim.tv.xml, https://xmltv.tvkaista.net/guides/tvireland.ie.xml, https://xmltv.tvkaista.net/guides/tvmi.mt.xml, https://xmltv.tvkaista.net/guides/tvmusor.hu.xml, https://xmltv.tvkaista.net/guides/tvpassport.com.xml, https://xmltv.tvkaista.net/guides/tvplus.com.tr.xml, https://xmltv.tvkaista.net/guides/tvprofil.com.xml, https://xmltv.tvkaista.net/guides/tvtv.us.xml, https://xmltv.tvkaista.net/guides/vidio.com.xml, https://xmltv.tvkaista.net/guides/virginmediatelevision.ie.xml, https://xmltv.tvkaista.net/guides/virgintvgo.virginmedia.com.xml, https://xmltv.tvkaista.net/guides/visionplus.id.xml, https://xmltv.tvkaista.net/guides/vtm.be.xml, https://xmltv.tvkaista.net/guides/walesi.com.fj.xml, https://xmltv.tvkaista.net/guides/watch.sportsnet.ca.xml, https://xmltv.tvkaista.net/guides/watchyour.tv.xml, https://xmltv.tvkaista.net/guides/wavve.com.xml, https://xmltv.tvkaista.net/guides/web.magentatv.de.xml, https://xmltv.tvkaista.net/guides/webtv.delta.nl.xml, https://xmltv.tvkaista.net/guides/worldfishingnetwork.com.xml, https://xmltv.tvkaista.net/guides/xumo.tv.xml, https://xmltv.tvkaista.net/guides/zap.co.ao.xml, https://xmltv.tvkaista.net/guides/ziggogo.tv.xml, https://xmltv.tvkaista.net/guides/znbc.co.zm.xml, https://xmltv.tvkaista.net/guides/zuragt.mn.xml"
"')
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
