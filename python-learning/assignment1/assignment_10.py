def greet(time, naam):
    if ( time.lower() == 'morning'):
        print(f'''Good morning..! {naam}
 Have a nice day.''')
    if ( time.lower() == 'afternoon'):
        print(f'''Good afternoon..! {naam}
 Have a nice day.''')
    if ( time.lower() == 'evening'):
        print(f'''Good evening..! {naam}
 How was your day?''')

naam = input('Enter your name: ')
time = input('Enter the time(morning,evening,afternoon): ')
greet(time , naam)