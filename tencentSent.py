'''
Author: 白帝
Date: 2022-04-26 15:50:04
LastEditTime: 2022-06-20 00:39:57
LastEditors: 白帝
Description: 
FilePath: \project\aort\tencentSent.py
'''
# -*- coding: utf-8 -*-
# pip install tencentcloud-sdk-python
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 SMS 模块的client models
from tencentcloud.sms.v20190711 import sms_client, models

# SMS 配置信息 -- 可登录 [短信控制台] 查看
# --- start
SMS_SECRET_ID = ''  # API秘钥管理SecretId
SMS_SECRET_KEY = ''  # API秘钥管理SecretKey
SMS_APPID = ''  # 应用列表SDK AppID
SMS_SIGN = ''  # 签名 - 文字
SMS_TEMPLATE_ID = ''  # 注册模板ID
# --- end

# * 必要步骤
# * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
# * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个
cred = credential.Credential(SMS_SECRET_ID, SMS_SECRET_KEY)
# * 第一个参数是实例化 SMS 的 client 对象
# * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量
client = sms_client.SmsClient(cred, "ap-guangzhou")
# * 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
req = models.SendSmsRequest()
# * 填充请求参数，这里 request 对象的成员变量即对应接口的入参
# * 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
# * 基本类型的设置:
req.SmsSdkAppid = SMS_APPID
req.Sign = SMS_SIGN


def send(phonelists):
    """  发送短信的功能
    :param ==> phonelists - Object -   手机号list
    :return ==> String - 发送状态
    使用示例
    send(['+86150574669'])
    """
    try:
        req.PhoneNumberSet = phonelists  # 如 ['+86150574669',...]
        #
        req.TemplateID = SMS_TEMPLATE_ID
        # 给腾讯云发送请求，让腾讯云发送短信
        resp = client.SendSms(req)
        # resp发送短信后的响应结果，可以用来判断，短信是否发送成功了
        print(resp.SendStatusSet, "<-- 发送结果")
        # for resp_datas in resp.SendStatusSet:
        #     if resp_datas.Code == "Ok":
        #         print('发送成功')
        #         # 发送成功的手机号码，带'+86'
        #         _sms_phone = resp_datas.PhoneNumber
        #         # 发送成功的手机号码，去除'+86'
        #         _phone = _sms_phone.replace('+86', '')
        #         continue # 结束本次循环
        #     print("发送失败")
        return "Ok"
    except TencentCloudSDKException as err:
        return 'error'
