def convert_date_to_bc(target):
  if not isinstance(target, list):
    target = [target]
  
  for a in target:
    if 'date' in a:
      a['date'] = f"{a['date'].year}/{a['date'].month}/{a['date'].day}"

def convert_date_to_roc(target):
  if not isinstance(target, list):
    target = [target]
  
  for a in target:
    if 'date' in a:
      a['date'] = f"民國{a['date'].year - 1911} / {a['date'].month} / {a['date'].day}"
