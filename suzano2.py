nome= "Dayane"
mensagem= f"""Seja bem vinda, {nome}!. Você é a Miss Python."""
print(mensagem)
print("Name:", nome)
for i in nome:
    print(f"Iteration {i}: {i}") # Iterating through each character in the string

print("Length of name:", len(nome)) # Length of the string
print(nome[::-1]) # Reversing the string
