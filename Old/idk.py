
def path_product(start):
    c1, c2, c3 = getCogs(start[0], start[1], start[2])

    clicks = 0
    last_hit = 0

    got_py = got_60 = got_tri = False
    p = q = r = s = None

    while True:
        a = spinCog(clicks, c1)
        b = spinCog(clicks, c2)
        c = spinCog(clicks, c3)

        if not got_py and checkPy(a, b, c):
            p = clicks - last_hit
            last_hit = clicks
            got_py = True

        elif got_py and not got_60 and check60(a, b, c):
            q = clicks - last_hit
            last_hit = clicks
            got_60 = True

        elif got_60 and not got_tri and checktri(a, b, c):
            r = clicks - last_hit
            last_hit = clicks
            got_tri = True

        elif got_tri and checkFib(a, b, c):
            s = clicks - last_hit
            return p * q * r * s

        clicks += 1


answers = []
for f in fib:
    answers.append(path_product(f))

print(min(answers))



































