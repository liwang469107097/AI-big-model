"""
https://mp.weixin.qq.com/s/0DWZAc_Q_sbHnJNf5GpiVg
"""
import qrcode

# 二维码内容（链接地址或文字）
data = 'https://www.baidu.com/'
# 生成二维码
img = qrcode.make(data=data)
# 显示二维码
img.show()
# 保存二维码
# img.save('qr.jpg')

