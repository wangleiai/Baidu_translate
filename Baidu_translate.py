#!/home/qyy/anaconda3/envs/funny/bin/python
import requests
import execjs
import re
import sys
import urwid
from random import randint
# requests headers
headers = {
  "Accept": "*/*",
  "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
  "Connection": "keep-alive",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",    
  "Host": "fanyi.baidu.com",
  "Origin": "https://fanyi.baidu.com",
  "Referer": "https://fanyi.baidu.com/",
  "Cookie": "locale=zh; BAIDUID=4D1795733CF65210374C9F0A8D3AB8F6:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1552131929,1552132277,1552136868; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1552163067; delPer=0; PSINO=6; BIDUPSID=477B30916C56697D5F3B9E08382BC0ED; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1433_21106_28608_28584_28641_26350_28519_28627_28605; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1552166521",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

# widths tables for calculate string length
widths = [
  (126,  1), (159,  0), (687,   1), (710,  0), (711,  1),
  (727,  0), (733,  1), (879,   0), (1154, 1), (1161, 0),
  (4347,  1), (4447,  2), (7467,  1), (7521, 0), (8369, 1),
  (8426,  0), (9000,  1), (9002,  2), (11021, 1), (12350, 2),
  (12351, 1), (12438, 2), (12442,  0), (19893, 2), (19967, 1),
  (55203, 2), (63743, 1), (64106,  2), (65039, 1), (65059, 0),
  (65131, 2), (65279, 1), (65376,  2), (65500, 1), (65510, 2),
  (120831, 1), (262141, 2), (1114109, 1),
]

# check language
def is_Chinese(word):
  for ch in word:
      if '\u4e00' <= ch <= '\u9fff':
          return True
  return False

def get_token_and_gtk(session):
  # get token and gtk value from target web page's source code 
  url = 'https://fanyi.baidu.com/'
  session.get(url=url)
  response = session.get(url=url)
  token = re.findall(r"token: '(.*?)'", response.text)[0]
  gtk = re.findall(r"window.gtk = '(.*?)'", response.text)[0]
  return [token, gtk]

def get_response(session):
  jsCode = r"""
  function n (r, o) {
    for (var t = 0; t < o.length - 2; t += 3) {
      var a = o.charAt(t + 2)
      a = a >= 'a' ? a.charCodeAt(0) - 87 : Number(a), a = '+' === o.charAt(t + 1) ? r >>> a : r << a, r = '+' === o.charAt(t) ? r + a & 4294967295 : r ^ a
    } return r
  }

  function e (r) {
    var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g)
    if (null === o) {
      var t = r.length
      t > 30 && (r = '' + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
    } else {
      for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)'' !== e[C] && f.push.apply(f, a(e[C].split(''))), C !== h - 1 && f.push(o[C])
      var g = f.length
      g > 30 && (r = f.slice(0, 10).join('') + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join('') + f.slice(-10).join(''))
    } var u = void 0, l = '' + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107)
    u = null !== i ? i : (i = window[l] || '') || ''
    for (var d = u.split('.'), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
      var A = r.charCodeAt(v)
      128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)), S[c++] = A >> 18 | 240, S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224, S[c++] = A >> 6 & 63 | 128), S[c++] = 63 & A | 128)
    } for (var p = m, F = '' + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ('' + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = '' + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ('' + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ('' + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)p += S[b], p = n(p, F)
    return p = n(p, D), p ^= s, 0 > p && (p = (2147483647 & p) + 2147483648), p %= 1e6, p.toString() + '.' + (p ^ m)
  }
  """
  argv = sys.argv[1:]
  query = ' '.join(argv)
  token, gtk = get_token_and_gtk(session)
  jsCodeWithGtk = "var i = '{0}'".format(gtk)
  jsCode = jsCodeWithGtk + jsCode 
  sign = execjs.compile(jsCode).call('e', query)
  from_is_zh = is_Chinese(query)
  
  formData = {
    "from": "zh" if from_is_zh else 'en',
    "to": "en" if from_is_zh else 'zh',
    "query": query,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": sign,
    "token": token
  }
  des_url = 'https://fanyi.baidu.com/v2transapi'
  response = session.post(url=des_url, data=formData)
  status_code = f"\033[1;37;40m{response.status_code}\033[0m"
  query_value = f"\033[1;37;40m{query}\033[0m"
  print(f'\nStatus_code：{status_code}\t\t\tQuery: {query_value}')
  # print(response.text)
  return response.json(), from_is_zh

def get_width( o ):
  """Return the screen column width for unicode ordinal o."""
  global widths
  if o == 0xe or o == 0xf:
    return 0
  for num, wid in widths:
    if o <= num:
      return wid
  return 1

def get_result(response, from_is_zh=True):   
  max_length = 50
  result_data = []
  # multi words
  is_multi_words = response.get('dict_result') == []
  if not is_multi_words:
    if from_is_zh:
      print('中文')
      means = response.get('dict_result').get('simple_means').get('symbols')[0].get('parts')
      means = means[0].get('means')
    else:
      means = response.get('dict_result').get('simple_means').get('symbols')[0].get('parts')

    for i in means:
      if 'means' in i:
        single_line = i['part']+','.join(i['means'])
      else:
        continue
      single_line_length = 0
      for i in single_line:
        single_line_length += get_width(ord(i))
      if max_length < single_line_length:
        max_length = single_line_length
      result_data.append([single_line, single_line_length])
    # trans_result.data[""0""].dst
    # main transfer result
    mail_transfer_result = response.get('trans_result').get('data')[0].get('dst')
    print(f"\033[1;37;40m\nMain: {mail_transfer_result}\033[0m\n")
    print('-'*(max_length+4))
    for i in result_data:
      line = '| '+i[0]+' '*(max_length-i[1]) + ' |'
      space_line = '| ' + ' '*max_length + ' |'
      random_color_value = randint(31, 37)
      print(f"\033[0;{random_color_value};40m{line}\033[0m")  
      print(f"\033[0;{random_color_value};40m{space_line}\033[0m")
    print('-'*(max_length+4), '\n')
  else:
    #   multi words
    #   trans_result.data[""0""].dst
    mail_transfer_result = response.get('trans_result').get('data')[0].get('dst')
    print(f"\033[1;37;40m\nMain: {mail_transfer_result}\033[0m\n")

def run():
  if len(sys.argv) == 1 or '-h' in sys.argv:
    print('\t\tcha Usage:\tcha [your words]')
    print('\tExample:')
    print('\t1. cha lucky\n\t2. cha 真是丑陋的内心啊\n\t3. cha I am here')
    sys.exit(-1)
    
  # session: keep headers and cookies effective
  session = requests.Session()
  # session.headers = headers
  response, from_is_zh = get_response(session)
  get_result(response, from_is_zh)
  

if __name__ == "__main__":
  run()
