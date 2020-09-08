from flask import Flask, jsonify, render_template, request, json
import requests
# import json
# from elasticsearch import Elasticsearch, RequestsHttpConnection
# import re

# es = Elasticsearch()
app = Flask(__name__)

@app.route('/', methods= ['GET'])
def get():
    return "hello"


if __name__ == '__main__':
   app.run(debug = True)

# def get_prod(txt):
#     query_body = {
#     "query": {
#         "match": {
#             "name": {
#                 "query": txt,
#                 "fuzziness": 2,
#                 "prefix_length": 1
#             }
#         }
#         }
#     }
#     ans = es.search(index="products", body=query_body)['hits']['hits']
#     return ans

# @app.route('/query', methods=['GET'])
# def get_product():
#     txt = request.args.get('q','')
#     if(len(txt)):
#         ans = get_prod(txt)
#         # print(txt)
#         products = []
#         for pro in ans:
#             name = json.dumps(pro['_source']["name"],ensure_ascii= False)
#             price = pro['_source']['price']["sellPrice"]
#             products.append((name,price))
#         # print(products)
#         # print(ans[0]['_source'])
#         # res = []
#         # for item in ans:
#         #     res.append(item['_source'])
#         # return json.dumps(ans[0]['_source']["name"],ensure_ascii= False)
#         return render_template('tasks.html', products = products)
#     else:
#         return "no txt"