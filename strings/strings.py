languages = "Python Ruby Java Rust Swift Elixir"
language_list = languages.split()
print(language_list)

languages = "Python-Ruby-Java-Rust-Swift-Elixir"
language_list = languages.split()
print(language_list)
language_list = languages.split("-")
print(language_list)
language_list = languages.split("-", 2)
print(language_list)

languages = ["Python", "Ruby", "Java", "Rust"] 
string_languages = ' '.join(languages)
print(string_languages)
string_languages = '-'.join(languages)
print(string_languages)


