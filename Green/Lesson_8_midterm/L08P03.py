email = input()

INVALID = "INVALID"
VALID = "VALID"

# check @
check = False
for char in email:
    if char == '@':
        if check:
            print(INVALID)
            exit(0)
        else:
            check = True

if check is False or len(email.split('@')) > 2:
    print(INVALID)
    exit(0)

# split local part and domain name
local_part, domain_name = email.split("@")

# Local Part và Domain Name không được rỗng.
if len(local_part) == 0 or len(domain_name) == 0:
    print(INVALID)
    exit(0)


# Phần Local Part gồm các ký tự ‘A’ – ‘Z’, ‘a’ – ‘z’, ‘0’ – ‘9’ và ký tự đặc biệt: ‘.’ và ‘_’.
for char in local_part:
    if ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9' or char == '.' or char == '_') is False:
        print(INVALID)
        exit(0)

# Domain Name gồm các ký tự ‘A’ – ‘Z’, ‘a’ – ‘z’ và ‘.’.
for char in domain_name:
    if ('A' <= char <= 'Z' or 'a' <= char <= 'z' or char == '.') is False:
        print(INVALID)
        exit(0)

# Domain Name phải có ít nhất một ký tự ‘.’.
check = False
for i in range(len(domain_name) - 1):
    if domain_name[i] == '.':
        if domain_name[i + 1] == '.':
            print(INVALID)
            exit(0)
        check = True

if domain_name[len(domain_name) - 1] == '.':
    check = True

if check is False:
    print(INVALID)
    exit(0)

print(VALID)
