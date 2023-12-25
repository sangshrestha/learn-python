def test(fn, input, output):
  results = []
  success = True
  length = len(input)
  for i in range(length):
    fn_out = fn(input[i])
    match = fn_out == output[i]
    if match:
      results.append("Passed ✅")
    else:
      success = False
      results.append(f"❌ Failed: '{fn_out}' does not match '{output[i]}'")
  print(results)
  return success
