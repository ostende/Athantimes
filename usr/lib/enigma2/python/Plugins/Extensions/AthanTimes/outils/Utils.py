from datetime import date, datetime
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmap, MultiContentEntryPixmapAlphaTest, MultiContentEntryPixmapAlphaBlend
from enigma import gFont, eTimer, eConsoleAppContainer, ePicLoad, loadPNG, loadJPG, getDesktop, eServiceReference, iPlayableService, eListboxPythonMultiContent, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, RT_VALIGN_CENTER
from Components.MenuList import MenuList
from Tools.Directories import fileExists, resolveFilename, SCOPE_PLUGINS, pathExists
import re, urllib, urllib2, os, cookielib, time
from os import path as os_path, system as os_system, unlink, stat, mkdir, popen, makedirs, listdir, access, rename, remove, W_OK, R_OK, F_OK
from Screens.Screen import Screen
from xml.etree.cElementTree import fromstring, ElementTree
from Tools.Directories import fileExists, resolveFilename, SCOPE_PLUGINS
import base64
import re, urllib, urllib2, os
from urllib2 import urlopen, Request
from twisted.web.client import downloadPage, getPage
from enigma import getDesktop
from enigma import eListboxPythonMultiContent, gFont
from enigma import gRGB
from Components.Sources.List import List
from Components.MenuList import MenuList
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmap, MultiContentEntryPixmapAlphaTest
from enigma import eListboxPythonMultiContent, eListbox, gFont, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, RT_WRAP
from Components.Pixmap import Pixmap, MovingPixmap
from Components.Label import Label
from urllib2 import urlopen, Request, URLError, HTTPError
from httplib import HTTPException
import cookielib, datetime, os, re, socket, sys, time, urllib2
from urlparse import parse_qs
from urllib import unquote_plus, urlencode
Agent = {'User-agent': 'Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.',
 'Connection': 'Close'}
UserAgent2 = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
 'Accept': 'text/html'}
wsize = getDesktop(0).size().width()
hsize = getDesktop(0).size().height()
dwidth = getDesktop(0).size().width()

def show_listiptv2(cityId, countryId, cityName, countryName):
    if dwidth == 1280:
        res = [(cityId,
          countryId,
          cityName,
          countryName)]
        res.append(MultiContentEntryText(pos=(2, 2), size=(425, 30), font=5, text=cityId, backcolor_sel=26214, backcolor=22503, flags=RT_HALIGN_CENTER))
        return res
    else:
        res = [(cityId,
          countryId,
          cityName,
          countryName)]
        res.append(MultiContentEntryText(pos=(2, 2), size=(459, 30), font=7, text=cityId, backcolor_sel=26214, backcolor=22503, flags=RT_HALIGN_CENTER))
        return res


def XML_Country(Mylist, Contnt, Contr):
    Path_1 = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/Choice/' + Contr + '.xml'
    if fileExists(Path_1):
        os.remove(Path_1)
        outfile = open(Path_1, 'a')
        outfile.write('<?xml version="1.0"?>\n<!-- List of ' + Contnt + ' -->\n<stream>\n')
        for x in Mylist:
            outfile.write('<Contry>\n\t<name>' + str(x[0][0]) + '</name>\n' + '\t<url>' + str(x[0][1]) + '</url>\n\t<Id>' + str(x[0][2]) + '</Id>\n</Contry>\n')

        outfile.write('</stream>')
        outfile.close()
    else:
        outfile = open(Path_1, 'a')
        outfile.write('<?xml version="1.0"?>\n<!-- List of ' + Contnt + ' -->\n<stream>\n')
        for x in Mylist:
            outfile.write('<Contry>\n\t<name>' + str(x[0][0]) + '</name>\n' + '\t<url>' + str(x[0][1]) + '</url>\n\t<Id>' + str(x[0][2]) + '</Id>\n</Contry>\n')

        outfile.write('</stream>')
        outfile.close()


def XML_Continent(Mylist, Contry):
    Path_1 = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/' + Contry + '/' + Contry + '.xml'
    if fileExists(Path_1):
        os.remove(Path_1)
        outfile = open(Path_1, 'a')
        outfile.write('<?xml version="1.0"?>\n<!-- List of ' + Contry + ' -->\n<stream>\n')
        for x in Mylist:
            outfile.write('<Contry>\n\t<name>' + str(x[0][0]) + '</name>\n' + '\t<url>' + str(x[0][1]) + '</url>\n</Contry>\n')

        outfile.write('</stream>')
        outfile.close()
    else:
        outfile = open(Path_1, 'a')
        outfile.write('<?xml version="1.0"?>\n<!-- List of ' + Contry + ' -->\n<stream>\n')
        for x in Mylist:
            outfile.write('<Contry>\n\t<name>' + str(x[0][0]) + '</name>\n' + '\t<url>' + str(x[0][1]) + '</url>\n</Contry>\n')

        outfile.write('</stream>')
        outfile.close()


def XML_Choice(Mylist):
    Path = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes.xml'
    Patho = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Prayer.txt'
    Pathoo = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/city.txt'
    os.remove(Path)
    os.remove(Patho)
    os.remove(Pathoo)
    outfile = open(Path, 'a')
    outfileo = open(Patho, 'a')
    outfileoo = open(Pathoo, 'a')
    outfile.write('<?xml version="1.0"?>\n<stream>\n')
    for x in Mylist:
        outfile.write('<Choice>\n\t<Contnt>' + str(x[0][0]) + '</Contnt>\n' + '\t<Contr>' + str(x[0][1]) + '</Contr>\n' + '\t<fajr>' + str(x[0][2]) + '</fajr>\n' + '\t<sunrise>' + str(x[0][3]) + '</sunrise>\n' + '\t<dhuhr>' + str(x[0][4]) + '</dhuhr>\n' + '\t<asr>' + str(x[0][5]) + '</asr>\n' + '\t<maghrib>' + str(x[0][6]) + '</maghrib>\n' + '\t<isha>' + str(x[0][7]) + '</isha>\n' + '\t<qiyam>' + str(x[0][8]) + '</qiyam>\n' + '\t<url>' + str(x[0][9]).replace('\n', '').replace('\t', '').replace('\r', '') + '</url>\n' + '\t<Id>' + str(x[0][10]) + '</Id>\n' + '\t<Lati>' + str(x[0][11]) + '</Lati>\n' + '\t<Longit>' + str(x[0][12]) + '</Longit>\n' + '\t<hijri>' + str(x[0][13]) + '</hijri>\n' + '\t<clac>' + str(x[0][14]) + '</clac>\n' + '\t<next>' + str(x[0][15]) + '</next>\n' + '\t<bled>' + str(x[0][16]) + '</bled>\n' + '\t<haiaa>' + str(x[0][17]) + '</haiaa>\n</Choice>\n')
        outfileo.write(str(x[0][1]) + '\n' + str(x[0][16]) + '\n' + str(Change_times(x[0][2])).replace('AM', '').replace('PM', '').replace(' ', '') + ':00' + '\n' + str(Change_times(x[0][3])).replace('AM', '').replace('PM', '').replace(' ', '') + ':00' + '\n' + str(Change_times(x[0][4])).replace('AM', '').replace('PM', '').replace(' ', '') + ':00' + '\n' + str(Change_times(x[0][5])).replace('AM', '').replace('PM', '').replace(' ', '') + ':00' + '\n' + str(Change_times(x[0][6])).replace('AM', '').replace('PM', '').replace(' ', '') + ':00' + '\n' + str(Change_times(x[0][7])).replace('AM', '').replace('PM', '').replace(' ', '') + ':00')
        outfileoo.write(str(x[0][1]) + ',' + str(x[0][16]))
        Favo = '<Contry>\n' + '\t<Contnt>' + str(x[0][0]) + '</Contnt>\n' + '\t<Contr>' + str(x[0][1]) + '</Contr>\n' + '\t<name>' + str(x[0][16]) + '</name>\n' + '\t<url>' + str(x[0][9]).replace('\n', '').replace('\t', '').replace('\r', '') + '</url>\n' + '\t<Id>' + str(x[0][10]) + '</Id>\n' + '</Contry>\n'
        name = str(x[0][16])
        XML_Replace_Line(Favo, name)

    outfile.write('</stream>')
    outfile.close()
    outfileo.close()
    outfileo.close()
    outfileoo.close()


def XML_AudioAthan(Mylist):
    Path = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/audiop.xml'
    os.remove(Path)
    outfile = open(Path, 'a')
    outfile.write('<?xml version="1.0"?>\n<stream>\n')
    for x in Mylist:
        outfile.write('<flash>\n\t<name>' + str(x[0][0]) + '</name>\n' + '\t<url>' + str(x[0][1]) + '</url>\n' + '</flash>\n')

    outfile.write('</stream>')
    outfile.close()


def XML_Replace_Line(line, name):
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/Favos.xml', 'r')
    chaine = f.read()
    f.close()
    if '<name>' + name + '</name>' in chaine:
        pass
    else:
        result = chaine.replace('</stream>', line + '</stream>')
        f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/Favos.xml', 'w')
        f.write(result)
        f.close()


def XML_Replace_Line_1(line):
    messg = ''
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/Favos.xml', 'r')
    chaine = f.read()
    f.close()
    if line in chaine:
        messg = 'Oui'
    else:
        messg = 'Non'
    return messg


def XML_Delet_Line_Favos(line):
    messg = ''
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/Favos.xml', 'r')
    chaine = f.read()
    f.close()
    result = chaine.replace(line, '')
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/Favos.xml', 'w')
    f.write(result)
    f.close()
    return messg


def Upcoming_Line():
    nomsalat = ''
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/Upcoming.txt', 'r')
    chaine = f.read()
    f.close()
    if chaine == 'Fajr':
        nomsalat = '\xd8\xa7\xd9\x84\xd9\x81\xd8\xac\xd8\xb1'
    elif chaine == 'Zuhr':
        nomsalat = '\xd8\xa7\xd9\x84\xd8\xb8\xd9\x87\xd8\xb1'
    elif chaine == 'Asr':
        nomsalat = '\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb5\xd8\xb1'
    elif chaine == 'Maghrb':
        nomsalat = '\xd8\xa7\xd9\x84\xd9\x85\xd8\xba\xd8\xb1\xd8\xa8'
    elif chaine == 'Esha':
        nomsalat = '\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb4\xd8\xa7\xd8\xa1'
    return nomsalat


class StreamURIParserAthanmenu_1:

    def __init__(self, xml):
        self.xml = xml

    def parseStreamListAthanmenu_1(self):
        Athanlist1 = []
        tree = ElementTree()
        tree.parse(self.xml)
        for Athan in tree.findall('Contry'):
            name = str(Athan.findtext('name'))
            url = str(Athan.findtext('url'))
            Id = str(Athan.findtext('Id'))
            Athanlist1.append({'name': name,
             'url': url,
             'Id': Id})

        return Athanlist1


class StreamURIParserAthanmenu_2:

    def __init__(self, xml):
        self.xml = xml

    def parseStreamListAthanmenu_2(self):
        Athanlist1 = []
        tree = ElementTree()
        tree.parse(self.xml)
        for Athan in tree.findall('Contry'):
            Contnt = str(Athan.findtext('Contnt'))
            Contr = str(Athan.findtext('Contr'))
            name = str(Athan.findtext('name'))
            url = str(Athan.findtext('url'))
            Id = str(Athan.findtext('Id'))
            Athanlist1.append({'Contnt': Contnt,
             'Contr': Contr,
             'name': name,
             'url': url,
             'Id': Id})

        return Athanlist1


class ParserAthanFlash:

    def __init__(self, xml):
        self.xml = xml

    def parseListAthanFlash(self):
        Athanlist1 = []
        tree = ElementTree()
        tree.parse(self.xml)
        for Athan in tree.findall('flash'):
            name = str(Athan.findtext('name'))
            url = str(Athan.findtext('url'))
            urimg = str(Athan.findtext('urimg'))
            Athanlist1.append({'name': name,
             'url': url,
             'urimg': urimg})

        return Athanlist1


class ParserAthanAyames:

    def __init__(self, xml):
        self.xml = xml

    def parseListAthanAyames(self):
        Athanlist1 = []
        tree = ElementTree()
        tree.parse(self.xml)
        for Athan in tree.findall('ayames'):
            name = str(Athan.findtext('name'))
            date1 = str(Athan.findtext('date1'))
            date2 = str(Athan.findtext('date2'))
            Athanlist1.append({'name': name,
             'date1': date1,
             'date2': date2})

        return Athanlist1


class StreamURIParserAthanmenu:

    def __init__(self, xml):
        self.xml = xml

    def parseStreamListAthanmenu(self):
        Athanlist1 = []
        tree = ElementTree()
        tree.parse(self.xml)
        for Athan in tree.findall('Choice'):
            Contnt = str(Athan.findtext('Contnt'))
            name = str(Athan.findtext('name'))
            Athanlist1.append({'Contnt': Contnt,
             'name': name})

        return Athanlist1


class StreamURIParserAthan:

    def __init__(self, xml):
        self.xml = xml

    def parseStreamListAthan(self):
        Athanlist = []
        im = 0
        tree = ElementTree()
        tree.parse(self.xml)
        for Athan in tree.findall('Choice'):
            Contnt = str(Athan.findtext('Contnt'))
            Contr = str(Athan.findtext('Contr'))
            fajr = str(Athan.findtext('fajr'))
            sunrise = str(Athan.findtext('sunrise'))
            dhuhr = str(Athan.findtext('dhuhr'))
            asr = str(Athan.findtext('asr'))
            maghrib = str(Athan.findtext('maghrib'))
            isha = str(Athan.findtext('isha'))
            qiyam = str(Athan.findtext('qiyam'))
            url = str(Athan.findtext('url'))
            Id = str(Athan.findtext('Id'))
            Lati = str(Athan.findtext('Lati'))
            Longit = str(Athan.findtext('Longit'))
            hijri = str(Athan.findtext('hijri'))
            clac = str(Athan.findtext('clac'))
            next = str(Athan.findtext('next'))
            bled = str(Athan.findtext('bled'))
            haiaa = str(Athan.findtext('haiaa'))
            WeatheId = str(Athan.findtext('WeatheId'))
            Athanlist.append({'Contnt': Contnt,
             'Contr': Contr,
             'fajr': fajr,
             'sunrise': sunrise,
             'sunrise': sunrise,
             'dhuhr': dhuhr,
             'asr': asr,
             'maghrib': maghrib,
             'isha': isha,
             'qiyam': qiyam,
             'url': url,
             'Id': Id,
             'Lati': Lati,
             'Longit': Longit,
             'hijri': hijri,
             'clac': clac,
             'next': next,
             'bled': bled,
             'haiaa': haiaa,
             'WeatheId': WeatheId})

        return Athanlist


def extr_url(cnd):
    HH = ''
    ecmf = open('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/Choice/Choice.txt', 'r')
    ecm = ecmf.readlines()
    for line in ecm:
        if cnd in line:
            HH = line.split('=')[1].replace('\n', '').replace('\t', '').replace('\r', '')
            if '=ar' in HH:
                HH = HH
            else:
                HH = HH + '=ar'

    return HH


def get_remaining_time(h, m):
    from datetime import datetime
    maintenant = datetime.now()
    H = maintenant.hour
    M = maintenant.minute
    S = maintenant.second
    if int(H) == 0:
        H = 24
    else:
        H = H
    if int(H) >= 12:
        if int(h) >= 12:
            Act_1 = int(H) * 60 + int(M)
            Act_2 = int(h) * 60 + int(m)
        if int(h) < 12:
            Act_1 = int(H) * 60 + int(M)
            Act_2 = (int(h) + 24) * 60 + int(m)
    else:
        Act_1 = int(H) * 60 + int(M)
        Act_2 = int(h) * 60 + int(m)
    rest = abs(Act_1 - Act_2)
    if rest >= 60:
        rest_1 = float(rest) / 60
        rest_2 = round(rest_1, 2)
        rest_3 = rest / 60
        rest_4 = (rest_2 - rest_3) * 60
        rest_4 = round(rest_4, 0)
        if rest_4 >= 60:
            rest_4 = rest_4 - 60
            rest = str(rest_3 + 1) + ' (h)\xd8\xb3\xd8\xa7 ' + ':' + str(format(rest_4, '.0f')) + ' (m)\xd8\xaf'
        else:
            rest = str(rest_3) + ' (h)\xd8\xb3\xd8\xa7 ' + ':' + str(format(rest_4, '.0f')) + ' (m)\xd8\xaf'
    else:
        rest = str(rest) + ' (m)\xd8\xaf '
    return str(rest) + ' '


def Change_times(txt):
    from Plugins.Extensions.AthanTimes.outils.Utils import get_remaining_time
    txt_1 = txt.split(':')[:1][0]
    txt_2 = txt.split(':')[1:][0]
    if 'PM' in txt_2:
        if int(txt.split(':')[:1][0]) < 12:
            txt_1 = int(txt.split(':')[:1][0]) + 12
            txt_2 = txt.split(':')[1:][0]
        else:
            txt_1 = txt.split(':')[:1][0]
            txt_2 = txt.split(':')[1:][0]
    if 'AM' in txt_2:
        txt_1 = txt.split(':')[:1][0]
        txt_2 = txt.split(':')[1:][0]
    return str(txt_1) + ':' + str(txt_2).replace('PM', '').replace('AM', '')


def Change_times_1(txt):
    txt_1 = txt.split(':')[:1][0]
    txt_2 = txt.split(':')[1:][0]
    return str(txt_1) + ':' + str(txt_2).replace('PM', '').replace('AM', '')


def Search_City(txt):
    from Plugins.Extensions.AthanTimes.outils.Utils import get_remaining_time
    txt_1 = txt.split(':')[:1][0]
    txt_2 = txt.split(':')[1:][0]
    if 'PM' in txt_2:
        if int(txt.split(':')[:1][0]) < 12:
            txt_1 = int(txt.split(':')[:1][0]) + 12
            txt_2 = txt.split(':')[1:][0]
        else:
            txt_1 = txt.split(':')[:1][0]
            txt_2 = txt.split(':')[1:][0]
    if 'AM' in txt_2:
        txt_1 = txt.split(':')[:1][0]
        txt_2 = txt.split(':')[1:][0]
    return str(txt_1) + ':' + str(txt_2).replace('PM', '').replace('AM', '')


class SearchAthan:

    def __init__(self, city, id):
        self.city = city
        self.id = id
        self.bilad = ''

    def SearchAthan_1(self):
        self.letter_list = []
        self.limit = 0
        main_url = 'https://www.islamicfinder.org/world/search-city?keyword=' + self.city + '&countryId=' + str(self.id)
        req = urllib2.Request(main_url)
        try:
            response = urllib2.urlopen(req)
            Test_page = response.read()
        except urllib2.HTTPError as e:
            print e.code
            Test_page = 'HTTP download ERROR: %s' % str(e.code)

        if Test_page.startswith('HTTP download ERROR:'):
            self.bilad = Test_page
        else:
            request = urllib2.Request(main_url, None, Agent)
            data = urllib2.urlopen(request).read()
            bilad = re.findall('"cityId":(.*?),"countryId":(.*?),"cityName":"(.*?)"', data)
            self.limit = len(bilad)
            for i in range(self.limit):
                try:
                    self.letter_list.append(show_listiptv2(bilad[i][2], bilad[i][0], bilad[i][1], ''))
                except IndexError:
                    pass

            if bilad == []:
                self.bilad = 'City Not Found'
            else:
                self.bilad = self.letter_list
        return self.bilad


def Search_idCtr(txt):
    idCtr = ''
    try:
        for line in open('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/countryId.txt'):
            if txt in line:
                idCtr = line.split('=')[1].replace('\n', '').replace('\t', '').replace(' ', '')

    except:
        return

    return idCtr


class SearchAthanConvert:

    def __init__(self, Day, Month, Year):
        self.Day = Day
        self.Month = Month
        self.Year = Year
        self.bilad = ''

    def SearchAthanConvert_1(self):
        self.limit = 0
        main_url = 'http://www.islamicfinder.org/dateConversion.php?mode=ger-hij&day=' + str(self.Day) + '&month=' + str(self.Month) + '&year=' + str(self.Year) + '&date_result=1&lang=arabic'
        req = urllib2.Request(main_url)
        try:
            response = urllib2.urlopen(req)
            Test_page = response.read()
        except urllib2.HTTPError as e:
            print e.code
            Test_page = 'HTTP download ERROR: %s' % str(e.code)

        if Test_page.startswith('HTTP download ERROR:'):
            self.bilad = Test_page
        else:
            request = urllib2.Request(main_url, None, Agent)
            data = urllib2.urlopen(request).read()
            bilad = re.findall('<span class="date-converted-date">(.+?)</span><span.+?class="date-converted-day">(.+?)</span><span class="note">.+?</span> <br>', data, re.S)
            self.limit = len(bilad)
            for i in range(self.limit):
                try:
                    self.bilad = Change_TXTDay(str(bilad[0][1])) + '_' + Change_TXT(str(bilad[0][0]))
                except IndexError:
                    pass

            if bilad == []:
                self.bilad = 'City Not Found'
            else:
                self.bilad = self.bilad
        return self.bilad


def Change_TXT(txt):
    TXT = txt
    if '\xd9\x85\xd8\xad\xd8\xb1\xd9\x85' in TXT:
        TXT = TXT.replace('\xd9\x85\xd8\xad\xd8\xb1\xd9\x85', '\xd9\x85\xd8\xad\xd8\xb1\xd9\x85_Muharram_')
    elif '\xd8\xb5\xd9\x81\xd8\xb1' in TXT:
        TXT = TXT.replace('\xd8\xb5\xd9\x81\xd8\xb1', '\xd8\xb5\xd9\x81\xd8\xb1_Safar_')
    elif '\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xb9 \xd8\xa7\xd9\x84\xd8\xa3\xd9\x88\xd9\x84' in TXT:
        TXT = TXT.replace('\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xb9 \xd8\xa7\xd9\x84\xd8\xa3\xd9\x88\xd9\x84', '\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xb9 \xd8\xa7\xd9\x84\xd8\xa3\xd9\x88\xd9\x84_Rabi Al-Awwal_')
    elif '\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xb9 \xd8\xa7\xd9\x84\xd8\xa2\xd8\xae\xd8\xb1\xd8\xa9' in TXT:
        TXT = TXT.replace('\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xb9 \xd8\xa7\xd9\x84\xd8\xa2\xd8\xae\xd8\xb1\xd8\xa9', '\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xb9 \xd8\xa7\xd9\x84\xd8\xa2\xd8\xae\xd8\xb1\xd8\xa9_Rabi Al-Akhar_')
    elif '\xd8\xac\xd9\x85\xd8\xa7\xd8\xaf\xd9\x89 \xd8\xa7\xd9\x84\xd8\xa3\xd9\x88\xd9\x84\xd9\x89' in TXT:
        TXT = TXT.replace('\xd8\xac\xd9\x85\xd8\xa7\xd8\xaf\xd9\x89 \xd8\xa7\xd9\x84\xd8\xa3\xd9\x88\xd9\x84\xd9\x89', '\xd8\xac\xd9\x85\xd8\xa7\xd8\xaf\xd9\x89 \xd8\xa7\xd9\x84\xd8\xa3\xd9\x88\xd9\x84\xd9\x89_Jumada Al-Awwal_')
    elif '\xd8\xac\xd9\x85\xd8\xa7\xd8\xaf\xd9\x89 \xd8\xa7\xd9\x84\xd8\xa2\xd8\xae\xd8\xb1\xd8\xa9' in TXT:
        TXT = TXT.replace('\xd8\xac\xd9\x85\xd8\xa7\xd8\xaf\xd9\x89 \xd8\xa7\xd9\x84\xd8\xa2\xd8\xae\xd8\xb1\xd8\xa9', '\xd8\xac\xd9\x85\xd8\xa7\xd8\xaf\xd9\x89 \xd8\xa7\xd9\x84\xd8\xa2\xd8\xae\xd8\xb1\xd8\xa9_Jumada Al-Akhirah_')
    elif '\xd8\xb1\xd8\xac\xd8\xa8' in TXT:
        TXT = TXT.replace('\xd8\xb1\xd8\xac\xd8\xa8', '\xd8\xb1\xd8\xac\xd8\xa8_Rajab_')
    elif '\xd8\xb4\xd8\xb9\xd8\xa8\xd8\xa7\xd9\x86' in TXT:
        TXT = TXT.replace('\xd8\xb4\xd8\xb9\xd8\xa8\xd8\xa7\xd9\x86', '\xd8\xb4\xd8\xb9\xd8\xa8\xd8\xa7\xd9\x86_Shaban_')
    elif '\xd8\xb1\xd9\x85\xd8\xb6\xd8\xa7\xd9\x86' in TXT:
        TXT = TXT.replace('\xd8\xb1\xd9\x85\xd8\xb6\xd8\xa7\xd9\x86', '\xd8\xb1\xd9\x85\xd8\xb6\xd8\xa7\xd9\x86_Ramadan_')
    elif '\xd8\xb4\xd9\x88\xd8\xa7\xd9\x84' in TXT:
        TXT = TXT.replace('\xd8\xb4\xd9\x88\xd8\xa7\xd9\x84', '\xd8\xb4\xd9\x88\xd8\xa7\xd9\x84_Shawwal_')
    elif '\xd8\xb0\xd9\x8a \xd8\xa7\xd9\x84\xd9\x82\xd8\xb9\xd8\xaf\xd8\xa9' in TXT:
        TXT = TXT.replace('\xd8\xb0\xd9\x8a \xd8\xa7\xd9\x84\xd9\x82\xd8\xb9\xd8\xaf\xd8\xa9', '\xd8\xb0\xd9\x8a \xd8\xa7\xd9\x84\xd9\x82\xd8\xb9\xd8\xaf\xd8\xa9_Dhul Qadah_')
    elif '\xd8\xb0\xd9\x8a \xd8\xa7\xd9\x84\xd8\xad\xd8\xac\xd8\xa9' in TXT:
        TXT = TXT.replace('\xd8\xb0\xd9\x8a \xd8\xa7\xd9\x84\xd8\xad\xd8\xac\xd8\xa9', '\xd8\xb0\xd9\x8a \xd8\xa7\xd9\x84\xd8\xad\xd8\xac\xd8\xa9_Dhul Hiijah_')
    else:
        TXT = TXT
    return TXT


def Change_TXTDay(txt):
    TXT = txt
    if '\xd8\xa7\xd9\x84\xd8\xac\xd9\x85\xd8\xb9\xd8\xa9' in TXT:
        TXT = TXT.replace('\xd8\xa7\xd9\x84\xd8\xac\xd9\x85\xd8\xb9\xd8\xa9', '\xd8\xa7\xd9\x84\xd8\xac\xd9\x85\xd8\xb9\xd8\xa9_Friday_')
    elif '\xd8\xa7\xd9\x84\xd8\xb3\xd8\xa8\xd8\xaa' in TXT:
        TXT = TXT.replace('\xd8\xa7\xd9\x84\xd8\xb3\xd8\xa8\xd8\xaa', '\xd8\xa7\xd9\x84\xd8\xb3\xd8\xa8\xd8\xaa_Saturday_')
    elif '\xd8\xa7\xd9\x84\xd8\xa3\xd8\xad\xd8\xaf' in TXT:
        TXT = TXT.replace('\xd8\xa7\xd9\x84\xd8\xa3\xd8\xad\xd8\xaf', '\xd8\xa7\xd9\x84\xd8\xa3\xd8\xad\xd8\xaf_Sunday_')
    elif '\xd8\xa7\xd9\x84\xd8\xa7\xd8\xab\xd9\x86\xd9\x8a\xd9\x86' in TXT:
        TXT = TXT.replace('\xd8\xa7\xd9\x84\xd8\xa7\xd8\xab\xd9\x86\xd9\x8a\xd9\x86', '\xd8\xa7\xd9\x84\xd8\xa7\xd8\xab\xd9\x86\xd9\x8a\xd9\x86_Monday_')
    elif '\xd8\xa7\xd9\x84\xd8\xab\xd9\x84\xd8\xa7\xd8\xab\xd8\xa7\xd8\xa1' in TXT:
        TXT = TXT.replace('\xd8\xa7\xd9\x84\xd8\xab\xd9\x84\xd8\xa7\xd8\xab\xd8\xa7\xd8\xa1', '\xd8\xa7\xd9\x84\xd8\xab\xd9\x84\xd8\xa7\xd8\xab\xd8\xa7\xd8\xa1_Tuesday_')
    elif '\xd8\xa7\xd9\x84\xd8\xa3\xd8\xb1\xd8\xa8\xd8\xb9\xd8\xa7\xd8\xa1' in TXT:
        TXT = TXT.replace('\xd8\xa7\xd9\x84\xd8\xa3\xd8\xb1\xd8\xa8\xd8\xb9\xd8\xa7\xd8\xa1', '\xd8\xa7\xd9\x84\xd8\xa3\xd8\xb1\xd8\xa8\xd8\xb9\xd8\xa7\xd8\xa1_Wednesday_')
    elif '\xd8\xa7\xd9\x84\xd8\xae\xd9\x85\xd9\x8a\xd8\xb3' in TXT:
        TXT = TXT.replace('\xd8\xa7\xd9\x84\xd8\xae\xd9\x85\xd9\x8a\xd8\xb3', '\xd8\xa7\xd9\x84\xd8\xae\xd9\x85\xd9\x8a\xd8\xb3_Thursday_')
    else:
        TXT = TXT
    return TXT


def Change_TXTDay_2(txt):
    TXT = txt
    if 'Friday' in TXT:
        TXT = TXT.replace('Friday', '_Friday_\xd8\xa7\xd9\x84\xd8\xac\xd9\x85\xd8\xb9\xd8\xa9')
    elif 'Saturday' in TXT:
        TXT = TXT.replace('Saturday', '_Saturday_\xd8\xa7\xd9\x84\xd8\xb3\xd8\xa8\xd8\xaa')
    elif 'Sunday' in TXT:
        TXT = TXT.replace('Sunday', '_Sunday_\xd8\xa7\xd9\x84\xd8\xa3\xd8\xad\xd8\xaf')
    elif 'Monday' in TXT:
        TXT = TXT.replace('Monday', '\xd8\xa7\xd9\x84\xd8\xa7\xd8\xab\xd9\x86\xd9\x8a\xd9\x86_Monday_')
    elif 'Tuesday' in TXT:
        TXT = TXT.replace('Tuesday', '_Tuesday_\xd8\xa7\xd9\x84\xd8\xab\xd9\x84\xd8\xa7\xd8\xab\xd8\xa7\xd8\xa1')
    elif 'Wednesday' in TXT:
        TXT = TXT.replace('Wednesday', '_Wednesday_\xd8\xa7\xd9\x84\xd8\xa3\xd8\xb1\xd8\xa8\xd8\xb9\xd8\xa7\xd8\xa1')
    elif 'Thursday' in TXT:
        TXT = TXT.replace('Thursday', '_Thursday_\xd8\xa7\xd9\x84\xd8\xae\xd9\x85\xd9\x8a\xd8\xb3')
    elif 'Mardi' in TXT:
        TXT = TXT.replace('Mardi', '_Mardi_\xd8\xa7\xd9\x84\xd8\xab\xd9\x84\xd8\xa7\xd8\xab\xd8\xa7\xd8\xa1')
    elif 'Mercredi' in TXT:
        TXT = TXT.replace('Mercredi', '_Mercredi_\xd8\xa7\xd9\x84\xd8\xa7\xd8\xb1\xd8\xa8\xd8\xb9\xd8\xa7\xd8\xa1')
    elif 'Jeudi' in TXT:
        TXT = TXT.replace('Jeudi', '_Jeudi_\xd8\xa7\xd9\x84\xd8\xae\xd9\x85\xd9\x8a\xd8\xb3')
    elif 'Vendredi' in TXT:
        TXT = TXT.replace('Vendredi', '_Vendredi_\xd8\xa7\xd9\x84\xd8\xac\xd9\x85\xd8\xb9\xd8\xa9')
    elif 'Samedi' in TXT:
        TXT = TXT.replace('Samedi', '_Samedi_\xd8\xa7\xd9\x84\xd8\xb3\xd8\xa8\xd8\xaa')
    elif 'Dimanche' in TXT:
        TXT = TXT.replace('Dimanche', '_Dimanche_\xd8\xa7\xd9\x84\xd8\xa7\xd8\xad\xd8\xaf')
    elif 'Lundi' in TXT:
        TXT = TXT.replace('Lundi', '_Lundi_\xd8\xa7\xd9\x84\xd8\xa7\xd8\xab\xd9\x86\xd9\x8a\xd9\x86')
    else:
        TXT = TXT
    return TXT


def Copyurlvideo(txt):
    Path = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/video.txt'
    os.remove(Path)
    outfile = open(Path, 'a')
    outfile.write('url =' + txt)
    outfile.close()
    return 'Video link recorded   \xd8\xaa\xd9\x85 \xd8\xaa\xd8\xb3\xd8\xac\xd9\x8a\xd9\x84 \xd8\xb1\xd8\xa7\xd8\xa8\xd8\xb7 \xd8\xa7\xd9\x84\xd9\x81\xd9\x8a\xd8\xaf\xd9\x8a\xd9\x88'


class SearchAthanWeather:

    def __init__(self, city, contr):
        self.city = city
        self.contr = contr
        self.bilad = ''

    def SearchWeather(self):
        if self.city == 'Algiers' or self.city == '\xd8\xa7\xd9\x84\xd8\xac\xd8\xb2\xd8\xa7\xd8\xa6\xd8\xb1' or self.city == 'Alger' or self.city == 'Algiers Bay' or self.city == 'Algiers Station':
            self.bilad = str(1253079)
            CopyidWeathe(self.bilad)
        else:
            main_url = 'https://www.yahoo.com/news/_td/api/resource/WeatherSearch;text=%s' % self.city.replace(' ', '%20')
            req = urllib2.Request(main_url)
            try:
                response = urllib2.urlopen(req)
                Test_page = response.read()
            except urllib2.HTTPError as e:
                print e.code
                Test_page = 'HTTP download ERROR: %s' % str(e.code)

            if Test_page.startswith('HTTP download ERROR:'):
                self.bilad = Test_page
                CopyidWeathe('City Not Found')
            else:
                request = urllib2.Request(main_url, None, Agent)
                data = urllib2.urlopen(request).read()
                bilado = re.findall('woeid":(.+?),"lat":.*?,"lon":.*?,"country":"' + self.contr + '"', data)
            if bilado == [] or len(bilado) == 0:
                self.bilad = 'City Not Found'
                CopyidWeathe(self.bilad)
            else:
                self.bilad = str(bilado[0])
                CopyidWeathe(self.bilad)
        return


def CopyidWeathe(txt):
    Path = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/outils/YahooWeather/Config/Location_id'
    os.remove(Path)
    outfile = open(Path, 'a')
    outfile.write(txt)
    outfile.close()
    XML_ADD_Line_WeatheId(txt)


def XML_ADD_Line_WeatheId(line):
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes.xml', 'r')
    chaine = f.read()
    f.close()
    result = chaine.replace('</Choice>', '\t<WeatheId>' + str(line) + '</WeatheId>\n</Choice>')
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes.xml', 'w')
    f.write(result)
    f.close()


def Prayer_txt(a, b, c, d, e, f, g):
    Patho = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Prayer.txt'
    os.remove(Patho)
    outfileo = open(Patho, 'a')
    outfileo.write(a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n' + f + '\n' + g)
    outfileo.close()


def XML_Choice_Contr_bled(Mylist):
    ZZZ = ''
    for x in Mylist:
        ZZZ = str(x[0][1]) + '\n' + str(x[0][16])

    return ZZZ


def Import_times_Salat(a):
    ptimesfile = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Prayer.txt'
    ptfile = open(ptimesfile, 'r')
    data = ptfile.readlines()
    ptfile.close()
    country = str(data[0]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    city = str(data[1]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    fajr = str(data[2]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    sunrise = str(data[3]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    dhur = str(data[4]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    asr = str(data[5]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    maghrib = str(data[6]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    isha = str(data[7]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    if a == 'fajr':
        return fajr
    if a == 'sunrise':
        return sunrise
    if a == 'dhur' or a == 'dhuhr' or a == 'Zuhr':
        return dhur
    if a == 'asr':
        return asr
    if a == 'maghrib':
        return maghrib
    if a == 'isha':
        return isha


def Import_times_Upadat_Salat():
    ptimesfile = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Prayer.txt'
    ptfile = open(ptimesfile, 'r')
    data = ptfile.readlines()
    ptfile.close()
    fajr = str(data[2]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    f = []
    f = fajr.split(':')
    fhour = f[0]
    fminute = f[1]
    fajr_1 = [fhour, fminute]
    sunrise = str(data[3]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    g = []
    g = sunrise.split(':')
    ghour = g[0]
    gminute = g[1]
    sunrise_1 = [ghour, gminute]
    dhur = str(data[4]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    h = []
    h = dhur.split(':')
    hhour = h[0]
    hminute = h[1]
    dhur_1 = [hhour, hminute]
    asr = str(data[5]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    i = []
    i = asr.split(':')
    ihour = i[0]
    iminute = i[1]
    asr_1 = [ihour, iminute]
    maghrib = str(data[6]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    j = []
    j = maghrib.split(':')
    jhour = j[0]
    jminute = j[1]
    maghrib_1 = [jhour, jminute]
    isha = str(data[7]).replace('\n', '').replace('\t', '').replace('\r', '').replace(' ', '')
    k = []
    k = isha.split(':')
    khour = k[0]
    kminute = k[1]
    isha_1 = [khour, kminute]
    return (fajr_1,
     sunrise_1,
     dhur_1,
     asr_1,
     maghrib_1,
     isha_1)


def Nmbrs_lines():
    if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/messageupdat.txt'):
        file = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/messageupdat.txt'
        n = sum((1 for _ in open(file)))
        return n
    else:
        return 0


def Nmbrs_lines_2():
    if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/Times.txt'):
        file = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/Times.txt'
        n = sum((1 for _ in open(file)))
        return n
    else:
        return 0


def Import_Datetime_Updat():
    message_1 = ''
    message_2 = ''
    message_3 = ''
    message_4 = ''
    n = Nmbrs_lines()
    if int(n) != 0:
        ptimesfile = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/messageupdat.txt'
        ptfile = open(ptimesfile, 'r')
        data = ptfile.readlines()
        ptfile.close()
        message_1 = str(data[0]).replace('\n', '').replace('\t', '').replace('\r', '')
        message_2 = str(data[1]).replace('\n', '').replace('\t', '').replace('\r', '')
        if int(message_2) < 10:
            message_2 = '0' + str(message_2)
        message_3 = str(data[2]).replace('\n', '').replace('\t', '').replace('\r', '')
        if int(message_3) < 10:
            message_3 = '0' + str(message_3)
        message_4 = str(data[3]).replace('\n', '').replace('\t', '').replace('\r', '')
        return (message_1,
         message_2,
         message_3,
         message_4)
    else:
        message_1 = '....'
        message_2 = '....'
        message_3 = '....'
        message_4 = '....'
        return (message_1,
         message_2,
         message_3,
         message_4)


def Import_time_Updat():
    timupdat = ''
    ptimesfile = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/Times.txt'
    ptfile = open(ptimesfile, 'r')
    data = ptfile.readlines()
    ptfile.close()
    n = Nmbrs_lines_2()
    if int(n) != 0:
        timupdat = str(data[0]).replace('\n', '').replace('\t', '').replace('\r', '')
    else:
        timupdat = ''
    return timupdat


def Replace_time_Line_Updat(line):
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/ChoiceTime.txt', 'r')
    chaine = f.readlines()
    f.close()
    lin0 = chaine[0].replace('\n', '').replace('\t', '').replace('\r', '')
    lin1 = chaine[1].replace('\n', '').replace('\t', '').replace('\r', '')
    lin2 = chaine[2].replace('\n', '').replace('\t', '').replace('\r', '')
    lin3 = chaine[3].replace('\n', '').replace('\t', '').replace('\r', '')
    lin4 = chaine[4].replace('\n', '').replace('\t', '').replace('\r', '')
    lin4 = lin4.replace(lin4, 'timeupdat=' + str(line))
    result = lin0 + '\n' + lin1 + '\n' + lin2 + '\n' + lin3 + '\n' + lin4
    f = file('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/PrayerTimes/ChoiceTime.txt', 'w')
    f.write(result)
    f.close()


def ImportDataInfos(data):
    import re
    data = data
    bilad = re.findall("<link rel='canonical' href='https://www.islamicfinder.org/world/.*?/.*?/(.*?)/?language=ar'></link>", data)[0]
    bilad = bilad.replace('-prayer-times', '').replace('/', '').replace('?', '')
    fajr = re.findall('<div class="prayerTiles fajar-tile">.+?<span class="prayername ">.+?</span>.+?<span class="prayertime">(.+?)</span>', data, re.S)
    sunrise = re.findall('<div class="prayerTiles sunrise-tile">.+?<span class="prayername">.+?</span>.+?<span class="prayertime">(.+?)</span>', data, re.S)
    dhuhr = re.findall('<div class="prayerTiles dhuhar-tile">.+?<span class="prayername">.+?</span>.+?<span class="prayertime">(.+?)</span>', data, re.S)
    asr = re.findall('<div class="prayerTiles asr-tile">.+?<span class="prayername">.+?</span>.+?<span class="prayertime">(.+?)</span>', data, re.S)
    maghrib = re.findall('<div class="prayerTiles maghrib-tile">.+?<span class="prayername">.+?</span>.+?<span class="prayertime">(.+?)</span>', data, re.S)
    isha = re.findall('<div class="prayerTiles isha-tile">.+?<span class="prayername">.+?</span>.+?<span class="prayertime">(.+?)</span>', data, re.S)
    qiyam = ['02:18 AM']
    Id = re.findall('"locationId": "(.+?)",', data)
    haiaa = re.findall('<p class="font-sm font-dark">(.+?)<a class=".+?" title="\xd8\xaa\xd8\xba\xd9\x8a\xd9\x8a\xd8\xb1 \xd8\xa7\xd9\x84\xd8\xa5\xd8\xb9\xd8\xaf\xd8\xa7\xd8\xaf\xd8\xa7\xd8\xaa">\xd9\x8a\xd8\xaa\xd8\xba\xd9\x8a\xd8\xb1\xd9\x88\xd9\x86</a>', data.encode('utf-8'), re.S)
    haiaa = haiaa[0].replace('\n', '').replace('\t', '').replace('\r', '').replace('&nbsp;', '')
    Calc = re.findall('<p class="font-xs font-muted">(.+?)<span class', data.encode('utf-8'), re.S)
    Calc = Calc[0].replace('&nbsp;', ' ').replace('\n', '').replace('\t', '').replace('\r', '')
    hijri = re.findall('<p class="font-weight-bold pt-date-right">(.+?)</p>', data)[0]
    hijri = hijri.replace('&nbsp;', ' ')
    NextSalat = re.findall('"nextPrayer": "lang.(.+?)", "nextPrayerRemainingTime": "(.+?):(.+?):.+?",', data, re.S)
    Posit = re.findall('id="user-manual-latitude" placeholder=.+?value="(.+?)".+?id="user-manual-longitude" placeholder=.+?name="Longitute" value="(.+?)"', data.encode('utf-8'), re.S)
    return (bilad,
     fajr,
     sunrise,
     dhuhr,
     asr,
     maghrib,
     isha,
     qiyam,
     Id,
     haiaa,
     Calc,
     Calc,
     hijri,
     NextSalat,
     Posit)


def show_listiptv0(h, p, u, pw):
    png = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Decos/menu-Contry.png'
    if dwidth == 1280:
        res = [(h,
          p,
          u,
          pw)]
        res.append(MultiContentEntryPixmapAlphaTest(pos=(2, 2), size=(380, 31), png=loadPNG(png)))
        res.append(MultiContentEntryText(pos=(45, 2), size=(380, 31), font=8, text=h, flags=RT_HALIGN_CENTER))
        return res
    else:
        res = [(h,
          p,
          u,
          pw)]
        res.append(MultiContentEntryPixmapAlphaTest(pos=(2, 2), size=(380, 31), png=loadPNG(png)))
        res.append(MultiContentEntryText(pos=(45, 2), size=(380, 31), font=8, text=h, flags=RT_HALIGN_CENTER))
        return res


def show_listiptv(h, p, u, pw):
    if dwidth == 1280:
        res = [(h,
          p,
          u,
          pw)]
        if 'Free Server Cccam' in h:
            res.append(MultiContentEntryText(pos=(2, 2), size=(425, 30), font=5, text=h, backcolor_sel=26214, backcolor=22503, flags=RT_HALIGN_CENTER))
            return res
        else:
            res.append(MultiContentEntryText(pos=(2, 2), size=(425, 30), font=5, text=h, backcolor_sel=26214, backcolor=1090519040, flags=RT_HALIGN_CENTER))
            return res
    else:
        res = [(h,
          p,
          u,
          pw)]
        if 'Free Server Cccam' in h:
            res.append(MultiContentEntryText(pos=(2, 2), size=(402, 30), font=7, text=h, backcolor_sel=26214, backcolor=22503, flags=RT_HALIGN_CENTER))
            return res
        res.append(MultiContentEntryText(pos=(2, 2), size=(402, 30), font=7, text=h, backcolor_sel=26214, backcolor=1090519040, flags=RT_HALIGN_CENTER))
        return res


def streamListEntry_2(entry):
    uriInfo = entry[1].get('name')
    return [entry, (eListboxPythonMultiContent.TYPE_TEXT,
      34,
      4,
      380,
      31,
      0,
      RT_HALIGN_LEFT,
      entry[0])]


class m2list(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        self.l.setFont(0, gFont('Regular', 14))
        self.l.setFont(1, gFont('Regular', 16))
        self.l.setFont(2, gFont('Regular', 18))
        self.l.setFont(3, gFont('Regular', 20))
        self.l.setFont(4, gFont('Regular', 22))
        self.l.setFont(5, gFont('Regular', 24))
        self.l.setFont(6, gFont('Regular', 26))
        self.l.setFont(7, gFont('Regular', 28))
        self.l.setFont(8, gFont('Regular', 30))


def show_listiptv1(Contnt, Contr, fajr, sunrise, dhuhr, asr, maghrib, isha, qiyam, urlop, Id, Posit1, Posit2, hijri, Calcule, Next, bilad, haiaa):
    if dwidth == 1280:
        res = [(Contnt,
          Contr,
          fajr,
          sunrise,
          dhuhr,
          asr,
          maghrib,
          isha,
          qiyam,
          urlop,
          Id,
          Posit1,
          Posit2,
          hijri,
          Calcule,
          Next,
          bilad,
          haiaa)]
        res.append(MultiContentEntryText(pos=(2, 2), size=(425, 30), font=5, text=Contnt, backcolor_sel=26214, backcolor=22503, flags=RT_HALIGN_CENTER))
        return res
    else:
        res = [(Contnt,
          Contr,
          fajr,
          sunrise,
          dhuhr,
          asr,
          maghrib,
          isha,
          qiyam,
          urlop,
          Id,
          Posit1,
          Posit2,
          hijri,
          Calcule,
          Next,
          bilad,
          haiaa)]
        res.append(MultiContentEntryText(pos=(2, 2), size=(459, 30), font=7, text=Contnt, backcolor_sel=26214, backcolor=22503, flags=RT_HALIGN_CENTER))
        return res


def streamListEntry(entry):
    uriInfo = entry[1].get('url')
    return [entry, (eListboxPythonMultiContent.TYPE_TEXT,
      80,
      15,
      880,
      50,
      0,
      RT_HALIGN_CENTER,
      entry[0])]


def openfile():
    try:
        fp = open('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/city.txt', 'r')
        line = fp.read()
        fp.close()
        return line
    except:
        cname = 'none'
        return cname


def geturlvideo():
    urlname = ''
    pathname = open('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/video.txt', 'r')
    getname = pathname.readlines()
    for line in getname:
        if 'url' in line:
            urlname = line.split('=')[1].replace('\n', '').replace('\t', '').replace('\r', '')

    return urlname


def Verif():
    verifrslt = ''
    if fileExists('/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/audio/adhan.mp3'):
        verifrslt = 'yes'
    else:
        verifrslt = 'no'
    return verifrslt


def Upcoming(txt):
    Path = '/usr/lib/enigma2/python/Plugins/Extensions/AthanTimes/Flash/Upcoming.txt'
    if fileExists(Path):
        os.remove(Path)
        outfile = open(Path, 'a')
        outfile.write(txt)
        outfile.close()


def Verif_1(Valist):
    if Valist[0] < 10:
        if Valist[1] < 10:
            Valist = ['0' + str(Valist[0]), '0' + str(Valist[1])]
        else:
            Valist = ['0' + str(Valist[0]), Valist[1]]
    elif Valist[1] < 10:
        Valist = [Valist[0], '0' + str(Valist[1])]
    else:
        Valist = [Valist[0], Valist[1]]
    return Valist