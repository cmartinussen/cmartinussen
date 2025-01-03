from collections import Counter
def read_file(text):
  with open(text, 'r') as file:
    lines = file.readlines()
    return lines
  
def calculate_distance(lines):
  left_list = []
  right_list = []
  for line in lines:
    left, right = map(int, line.strip().split())
    left_list.append(left)
    right_list.append(right)
  
  #print(left_list)
  #print(right_list)
  
  left_sorted = sorted(left_list)
  #print(left_sorted)
  right_sorted = sorted(right_list)
  #print(right_sorted)

  total_distance = 0
  for left, right in zip(left_sorted, right_sorted):
    total_distance += abs(left - right)

  return total_distance

def calculate_similarity(lines):
  left_list = []
  right_list = []
  for line in lines:
    left, right = map(int, line.strip().split())
    left_list.append(left)
    right_list.append(right)
  
  #print(left_list)
  #print(right_list)
    # Count occurrences of each number in the right list
  right_count = Counter(right_list)
 
    # Calculate the similarity score
  similarity_score = 0
  for number in left_list:
    #print(str(number))
    similarity_score += number * right_count[number]
    print(str(number) +": " + str(right_count[number]))

  return similarity_score
    
#part 1
#print(calculate_distance(read_file("input1.txt")))

#part 2
print(calculate_similarity(read_file("input1.txt")))