import json
import qrcode
val = json.loads(open('asset.json').read())
for i in range(len(val)):
    strs = f"file{i+1}"
    img = qrcode.make(val[strs])
    img.save(strs + ".jpg")
    print("QR Code Generated")
