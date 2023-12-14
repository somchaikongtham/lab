plan_text = "ILOVEYOU"
encrypt = ""
for p in plan_text:
    x = ((ord(p) - 65)+3) %26
    x = x + 65
    encrypt = encrypt + chr(x)
    print(p, chr(x))
print(encrypt)

plan_text = ""
for p in encrypt:
    x = ((ord(p) - 65)-3) %26
    x = x + 65
    plan_text = plan_text + chr(x)
    print(p, chr(x))
print(plan_text)