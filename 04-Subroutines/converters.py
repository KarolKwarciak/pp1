converters.py

def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

if __name__ == "__main__":
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')


import converters
print('## Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
