
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def main():
    serialize=Serializer("secretKey",60)
    s="123456"
    res=serialize.dumps(s)
    res2=serialize.loads(res)
    print(res)

def main2():
    serialize=Serializer("secretKey",60)
    s=str(input('输入密钥:'))
    res=serialize.loads(s)
    print(res)

if __name__ == "__main__":
    main2()