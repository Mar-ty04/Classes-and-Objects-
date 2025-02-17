#fn (first name), ln(last name), ph(phone number), addr(address), city, zip)

class Contact:
  def __init__(self, first_name, last_name, phone_number, address, city, zip_code):
    self.fn = first_name
    self.ln = last_name
    self.ph = phone_number
    self.addr = address
    self.city = city
    self.zip = zip_code

  def __lt__(self, other):
    if self.ln == other.ln:
      return self.fn < other.fn
    return self.ln < other.ln

  def __str__(self):
    return f"{self.fn} {self.ln}\n{self.ph}\n{self.addr}\n{self.city} {self.zip}"

  def __repr__(self):
    return (f' {self.fn},{self.ln},{self.ph},{self.addr},{self.city},{self.zip}') 
  