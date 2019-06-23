a,b,c = map(int,input("Enter urchins: BIG, MEDIUM, SMALL (space sep)").split())
a_p =3*a
b_p =2*b
c_p =c
total_points = a_p + b_p + c_p
xp = (total_points // 300) * 3000
print("XP to be gained: " + str(xp))
