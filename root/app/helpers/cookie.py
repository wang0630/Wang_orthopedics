def test_and_set_cookie(res, cookie, id):
  cookie_list = cookie.split('&') if cookie else []
  if id in cookie_list:
    # Make the most recently visited id the first element in the list
    pos = cookie_list.index(id)
    cookie_list = [cookie_list[pos], *cookie_list[:pos], *cookie_list[pos + 1:]]
  else:
    if (len(cookie_list) >= 5):
      cookie_list[-1] = id
    else:
      cookie_list.append(id)
  new_cookie = '&'.join(cookie_list)
  res.set_cookie('recent_view', new_cookie, max_age=86400, httponly=True)
