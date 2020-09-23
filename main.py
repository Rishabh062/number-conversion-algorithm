print("Welcome to number_conversion:1\n")
print("1.decimal to binary\n2.binary to decimal\n3.decimal to octal\n4.octal to decimal\n5.decimal to hexadecimal\n6.hexadecimal to decimal")
n=int(input())
if(n==1):
  def deci_bin():
    print("Enter decimal number:\n")
    k=int(input())
    temp=k
    pv=1
    rem=1
    ans=0

    while(temp):
      rem=temp%2
      ans+=pv*rem
      pv=pv*10
      temp=temp//2
    print(ans)
  deci_bin()
if(n==2):
  def bin_deci():
    print("Enter binary number:\n")
    k=int(input())
    temp=k
    dec=0
    t=1
    base=1
    while(temp):
      t=temp%10
      dec=dec+(t*base)
      base=base*2
      temp=temp//10
    print(dec)
  bin_deci()

if(n==3):
  def deci_oct():
    k=int(input("Enter decimal no.\n"))
    temp,oct,rem,pv=k,0,1,1
    while(temp):
      rem=temp%8
      oct+=rem*pv
      pv=pv*10
      temp//=8
    print(oct)
  deci_oct()
  
if(n==4):
  def oct_deci():
      n=int(input("Enter octal no.\n"))
      temp=n
      ans,pv,rem,t=0,1,1,1
      while(temp):
        t=temp%10
        ans+=pv*t
        pv=pv*8
        temp//=10
      print(ans)
  oct_deci()
if(n==5):
  def deci_hex():
    k=int(input("Enter decimal no.\n"))
    print(hex(k).lstrip("0x").rstrip("L"))
  deci_hex()
if(n==6):
  def hex_deci():
    k=input("Enter hexadecimal no.\n")
    dec=int(k,16)
    print(str(dec))
  hex_deci()

