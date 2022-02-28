def foo(my):
    my_new = [float(ll) for ll in my]
    return (sum(my_new))

print(foo(["1.2", "1.3"]))