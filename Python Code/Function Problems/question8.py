def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Shaktiman", power="lazer")
print_kwargs(power="lazer")
print_kwargs(name="Shaktiman", power="lazer", enemy="Dr.Jackal")