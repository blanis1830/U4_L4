# Blayne Hoy
# U4 L1

class ArrayStack():
  def __init__(self):
    """Initiliaze stack and size"""
    self.__stack = []
    self.__size = 0

  def push(self, elem):
    """Pushes new element to the top of the stack"""
    self.__stack.append(elem)
    self.__size += 1
  
  def pop(self):
    """Removes and returns top element of a stack"""
    if self.__is_empty():
      raise IndexError("Empty Stack")
    top_element = self.__stack[-1]
    self.__stack = self.__stack[:-1]
    self.__size -= 1
    return top_element
  
  def top(self):
    """Returns top element of a stack without returning it"""
    if self.__is_empty():
      raise IndexError("Empty Stack")
    return self.__stack[-1]
  
  def __is_empty(self):
    """Checks if stack is empty"""
    return self.__size == 0

  def __len__(self):
    """Returns amount of elements in the stack"""
    return self.__size

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out

