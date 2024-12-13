# # Implementation & testing of the ArrayStack class

from StackClass import ArrayStack
import os

def balanced(str):
  stack = ArrayStack()
  matching_brackets = {')': '(', ']' : '[', '}' : '{'}
  for char in str:
    if char in "({[":
      stack.push(char)
    elif char in ")}]":
      if len(stack) == 0 or stack.pop() != matching_brackets[char]:
        return False
  return len(stack) == 0

def main():
  test1 = "()(()){([()])}"
  test2 = "((()(()){([()])}))"
  test3 = ")(()){([()])]"
  test4 = "({[])}"
  test5 = "("

  for test in [test1, test2, test3, test4, test5]:
    result = "Balanced" if balanced(test) else "Unbalanced"
    print(f"{test} - {result}")

if __name__ == "__main__":
    os.system("clear")
    main()