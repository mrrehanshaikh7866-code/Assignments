assignments = ["maths assignment","python assignment","java assignment"]
new_assignment =input("enter the new assignment: ")
assignments.append(new_assignment)
print("current assignment list: ",assignments)
completed_assignment = input("enter the completed assignment to remove :")
if completed_assignment in assignments:
  assignments.remove(completed_assignment)
  print("assignment removed successfully :")
else:
  print("assignment not found !")
for assignment in assignments:
  print (assignment)