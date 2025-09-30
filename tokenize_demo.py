import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
text = "Je suis un ordinateur"

#représentation des tokens en texte
print([enc.decode_single_token_bytes(t).decode('utf-8', 'replace') for t in enc.encode(text)])

#Token ids
print(enc.encode(text))
