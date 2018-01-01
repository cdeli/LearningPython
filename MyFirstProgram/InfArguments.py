

# Array defined with asterisk ********
def print_people(*people):
    for person in people: #Person can be anything, its arbitraty
        print("The person is", person)

print_people("Nick", "Corey", "Jim", "Kevin", "Smiley")