ls = ["ivan-ivanov@beegeek.bzz", "ivan-ivanov1@beegeek.bzz", "ivan-ivanov2@beegeek.bzz"]

email = "ivan-ivanov@beegeek.bzz"

count = 0
for i in ls:
    if email in ls:
        count += 1


print(count)