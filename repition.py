

# for key in user:
#     print(key, ":", user[key])

#Looping list of Dictionaries
list_of_users=[ {
        "first_name" : "Johnny",
        "last_name" : "Tadea",
        "age" : 23,
        "average" : 82.54,
        "list_subjects" : ["Programming", "Mathematics", "English"]
    },
    {
        "first_name" : "Rose",
        "last_name" : "Tadea",
        "age" : 23,
        "average" : 82.54,
        "list_subjects" : ["Programming", "Mathematics", "English"]
    },
    {
        "first_name" : "Angel",
        "last_name" : "Tadea",
        "age" : 27,
        "average" : 86,
        "list_subjects" : ["Programming", "Mathematics", "English"]
    },
]
for key in list_of_users:
    for x in key:
        print(x, ":", key[x])