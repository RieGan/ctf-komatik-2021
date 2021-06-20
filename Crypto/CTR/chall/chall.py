from secret import FLAG
import os
from Crypto.Util import *
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from binascii import hexlify
from pwn import xor


KEY = os.urandom(16)

text = b"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

cipher  = AES.new(KEY, AES.MODE_CTR, counter = Counter.new(128))
ct_text = cipher.encrypt(text)

cipher  = AES.new(KEY, AES.MODE_CTR, counter = Counter.new(128))
ct_flag = cipher.encrypt(FLAG)


print(f"ct_text = {hexlify(ct_text)}")
print(f"ct_flag = {hexlify(ct_flag)}")

# ct_text = b'de65cc2e4d56a574a15e8cc80dea5640eaf38bc23c2bab469f68ddc6165900883c68b47d9867939a665829a2f12e47da9d5ff4e9abf05b845841f7c3dfd627fdf85d10a9a38f4a6eaf2ce212827882b589b2da1e1d2376a8924856e9deb97656ed80bcab13efb8e9ecd85fbba2191652a8c5f46cd57844e3cf4f9594dd6fcb4701bb9a462ca8c9efb80953c55449071a0a913124e5595c64622265af2a18bb43634961ec46ffaaacb9a1c204f450ba5ac3de05ca3ee3732d192840c342442eca7bfb7d2e0d3b689a63263d547e6c79136718353dbd6daa0e183ea0fec3fb486f6227b35a432028ad4ea4d4360ae2716814bf9b25c30496b13f8cae642dd5206550cb856d62fff705bf77d22f076847fb46e71d0c9c4820e95fdf5dc8e251bb5fa56322edc74bd6b5cf5edcb7125c40bc30a9168195cb85c97afba01ab250f662af6e9c730d4aaa083f6e244a972a2f38a6ba77bfc8424c2628098bb0a577b808db4e3278d4a882f5ab86872137e9e5ba2400351e0cb6b4b50b7f0a6321cb8324e1c3a948924d6c2a01331a298e1d202ece7e5178764aab4b15a95c4fe7be28603997555823f093af40873079692438677f165480453462e3883d90acac6eea4c3489be442da24c400cd82b0fd6a39555333ebaff0d5055ef72d4a65f1fc06d781cbc9e3a103dad6a90a116accd75858a140d843c47e42932f71a9d7a8ac1a6cf8c59fc0fa0c3c40c0d97cebbe902544c61cfc7fb5bbab6f2db39fffbbaeedc2bca390813b10e102c73c3cdeda120afe11a53381ce8173376e016defeda35'
# ct_flag = b'd945f30a743fa747866d9a9f0ce0295af7c197c12a60bc6c9e6ccf833d4f0c8e7966bf028f6686d273587ff3ba3a'