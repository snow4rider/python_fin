from accounting import *

def main():
  a = Interest(principal = 300, interest_rate = 5, time = 30, n = 1)

  print(a.compound_interest())

if __name__ == "__main__":
    # execute only if run as a script
    main()