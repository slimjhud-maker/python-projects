def student_profile(**kwargs):
    print(f"Name: {kwargs['Name']}\nAge: {kwargs['Age']}\nCity: {kwargs['City']}")


student_profile(Name="Jhud", Age=12, City="London")