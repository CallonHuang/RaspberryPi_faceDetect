API_KEY = "UlV94eEcopnWrufrxwAX7S2LrkhESAL0"
API_SECRET = "uR3wTHOmRDuX456LxhVYvUB6KcCTromL"

api_server_china = 'https://api-cn.faceplusplus.com/facepp/v3/'

face_will_lee = './faceset/will_lee.png'
face_rl_cui = './faceset/rl_cui.png'
face_yulu_hu = './faceset/yulu_hu.png'
face_ming_xie = './faceset/ming_xie.png'
face_lin_du = './faceset/lin_du.png'
face_liya_tong = './faceset/tong.png'
face_host = './faceset/callon1.jpg'

face_test = './temp.jpg'


from pprint import pformat

def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))

from facepp import API, File
api = API(API_KEY, API_SECRET)
Face = {}
Face['will_lee'] = '8c0b842dbcc1123862c7f5d689b3d9f6'
Face['yulu_hu'] = 'd70ebe294dbbd3510cb1e2293e8789a2'
Face['ming_xie'] = 'f4a32043fc83faf9aed0799c232cba79'
Face['lin_du'] = 'f3d31e6d6b6b4c738f06305ca9f3bf82'
Face['rl_cui'] = 'a95af5f81e852e810bbeca9918daf651'
Face['liya_tong'] = 'e29f1daf710ac028476e69a9346bbb19'
Face['callon'] = '2e62f57aae6e28b25e03f8b18cdd1dd3'
'''
ret = api.faceset.create(outer_id='test')
print_result("faceset create", ret)

Face = {}

res = api.detect(image_file=File(face_liya_tong))
print_result("liya_tong", res)
Face['liya_tong'] = res["faces"][0]["face_token"]

res = api.detect(image_file=File(face_will_lee))
print_result("will_lee", res)
Face['will_lee'] = res["faces"][0]["face_token"]

res = api.detect(image_file=File(face_yulu_hu))
print_result("yulu_hu", res)
Face['yulu_hu'] = res["faces"][0]["face_token"]

res = api.detect(image_file=File(face_ming_xie))
print_result("ming_xie", res)
Face['ming_xie'] = res["faces"][0]["face_token"]

res = api.detect(image_file=File(face_lin_du))
print_result("lin_du", res)
Face['lin_du'] = res["faces"][0]["face_token"]

res = api.detect(image_file=File(face_rl_cui))
print_result("rl_cui", res)
Face['rl_cui'] = res["faces"][0]["face_token"]

api.faceset.addface(outer_id='test', face_tokens=Face.itervalues())
'''
ret = api.detect(image_file=File(face_test))
print_result("face_test", ret)
search_result = api.search(face_token=ret["faces"][0]["face_token"], outer_id='test')

print_result('search', search_result)
print '=' * 60
for k, v in Face.iteritems():
    if v == search_result['results'][0]['face_token']:
        print 'The person with highest confidence:', k
        break


#api.faceset.delete(outer_id='test', check_empty=0)




