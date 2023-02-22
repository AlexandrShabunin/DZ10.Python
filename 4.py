for w in ['разработка', 'администрирование', 'protocol', 'standard']:
    q = w.encode('utf-8', 'replace')
    e = q.decode('utf-8')
    print(w, q, e)
