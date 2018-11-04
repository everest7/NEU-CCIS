from string_processor import StringProcessor


def main():
    sp = StringProcessor()
    line = input("Input a line:\n")
    print(sp.process_string(line))

main()

# Try with these inputs:
# bes^mc*uer^xlt*a
# nas*o*veul^zit^no^pr
# zeM^un-e*0 t^a*l t^75*4a1:^s35*A,P ^2NM* ,^Mc.+GcO^ t^3*,0^2 ^5m0*x81^
