def hyphen(input_string):
  out = input_string.split('_')
  out.sort()
  return '_'.join(out)

hyphen('black_out_friday')
