students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
result_dict={}
for k,v in (zip(students, subjects)):
  result_dict[k]=v

print(result_dict)
