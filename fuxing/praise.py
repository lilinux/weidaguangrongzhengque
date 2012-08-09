from base64 import decodestring
import locale

head = '5Lit5Y2O5rCR5peP5q2j5Zyo6YKj5ZWlLi4u'
tail = (
'5Lit5Y2O5rCR5peP5bey6aG65Yip5a6M5oiQ5pmu6YCa5aSN5YW05ZKM5paH6Im65aSN5YW05Lul'
'5aSW55qE56ys5LiJ56eN5aSN5YW077yM5oSf6LCi6L+Z5Lus5aSa5bm05p2l5L2g5Lus55qE5b+N'
'6ICQ')
interupt = '5oKo5oiW6K645LiN57uP5oSP55qE5Li+5Yqo5ouv5pWR5LqG5Lit5Y2O5rCR5peP'
error = '5aaC6Iul5YaN54qv77yM5Yu/6LCT6KiA5LmL5LiN6aKE5Lmf77yB'

head = decodestring(head)
tail = decodestring(tail)
interupt = decodestring(interupt)
error = decodestring(error)

transcode = lambda s: s.decode('utf-8').encode('gbk')

if locale.getpreferredencoding() != 'UTF-8':
    head = transcode(head)
    tail = transcode(tail)
    interupt = transcode(interupt)
    error = transcode(error)


