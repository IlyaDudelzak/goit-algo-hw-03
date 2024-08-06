def normalize_phone(phone_number):
  phone_number = phone_number.replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace("-", "")

  if(phone_number.startswith("0")):
    phone_number = "+38" + phone_number
  elif(phone_number.startswith("380")):
    phone_number = "+" + phone_number

  return phone_number
