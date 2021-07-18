print("Welcome to Access The Marks (ATM)")


def get_roll_number_marks_mapping_from_file(fname: str):
  with open(fname, "r") as fp:
    records = fp.readlines()
    fp.close()
    
  roll_number_mark_map = {}

  for line in records:    
      try:
        data = line.split()
        rollno = data[0]  # because the roll number is the first column
        marklist = [int(i) for i in data[1:]
                  ]  # this will hold the marks of each student
      # is the dame as the og for loop, just usees generators instead
        roll_number_mark_map[rollno] = marklist

      except Exception:
        raise(ValueError("Bad roll number file"))

  return roll_number_mark_map


def repl(roll_number_mark_map):
    while True:
      roll_number_input = (input("roll number to retrieve: ")).upper()
      
      if roll_number_input not in (roll_number_mark_map):
          print("wrong input")
      
      else:

          numofrecords = len(roll_number_mark_map[roll_number_input])
          
          print(roll_number_mark_map[roll_number_input])
          print("Total is", sum(roll_number_mark_map[roll_number_input]))
          print("Number of records is", numofrecords)
          print("Average is",
                sum(roll_number_mark_map[roll_number_input]) / numofrecords)

          (roll_number_mark_map[roll_number_input]).sort()
          
          print("Marks in ascending order:",
                roll_number_mark_map[roll_number_input])

          (roll_number_mark_map[roll_number_input]).sort(reverse=True)
          print("Marks in descending order:",
                roll_number_mark_map[roll_number_input])
          print("max is : ", max(roll_number_mark_map[roll_number_input]))
          print("min is : ", min(roll_number_mark_map[roll_number_input]))
          
          if min(roll_number_mark_map[roll_number_input]) >= 34:
              print("Result: PASS")
          
          else:
              print("Result: FAIL")

          print("-----------------------")

          end()


def end() -> bool:
    while True:
        restart = input("Do you want to query again?(Y/N):").lower()
        print("-----------------------")
        if restart == "y":
            return True
        elif restart == "n":
            print("Thank you for using ATM")
            exit(0)
        else:
            print("Wrong input")


def main():
    roll_number_mark_map = get_roll_number_marks_mapping_from_file(
        ("Filename//a"))
    repl(roll_number_mark_map)


if __name__ == "__main__":
  main()
