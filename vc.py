import requests,random,colorama
from colorama import Fore
print("""
visa checker
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣞⣠⣤⡴⢒⣿⣥⡆⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡄⢀⣴⢟⢛⡹⠋⣿⡧⠖⢉⡽⣿⠉⠻⢯⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡼⣷⡏⠁⢺⣸⡁⣸⣾⡥⢤⣾⣾⡇⢀⣀⣀⠈⢽⠂⠀⠀⠀⠀⠀By 6G7R
⢀⠀⣰⠃⣾⣝⡶⠚⣻⠋⠁⠀⠀⠀⠀⠙⠉⠛⠿⣵⢄⡀⠹⡶⠄⠀⠀⠀⠀⠀insta : @6g7r
⢿⠷⣿⣖⣾⠋⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠈⠓⣌⣃⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣄⣸⠏⡇⠀⠀⠀⠀⠀⢢⡀⠀⠀⠀⠀⠈⣇⡀⠀⣼⣩⣝⠃⢘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢘⣇⣉⣻⢇⠔⢋⣒⣶⣤⣼⠏⠲⡶⢤⣴⣶⣿⡉⠙⠻⣖⠺⣷⠨⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⢻⠛⢧⠀⣾⡟⣿⡯⠟⠉⣇⠀⠀⠘⠟⠛⢻⠟⠃⠀⣏⢻⣿⣦⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣷⣿⡄⠀⠁⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⢸⡇⠀⠀⣿⢫⣿⣭⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣏⣇⠀⠀⠀⠀⠀⠀⠳⠖⠀⠀⠀⠀⠈⠀⠀⢰⡿⣾⣼⡿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣿⠀⠀⠀⢀⣀⡠⠤⠤⠤⠤⠤⠖⠚⠁⠀⢸⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣿⣇⠀⠀⠈⠀⠠⠴⠖⠒⠰⠂⠀⠀⠀⢠⣾⡿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢧⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⡿⢇⢻⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣤⣤⣤⣤⣤⣤⣴⢾⣿⣿⣿⢧⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⠻⢼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠉⠛⠋⡿⣿⣿⣽⣿⣿⣿⠗⠀⠀⣻⣴⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠛⢿⠿⡽⠻⠃⣃⣴⣾⣿⣿⣿⣿⣷⣤⣀⣀⡀api:telegram :@RevengeReBack
⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠈⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⢀⠴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠀⠀⠀⠀⣠⣾⠀⠀⠀⢀⡠⠞⣁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⣠⣾⠟⠁⠀⡠⠒⠉⢰⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⣼⣿⡏⠙⣲⠊⠀⣤⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡇

    """)
class v:


    
  def test(self):
    self.good=0
    self.bad=0
    self.error=0
    print("1 - check visa / 2 - get random visa ")
    self.i=input(">>>")
    
    if "1" in self.i:
      self.inp=input("name File : ")
      file=open(self.inp,"r").read().splitlines()
      for file in file:
        self.req=requests.get(f"https://reback.trakosdiaa1.repl.co/cc?c={file}").text

        if "success" in self.req:
          print(f"\r Hits Visa {Fore.GREEN}[   {self.good}  ] {Fore.WHITE}- Bad Visa {Fore.RED}[   {self.bad}  ]",end="")
          self.good += 1
          with  open(f"hits visa.txt", "a") as mix:
            mix.write(f"{f}\n")
            mix.close()
          
        else :
          print(f"\r Hits Visa {Fore.GREEN}[   {self.good}  ] {Fore.WHITE}- Bad Visa {Fore.RED}[   {self.bad}  ]",end="")
          self.bad += 1
    if "2" in self.i:
      self.dn=0
      self.io=int(input("How many ?: "))
      for i in range(self.io):
        self.co = "".join(random.choice("1234567890") for _ in range(16))
        self.co1 = "".join(random.choice("23456789") for _ in range(1))
        self.co2 = "".join(random.choice("3456789") for _ in range(1))
        self.co3 = "".join(random.choice("1234567890") for _ in range(3))
        with open("visaDone.txt","a") as d7:
          d7.write(f"{self.co}|{self.co1}|2{self.co2}|{self.co3} \n")
          d7.close()
        print(f"\r Done make visa > {self.dn}")
        self.dn+=1
vv=v()
vv.test()
