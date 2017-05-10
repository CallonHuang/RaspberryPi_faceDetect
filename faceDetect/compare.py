API_KEY = "UlV94eEcopnWrufrxwAX7S2LrkhESAL0"
API_SECRET = "uR3wTHOmRDuX456LxhVYvUB6KcCTromL"

api_server_china = 'https://api-cn.faceplusplus.com/facepp/v3/'

face_person_one = './faceset/will_lee.png'
face_person_two = './faceset/ming_xie.png'

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

person_one = api.detect(image_file=File(face_person_one))
print_result("person_one", person_one)

person_two = api.detect(image_file=File(face_person_two))
print_result("person_two", person_two)

compare_result = api.compare(face_token1=person_one["faces"][0]["face_token"], face_token2=person_two["faces"][0]["face_token"])

print_result('compare', compare_result)




